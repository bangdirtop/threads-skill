#!/usr/bin/env python3
"""
humanize.py - bersihkan jejak mesin dari draf Threads.

Pemakaian:
    python3 humanize.py draf.txt --report          # tampilkan hasil + apa yang diubah
    python3 humanize.py draf.txt -o bersih.txt     # simpan hasil
    cat draf.txt | python3 humanize.py - --report

Yang diperbaiki otomatis:
    1. Karakter tak terlihat (zero-width, soft hyphen, BOM, penanda arah) dihapus.
       Spasi aneh (non-breaking, narrow) jadi spasi biasa.
    2. Em dash dan en dash: DILARANG TOTAL. Semuanya diganti koma (atau tanda
       hubung kalau di antara dua angka, misal 10-20).
    3. Tipografi: kutip melengkung jadi lurus, elipsis satu karakter jadi tiga titik.
    4. Leksikon slop dari slop.json diganti kata biasa atau dihapus.

Yang hanya ditandai (perlu ditulis ulang manusia): pola struktur di slop.json,
misalnya "bukan sekadar X, tapi Y", "Hasilnya?", pengumuman kejujuran.
"""
import argparse
import json
import os
import re
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
URL = re.compile(r"https?://\S+|www\.\S+")


def muat_slop():
    with open(os.path.join(DIR, "slop.json"), encoding="utf-8") as f:
        return json.load(f)


def _cocokkan_kapital(asli, ganti):
    if not ganti:
        return ganti
    if asli.isupper() and len(asli) > 1:
        return ganti.upper()
    if asli[0].isupper():
        return ganti[0].upper() + ganti[1:]
    return ganti


def _rapikan(teks):
    teks = re.sub(r"[ \t]+", " ", teks)
    teks = re.sub(r" +([,.!?;:])", r"\1", teks)
    teks = re.sub(r",\s*,", ",", teks)
    teks = re.sub(r",\s*([.!?])", r"\1", teks)
    teks = re.sub(r"([.!?])\s*,", r"\1", teks)
    teks = re.sub(r"(?m)^[ ,]+", "", teks)
    teks = re.sub(r"(?m)[ ]+$", "", teks)
    # huruf kapital di awal kalimat setelah frasa dihapus
    teks = re.sub(r"(^|[.!?]\s+|\n)([a-z])", lambda m: m.group(1) + m.group(2).upper(), teks)
    return teks


def bersihkan(teks, slop=None):
    slop = slop or muat_slop()
    ubah = []

    # 1. tak terlihat
    n = sum(teks.count(c) for c in slop["tak_terlihat"])
    for c in slop["tak_terlihat"]:
        teks = teks.replace(c, "")
    sisa = re.findall(r"[\u2000-\u200f\u2028-\u202f\u205f-\u206f\ufff0-\uffff]", teks)
    for c in set(sisa):
        if c not in slop["spasi_aneh"]:
            n += teks.count(c)
            teks = teks.replace(c, "")
    if n:
        ubah.append(f"{n} karakter tak terlihat dihapus")
    n = sum(teks.count(c) for c in slop["spasi_aneh"])
    for c in slop["spasi_aneh"]:
        teks = teks.replace(c, " ")
    if n:
        ubah.append(f"{n} spasi aneh dijadikan spasi biasa")

    # 2. em dash dan en dash, larangan total
    n = teks.count("\u2014") + teks.count("\u2013") + teks.count("\u2015")
    if n:
        teks = re.sub(r"(\d)\s*[\u2013\u2014]\s*(\d)", r"\1-\2", teks)
        teks = re.sub(r"\s*[\u2014\u2013\u2015]\s*", ", ", teks)
        teks = re.sub(r"(?<=\w)\s+--\s+(?=\w)", ", ", teks)
        ubah.append(f"{n} em/en dash diganti (larangan total)")

    # 3. tipografi
    n = 0
    for k, v in slop["tipografi"].items():
        c = teks.count(k)
        if c:
            n += c
            teks = teks.replace(k, v)
    if n:
        ubah.append(f"{n} tanda tipografi diluruskan")

    # 4. leksikon, URL dilindungi
    simpan = {}

    def lindungi(m):
        kunci = f"\x00{len(simpan)}\x00"
        simpan[kunci] = m.group(0)
        return kunci

    teks = URL.sub(lindungi, teks)
    for frasa in sorted(slop["ganti"], key=len, reverse=True):
        ganti = slop["ganti"][frasa]
        pola = re.compile(r"(?<![\w-])" + re.escape(frasa) + r"(?![\w-])", re.IGNORECASE)
        hit = pola.findall(teks)
        if hit:
            teks = pola.sub(lambda m: _cocokkan_kapital(m.group(0), ganti), teks)
            ubah.append(f'"{frasa}" -> "{ganti}" ({len(hit)}x)' if ganti else f'"{frasa}" dihapus ({len(hit)}x)')
    for k, v in simpan.items():
        teks = teks.replace(k, v)

    teks = _rapikan(teks)
    return teks, ubah


def tandai_struktur(teks, slop=None):
    slop = slop or muat_slop()
    temuan = []
    for s in slop["struktur"]:
        hit = re.findall(s["regex"], teks)
        jumlah = len(hit)
        if s["nama"] == "tiga serangkai" and jumlah < 2:
            continue
        if jumlah:
            temuan.append((s["nama"], jumlah, s["saran"]))
    tagar = re.findall(r"(?<!\w)#\w+", teks)
    if len(tagar) > 1:
        temuan.append(("tag topik lebih dari satu", len(tagar), "Threads memakai satu tag topik per postingan. Sisakan satu."))
    satu_kata = [b for b in teks.splitlines() if re.fullmatch(r"\s*\w+[.!]\s*", b)]
    if len(satu_kata) >= 2:
        temuan.append(("baris satu kata untuk drama", len(satu_kata), "Gabungkan ke kalimat di dekatnya."))
    return temuan


def main():
    ap = argparse.ArgumentParser(description="Bersihkan jejak mesin dari draf Threads.")
    ap.add_argument("berkas", help="file draf, atau - untuk stdin")
    ap.add_argument("-o", "--output", help="simpan hasil ke file ini")
    ap.add_argument("--report", action="store_true", help="tampilkan apa saja yang diubah")
    a = ap.parse_args()

    teks = sys.stdin.read() if a.berkas == "-" else open(a.berkas, encoding="utf-8").read()
    slop = muat_slop()
    hasil, ubah = bersihkan(teks, slop)
    struktur = tandai_struktur(hasil, slop)

    if a.output:
        with open(a.output, "w", encoding="utf-8") as f:
            f.write(hasil)
    if a.report or not a.output:
        print(hasil)
    if a.report:
        print("\n" + "=" * 40)
        print("DIUBAH OTOMATIS" if ubah else "DIUBAH OTOMATIS: tidak ada")
        for u in ubah:
            print("  - " + u)
        print("PERLU DITULIS ULANG MANUAL" if struktur else "POLA STRUKTUR: bersih")
        for nama, j, saran in struktur:
            print(f"  - {nama} ({j}x): {saran}")


if __name__ == "__main__":
    main()
