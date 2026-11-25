#!/usr/bin/env python3
"""
detect.py - nilai seberapa manusiawi sebuah draf Threads, lima pemeriksaan.

Pemakaian:
    python3 detect.py draf.txt                 # nilai satu draf
    python3 detect.py sebelum.txt sesudah.txt  # bandingkan dua versi

Lima pemeriksaan, 0-100, makin tinggi makin manusiawi:
    VARIASI   panjang kalimat bervariasi wajar, tidak seragam seperti mesin
    KONKRET   angka, nama, tanggal, nominal per 100 kata
    SLOP      kata dan frasa klise AI per 100 kata (dari slop.json)
    JEJAK     karakter tak terlihat, kutip melengkung, dan em/en dash
    SUARA     orang pertama/kedua, ragam lisan, tanpa pola struktur AI

Putusan: skor = 60% rata-rata + 40% pemeriksaan terlemah.
LOLOS bila skor >= 70 dan tidak ada pemeriksaan di bawah 55.
Em dash atau en dash satu pun = GAGAL, apa pun skornya (larangan total).

Jujur soal batasnya: ini heuristik lokal, tidak memanggil GPTZero, Originality,
Turnitin, atau detektor lain, dan tidak bisa menjanjikan hasil mereka.
"""
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from humanize import muat_slop, tandai_struktur  # noqa: E402

LISAN = [
    "nggak", "ngga", "gak", "ga ", "udah", "aja", "banget", "sih", "kok", "deh", "dong",
    "kayak", "gimana", "emang", "bikin", "pake", "pakai", "gue", "gw", "lo ", "lu ",
    "aku", "saya", "kamu", "kalian", "kita", "i ", "i'm", "you", "don't", "can't",
]


def kalimat(teks):
    bagian = re.split(r"(?<=[.!?])\s+|\n+", teks.strip())
    return [b for b in bagian if len(b.split()) >= 1]


def nilai(teks, slop):
    kata = re.findall(r"\w+", teks)
    n = max(len(kata), 1)
    low = " " + teks.lower() + " "
    catatan = []

    # VARIASI
    panjang = [len(k.split()) for k in kalimat(teks)]
    if len(panjang) >= 3:
        rata = statistics.mean(panjang)
        cv = statistics.pstdev(panjang) / rata if rata else 0
        variasi = max(0, min(100, int(40 + cv * 150)))
        if variasi < 55:
            catatan.append("VARIASI: kalimat terlalu seragam panjangnya")
    else:
        variasi = 75

    # KONKRET
    angka = len(re.findall(r"\d[\d.,]*", teks))
    nama = len(re.findall(r"(?<=[a-z0-9,] )[A-Z][a-zA-Z]{2,}", teks))
    per100 = (angka * 2 + nama) / n * 100
    konkret = max(0, min(100, int(per100 * 9)))
    if konkret < 55:
        catatan.append("KONKRET: tambah angka, nama, tanggal, atau nominal (jangan dikarang)")

    # SLOP
    hit = 0
    for frasa in slop["ganti"]:
        hit += len(re.findall(r"(?<![\w-])" + re.escape(frasa) + r"(?![\w-])", teks, re.IGNORECASE))
    slop_per100 = hit / n * 100
    skor_slop = max(0, int(100 - slop_per100 * 35))
    if hit:
        catatan.append(f"SLOP: {hit} kata/frasa klise, jalankan humanize.py")

    # JEJAK
    dash = teks.count("\u2014") + teks.count("\u2013") + teks.count("\u2015")
    tak = sum(teks.count(c) for c in slop["tak_terlihat"])
    kutip = sum(teks.count(c) for c in "\u201c\u201d\u2018\u2019…")
    jejak = max(0, 100 - dash * 50 - tak * 40 - kutip * 10)
    if dash:
        catatan.append(f"JEJAK: {dash} em/en dash, DILARANG")
    if tak:
        catatan.append(f"JEJAK: {tak} karakter tak terlihat")

    # SUARA
    lisan = sum(1 for m in LISAN if m in low)
    struktur = tandai_struktur(teks, slop)
    suara = max(0, min(100, 45 + lisan * 12 - sum(j for _, j, _ in struktur) * 15))
    if struktur:
        catatan.append("SUARA: pola struktur AI: " + ", ".join(nm for nm, _, _ in struktur))
    elif suara < 55:
        catatan.append("SUARA: terdengar seperti rilis pers, pakai kamu/saya dan ragam lisan")

    cek = {"VARIASI": variasi, "KONKRET": konkret, "SLOP": skor_slop, "JEJAK": jejak, "SUARA": suara}
    skor = round(statistics.mean(cek.values()) * 0.6 + min(cek.values()) * 0.4)
    if dash:
        putusan = "GAGAL"
    elif skor >= 70 and min(cek.values()) >= 55:
        putusan = "LOLOS"
    else:
        putusan = "TINJAU"
    return cek, skor, putusan, catatan


def cetak(nama, teks, slop):
    cek, skor, putusan, catatan = nilai(teks, slop)
    print(f"== {nama}")
    for k, v in cek.items():
        bar = "#" * (v // 10)
        print(f"  {k:<8} {v:>3}  {bar}")
    print(f"  SKOR     {skor:>3}  {putusan}")
    lemah = min(cek, key=cek.get)
    print(f"  terlemah: {lemah}")
    for c in catatan:
        print("  - " + c)
    return skor


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    slop = muat_slop()
    skor = []
    for p in sys.argv[1:3]:
        with open(p, encoding="utf-8") as f:
            skor.append(cetak(p, f.read(), slop))
    if len(skor) == 2:
        print(f"\nSELISIH  {skor[1] - skor[0]:+d}")


if __name__ == "__main__":
    main()
