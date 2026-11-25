#!/usr/bin/env python3
"""
lint_post.py - periksa postingan atau utas Threads sebelum diposting.

Pemakaian:
    python3 lint_post.py draf.txt
    python3 lint_post.py utas.txt --keywords "prompt video,konten AI"

Untuk utas (beberapa postingan bersambung), pisahkan tiap postingan dengan
baris berisi tiga tanda hubung saja:

    Baris pertama postingan 1
    ---
    Postingan 2
    ---
    Postingan 3

Aturan yang diperiksa:
    GAGAL  lebih dari 500 karakter per postingan (batas Threads)
    GAGAL  ada em dash atau en dash (larangan total)
    GAGAL  ada karakter tak terlihat
    GAGAL  lebih dari satu tag topik di satu postingan
    AWAS   baris pertama dibuka sapaan, emoji, atau lebih dari 120 karakter
    AWAS   lebih dari satu ajakan di seluruh postingan/utas
    AWAS   lebih dari satu link, atau link di postingan pertama utas
    AWAS   emoji lebih dari 4 per 100 karakter
    AWAS   kata kunci pencarian (--keywords) tidak muncul di teks
"""
import argparse
import re
import sys

BATAS = 500
TAK_TERLIHAT = re.compile("[\u200b-\u200f\u2060-\u2064\ufeff\u00ad\u202a-\u202e\u2066-\u2069]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-↪]")
TAGAR = re.compile(r"(?<![\w/])#[\w]+")
LINK = re.compile(r"https?://\S+|www\.\S+|\b\w+\.(com|id|app|md|co|io|net|org|ai)(/\S*)?\b", re.IGNORECASE)
SAPAAN = re.compile(r"^(halo|hai|hi|hello|selamat (pagi|siang|sore|malam)|assalamu|guys|gaes|warga|teman-teman|temen-temen|oke jadi|jadi gini|izin)\b", re.IGNORECASE)
AJAKAN = [
    r"\brepost\b", r"\bsimpan\b", r"\bsave\b", r"\bfollow\b", r"\bikuti\b",
    r"\bkomen(tar)?\b", r"\bbalas\b", r"\bketik\b", r"\bklik\b", r"\bdm\b",
    r"\blink (di|ada di)\b", r"\bcek (link|bio)\b", r"\bdaftar\b", r"\bbeli\b",
    r"\bshare\b", r"\bbagikan\b", r"\bvote\b", r"\bpilih\b",
]


def periksa(teks, keywords):
    bagian = [b.strip("\n") for b in re.split(r"(?m)^---\s*$", teks)]
    bagian = [b for b in bagian if b.strip()]
    gagal, awas, info = [], [], []

    for i, b in enumerate(bagian, 1):
        label = f"postingan {i}" if len(bagian) > 1 else "postingan"
        n = len(b)
        if n > BATAS:
            gagal.append(f"{label}: {n} karakter, lebih {n - BATAS} dari batas 500")
        d = b.count("\u2014") + b.count("\u2013") + b.count("\u2015")
        if d:
            gagal.append(f"{label}: {d} em/en dash, ganti koma, titik dua, atau tulis ulang")
        t = len(TAK_TERLIHAT.findall(b))
        if t:
            gagal.append(f"{label}: {t} karakter tak terlihat, jalankan threads-human/humanize.py")
        tag = TAGAR.findall(b)
        if len(tag) > 1:
            gagal.append(f"{label}: {len(tag)} tag topik ({' '.join(tag)}), Threads memakai satu per postingan")
        e = len(EMOJI.findall(b))
        if n and e / n * 100 > 4:
            awas.append(f"{label}: {e} emoji di {n} karakter, terlalu ramai")

    pertama = bagian[0].strip().splitlines()[0] if bagian else ""
    if SAPAAN.match(pertama):
        awas.append("baris pertama dibuka sapaan, buang dan mulai dari klaim atau angka")
    if pertama and EMOJI.match(pertama):
        awas.append("baris pertama dibuka emoji")
    if len(pertama) > 120:
        awas.append(f"baris pertama {len(pertama)} karakter, usahakan di bawah 120 supaya terbaca sekali lirik")
    if pertama and TAGAR.search(pertama):
        awas.append("tag topik ada di baris pertama, pindah ke akhir")

    semua = "\n".join(bagian)
    jumlah_link = len(LINK.findall(semua))
    if jumlah_link > 1:
        awas.append(f"{jumlah_link} link, satu tujuan saja")
    if len(bagian) > 1 and LINK.search(bagian[0]):
        awas.append("link di postingan pertama utas, taruh di postingan terakhir")
    if jumlah_link:
        info.append("link di Threads bisa diklik, tidak perlu 'link di bio'")

    low = semua.lower()
    ajakan = [p for p in AJAKAN if re.search(p, low)]
    kalimat_ajakan = [k for k in re.split(r"(?<=[.!?])\s+|\n", semua) if any(re.search(p, k.lower()) for p in AJAKAN)]
    if len(kalimat_ajakan) > 1:
        awas.append(f"{len(kalimat_ajakan)} kalimat berisi ajakan, pilih satu: " + " | ".join(k.strip()[:50] for k in kalimat_ajakan[:3]))
    elif not ajakan:
        info.append("tidak ada ajakan, wajar untuk postingan opini, cek apakah memang disengaja")

    for kw in [k.strip() for k in (keywords or "").split(",") if k.strip()]:
        if kw.lower() not in low:
            awas.append(f"kata kunci pencarian \"{kw}\" tidak ada di teks")
        else:
            info.append(f"kata kunci \"{kw}\" ada")

    if len(bagian) > 1:
        info.append(f"utas {len(bagian)} postingan")
        if len(bagian) > 10:
            awas.append("utas lebih dari 10 postingan, pertimbangkan album atau lampiran teks")
    return bagian, gagal, awas, info


def main():
    ap = argparse.ArgumentParser(description="Periksa postingan atau utas Threads.")
    ap.add_argument("berkas", help="file draf, atau - untuk stdin")
    ap.add_argument("--keywords", help="kata kunci pencarian, dipisah koma")
    a = ap.parse_args()
    teks = sys.stdin.read() if a.berkas == "-" else open(a.berkas, encoding="utf-8").read()
    bagian, gagal, awas, info = periksa(teks, a.keywords)

    for i, b in enumerate(bagian, 1):
        pertama = b.strip().splitlines()[0] if b.strip() else ""
        print(f"[{i}] {len(b):>3}/500  {pertama[:80]}")
    print()
    for g in gagal:
        print("GAGAL  " + g)
    for w in awas:
        print("AWAS   " + w)
    for x in info:
        print("INFO   " + x)
    status = "PERBAIKI" if gagal else ("SIAP, putuskan tiap AWAS" if awas else "SIAP")
    print(f"\nSTATUS: {status}")
    sys.exit(1 if gagal else 0)


if __name__ == "__main__":
    main()
