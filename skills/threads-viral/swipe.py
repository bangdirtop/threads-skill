#!/usr/bin/env python3
"""
swipe.py - urutkan postingan Threads yang dikumpulkan berdasarkan kelipatan
median akunnya sendiri, beri nama rumus hook-nya, dan tulis swipe file.

Pemakaian:
    python3 swipe.py kumpulan.tsv
    python3 swipe.py kumpulan.tsv --out ~/.claude/threads/swipe.md

Format TSV (baris pertama header, dipisah TAB). Kolom wajib:
    akun  follower  median  views  hook
Kolom opsional: format (teks/album/video/utas), balasan, repost, link

    akun	follower	median	views	hook	format
    @contoh	4800	1100	38000	Tidak ada yang bilang kalau ...	album

Kelipatan = views / median akun itu. Di atas 3x = sinyal. Di bawah 1,5x = hari
biasa akun itu, tidak mengajarkan apa-apa, berapa pun angkanya.
"""
import argparse
import csv
import json
import os
import re
import statistics
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
HOOK_DIR = os.path.join(DIR, "..", "threads-hook")
sys.path.insert(0, HOOK_DIR)
from hookscore import nilai as skor_hook  # noqa: E402


def muat_rumus():
    with open(os.path.join(HOOK_DIR, "hooks.json"), encoding="utf-8") as f:
        return json.load(f)["rumus"]


def klasifikasi(hook, rumus):
    low = hook.lower()
    terbaik, hit_terbaik = None, 0
    for r in rumus:
        hit = 0
        for d in r["deteksi"]:
            if re.search(d, low) if any(c in d for c in "\\[]") else d in low:
                hit += 1
        if hit > hit_terbaik:
            terbaik, hit_terbaik = r, hit
    return terbaik


def angka(s):
    s = (s or "").strip().lower().replace(".", "").replace(",", ".")
    kali = 1
    if s.endswith("rb") or s.endswith("k"):
        kali, s = 1000, s.rstrip("rbk")
    elif s.endswith("jt") or s.endswith("m"):
        kali, s = 1_000_000, s.rstrip("jtm")
    try:
        return float(s) * kali
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser(description="Swipe file Threads berbasis kelipatan median.")
    ap.add_argument("tsv")
    ap.add_argument("--out", help="tulis swipe file markdown ke sini")
    a = ap.parse_args()
    rumus = muat_rumus()

    baris = []
    with open(a.tsv, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            v, m = angka(r.get("views")), angka(r.get("median"))
            if not v or not m or not (r.get("hook") or "").strip():
                continue
            h = r["hook"].strip()
            k = klasifikasi(h, rumus)
            s = skor_hook(h)
            baris.append({
                "akun": r.get("akun", "?"), "follower": angka(r.get("follower")),
                "median": m, "views": v, "kelipatan": v / m, "hook": h,
                "format": (r.get("format") or "-").strip() or "-",
                "rumus": k, "skor": s["skor"], "kata": len(h.split()),
            })
    if not baris:
        sys.exit("Tidak ada baris valid. Cek header: akun follower median views hook")

    baris.sort(key=lambda x: -x["kelipatan"])
    akun = sorted({b["akun"] for b in baris})
    sepertiga = max(1, len(baris) // 3)
    atas, bawah = baris[:sepertiga], baris[-sepertiga:]

    out = []
    out.append(f"SWIPE  ·  {len(baris)} postingan  ·  {len(akun)} akun  ·  dasar: median akun sendiri\n")
    out.append("OUTLIER (di atas 3x)")
    for b in [x for x in baris if x["kelipatan"] >= 3]:
        nm = f"#{b['rumus']['id']} {b['rumus']['nama']}" if b["rumus"] else "tak terklasifikasi"
        out.append(f"  {b['kelipatan']:>5.1f}x  hook {b['skor']:>3}  {nm:<28} {b['akun']:<18} {int(b['views']):,} (median {int(b['median']):,})  [{b['format']}]")
        out.append(f"         \"{b['hook']}\"")
    if not any(x["kelipatan"] >= 3 for x in baris):
        out.append("  tidak ada. Sampel ini belum punya sinyal kuat.")

    def hitung(kelompok):
        c = {}
        for b in kelompok:
            key = f"#{b['rumus']['id']} {b['rumus']['nama']}" if b["rumus"] else "tak terklasifikasi"
            c[key] = c.get(key, 0) + 1
        return c

    ca, cb = hitung(atas), hitung(bawah)
    out.append("\nRUMUS DI SEPERTIGA ATAS vs BAWAH")
    for k in sorted(ca, key=lambda x: -ca[x]):
        out.append(f"  {k:<30} atas {ca[k]}  bawah {cb.get(k, 0)}")
    out.append(f"\n  median panjang hook: atas {statistics.median([b['kata'] for b in atas]):.0f} kata, bawah {statistics.median([b['kata'] for b in bawah]):.0f} kata")
    fa = {}
    for b in atas:
        fa[b["format"]] = fa.get(b["format"], 0) + 1
    out.append("  format di sepertiga atas: " + ", ".join(f"{k} {v}" for k, v in sorted(fa.items(), key=lambda x: -x[1])))

    tak = [b for b in baris if not b["rumus"]]
    out.append(f"\nTAK TERKLASIFIKASI ({len(tak)})  baca manual, bisa jadi rumus baru")
    for b in tak:
        out.append(f"  {b['kelipatan']:>5.1f}x  {b['akun']}: \"{b['hook']}\"")

    yakin = "cukup untuk klaim" if len(baris) >= 30 and len(akun) >= 5 else "belum cukup untuk klaim, anggap petunjuk"
    out.append(f"\nSAMPEL: {len(baris)} postingan dari {len(akun)} akun, {yakin}.")

    teks = "\n".join(out)
    print(teks)
    if a.out:
        p = os.path.expanduser(a.out)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write("# Swipe file Threads\n\n```\n" + teks + "\n```\n")
        print(f"\nDitulis ke {p}")


if __name__ == "__main__":
    main()
