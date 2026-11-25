#!/usr/bin/env python3
"""
hookscore.py - beri skor baris pertama postingan Threads dan urutkan beberapa
kandidat sekaligus.

Pemakaian:
    python3 hookscore.py kandidat.txt          # satu kandidat per baris
    python3 hookscore.py --hook "satu baris"   # nilai satu kandidat
    python3 hookscore.py kandidat.txt --json   # keluaran JSON

Yang diukur (lima pemeriksaan lokal, hanya dari teks):
    PANJANG   cukup pendek untuk dibaca sekali lirik
    KONKRET   ada angka, nominal, nama, durasi
    TARUHAN   ada yang dipertaruhkan: uang, waktu, gagal, salah
    DEPAN     isi penting muncul di awal, bukan di ujung
    SASARAN   jelas bicara ke siapa (kamu, kalian, kelompok tertentu)

Yang TIDAK diukur: apakah postingan akan ramai. Skor ini menyaring baris yang
lemah (sapaan, pembukaan basa-basi, tanpa isi konkret). Untuk memilih di antara
dua baris yang sama-sama bagus, data akunmu sendiri (threads-audit) lebih jujur.
"""
import argparse
import json
import re
import sys

SAPAAN = [
    "halo", "hai", "hi ", "hello", "selamat pagi", "selamat siang", "selamat malam",
    "assalamualaikum", "guys", "warga", "teman-teman", "temen-temen", "gaes",
    "di postingan ini", "di thread ini", "di utas ini", "aku mau share", "saya mau share",
    "mau sharing", "izin share", "jadi gini", "oke jadi", "kali ini", "pada kesempatan",
    "in this", "today i", "let's talk", "mari kita bahas", "yuk bahas",
]

TARUHAN = [
    "rugi", "boncos", "gagal", "habis", "hilang", "salah", "bayar", "juta", "ribu",
    "rp", "naik", "turun", "berhenti", "jangan", "stop", "rahasia", "tidak ada yang",
    "ga ada yang", "nggak ada yang", "dipecat", "ditolak", "refund", "sepi", "flop",
    "telat", "terlambat", "kalah", "menang", "closing", "omzet", "untung", "cuan",
    "bangkrut", "utang", "denda", "diblokir", "banned", "takedown", "cost", "lost",
    "mistake", "wrong", "never", "stop",
]

SASARAN = ["kamu", "kalian", "lo ", "lu ", "anda", "you", "buat yang", "untuk yang", "para "]

SATUAN = [
    "detik", "menit", "jam", "hari", "minggu", "bulan", "tahun", "kali", "orang",
    "view", "follower", "order", "video", "postingan", "persen", "%", "x ", "rb", "jt",
]

ANGKA = re.compile(r"\d")
NAMA = re.compile(r"(?<=[a-z0-9,] )[A-Z][a-zA-Z]{2,}")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def kata(teks):
    return re.findall(r"[\w%.,'-]+", teks)


def nilai(teks):
    t = teks.strip()
    low = " " + t.lower() + " "
    w = kata(t)
    n = max(len(w), 1)
    catatan = []

    # PANJANG: 5 sampai 14 kata ideal untuk baris pertama di feed
    if 5 <= n <= 14:
        panjang = 100
    elif n < 5:
        panjang = 70
        catatan.append("sangat pendek, pastikan tetap ada isi")
    elif n <= 20:
        panjang = 100 - (n - 14) * 8
        catatan.append(f"{n} kata, potong ke 14 atau kurang")
    else:
        panjang = max(0, 52 - (n - 20) * 5)
        catatan.append(f"{n} kata, ini paragraf, bukan hook")

    # KONKRET
    konkret_hit = 0
    if ANGKA.search(t):
        konkret_hit += 2
    if NAMA.search(t):
        konkret_hit += 1
    if any(s in low for s in SATUAN):
        konkret_hit += 1
    konkret = min(100, konkret_hit * 35)
    if konkret_hit == 0:
        catatan.append("tidak ada angka, nama, atau durasi")

    # TARUHAN
    tar = sum(1 for s in TARUHAN if s in low)
    taruhan = min(100, tar * 45)
    if tar == 0:
        catatan.append("tidak ada yang dipertaruhkan")

    # DEPAN: posisi kata konkret atau taruhan pertama
    posisi = None
    for i, k in enumerate(w):
        kl = k.lower()
        if ANGKA.search(kl) or any(kl.startswith(s.strip()) for s in TARUHAN if s.strip()):
            posisi = i
            break
    if posisi is None:
        depan = 30
    else:
        rasio = posisi / n
        depan = 100 if rasio <= 0.4 else int(100 - (rasio - 0.4) * 120)
        if rasio > 0.6:
            catatan.append("isi penting baru muncul di ujung, pindah ke depan")

    # SASARAN
    sasaran = 100 if any(s in low for s in SASARAN) else 40

    # Penalti
    penalti = 0
    dash = False
    if any(low.strip().startswith(s.strip()) for s in SAPAAN) or any(s in low[:40] for s in SAPAAN[12:]):
        penalti += 35
        catatan.append("dibuka dengan sapaan atau basa-basi")
    if "\u2014" in t or "\u2013" in t:
        penalti += 25
        dash = True
        catatan.append("ada em dash atau en dash, dilarang, skor dibatasi 40")
    if t and EMOJI.match(t):
        penalti += 15
        catatan.append("emoji di karakter pertama")
    if "#" in t:
        penalti += 10
        catatan.append("tag topik di baris pertama")
    huruf = [c for c in t if c.isalpha()]
    if len(huruf) > 12 and sum(c.isupper() for c in huruf) / len(huruf) > 0.7:
        penalti += 15
        catatan.append("hampir semua huruf kapital")

    total = (panjang * 0.2 + konkret * 0.25 + taruhan * 0.2 + depan * 0.2 + sasaran * 0.15) - penalti
    total = max(0, min(100, round(total)))
    if dash:
        total = min(total, 40)
    label = "KUAT" if total >= 70 else "OKE" if total >= 50 else "LEMAH"
    return {
        "hook": t,
        "skor": total,
        "label": label,
        "rincian": {
            "PANJANG": panjang, "KONKRET": konkret, "TARUHAN": taruhan,
            "DEPAN": depan, "SASARAN": sasaran, "penalti": penalti,
        },
        "catatan": catatan,
    }


def main():
    ap = argparse.ArgumentParser(description="Skor baris pertama postingan Threads.")
    ap.add_argument("berkas", nargs="?", help="file berisi satu kandidat per baris")
    ap.add_argument("--hook", help="nilai satu baris saja")
    ap.add_argument("--json", action="store_true", help="keluaran JSON")
    a = ap.parse_args()

    if a.hook:
        baris = [a.hook]
    elif a.berkas:
        with open(a.berkas, encoding="utf-8") as f:
            baris = [b.strip() for b in f if b.strip()]
    else:
        baris = [b.strip() for b in sys.stdin if b.strip()]
    if not baris:
        sys.exit("Tidak ada kandidat hook.")

    hasil = sorted((nilai(b) for b in baris), key=lambda r: -r["skor"])
    if a.json:
        print(json.dumps(hasil, ensure_ascii=False, indent=2))
        return
    print("HOOK (diurutkan)")
    for r in hasil:
        print(f"  {r['skor']:>3}  {r['label']:<5}  {r['hook']}")
        if r["catatan"]:
            print("             " + "; ".join(r["catatan"]))
    if hasil[0]["skor"] < 50:
        print("\nKandidat teratas di bawah 50. Hook-nya belum ketemu, tulis ulang dari rumus lain.")


if __name__ == "__main__":
    main()
