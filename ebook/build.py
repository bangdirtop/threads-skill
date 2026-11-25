#!/usr/bin/env python3
"""
build.py - gabungkan PANDUAN.md dan CONTOH.md jadi satu ebook PDF.

Pemakaian (dari folder repo):
    pip install markdown pypdf
    python3 ebook/build.py

Hasil: ebook/threads-skill-panduan.pdf (dan ebook/threads-skill-panduan.html)
Butuh Google Chrome atau Chromium versi 131 ke atas (untuk nomor halaman).
"""
import html
import os
import re
import shutil
import subprocess
import sys

import markdown
from markdown.extensions.toc import slugify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "ebook")
HTML_OUT = os.path.join(OUT_DIR, "threads-skill-panduan.html")
PDF_OUT = os.path.join(OUT_DIR, "threads-skill-panduan.pdf")
VERSI = "1.0"
TANGGAL = "November 2026"

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
]

IKON = {"💡": "tips", "📌": "ingat", "⚠️": "awas", "🤓": "teknis"}


def baca(nama):
    with open(os.path.join(ROOT, nama), encoding="utf-8") as f:
        return f.read()


def buang_daftar_isi(md):
    """Daftar isi bawaan markdown diganti daftar isi gabungan di depan ebook."""
    return re.sub(r"(?ms)^## Daftar Isi\n.*?(?=^---\s*$)", "", md, count=1)


def rapikan_link(md):
    md = re.sub(r"\]\((?:PANDUAN|CONTOH)\.md#([^)]+)\)", r"](#\1)", md)
    md = md.replace("](CONTOH.md)", "](#buku-contoh)").replace("](PANDUAN.md)", "](#buku-panduan)")
    return md


def jarak_daftar(md):
    """Python-Markdown butuh baris kosong sebelum daftar. GitHub tidak, jadi ditambahkan di sini."""
    keluar, di_kode, sebelum = [], False, ""
    for baris in md.split("\n"):
        if baris.startswith("```"):
            di_kode = not di_kode
        adalah_daftar = bool(re.match(r"^(\s*)(- |\d+\. )", baris))
        sebelum_daftar = bool(re.match(r"^(\s*)(- |\d+\. )", sebelum)) or sebelum.startswith("  ")
        if not di_kode and adalah_daftar and sebelum.strip() and not sebelum_daftar:
            keluar.append("")
        keluar.append(baris)
        sebelum = baris
    return "\n".join(keluar)


def jadi_html(md):
    return markdown.markdown(
        md,
        extensions=["tables", "fenced_code", "toc", "sane_lists", "attr_list"],
        extension_configs={"toc": {"permalink": False}},
    )


def kotak_ikon(h):
    """Blockquote yang diawali ikon jadi kotak berwarna."""
    def ganti(m):
        isi = m.group(1)
        polos = re.sub(r"<[^>]+>", "", isi).strip()
        for emoji, kelas in IKON.items():
            if polos.startswith(emoji):
                return f'<aside class="kotak {kelas}">{isi}</aside>'
        return f"<blockquote>{isi}</blockquote>"
    return re.sub(r"(?s)<blockquote>(.*?)</blockquote>", ganti, h)


def ikat_pengantar(h):
    """Kalimat pengantar yang diakhiri titik dua tetap satu halaman dengan blok sesudahnya."""
    def ganti(m):
        teks = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if not teks.endswith(":"):
            return m.group(0)
        return f'<div class="ikat">{m.group(1)}{m.group(2)}</div>'
    return re.sub(r"(?s)(<p>(?:(?!</p>).)*</p>)\s*(<pre>.*?</pre>|<table>.*?</table>)", ganti, h)


def pisah_bab(h):
    # h1 = Bagian (halaman pembuka), h2 = bab (halaman baru)
    h = re.sub(r"<h1 id=\"([^\"]+)\">(Bagian [^<]+)</h1>",
               lambda m: f'<section class="bagian" id="{m.group(1)}"><div class="bagian-isi">'
                         f'<span class="bagian-label">{m.group(2).split(":")[0]}</span>'
                         f'<h1>{m.group(2).split(":", 1)[1].strip()}</h1></div></section>', h)
    h = re.sub(r"<h1 id=\"([^\"]+)\">(Lampiran)</h1>",
               r'<section class="bagian" id="\1"><div class="bagian-isi"><span class="bagian-label">Penutup</span><h1>\2</h1></div></section>', h)
    return h


def daftar_isi(md_panduan, md_contoh):
    baris = []
    baris.append('<li class="toc-buku"><a href="#buku-panduan">Buku 1 · Panduan</a></li>')
    for lvl, judul in re.findall(r"(?m)^(#{1,2}) (.+)$", md_panduan):
        if judul.startswith(("threads-skill Buat", "Daftar Isi", "Buku")):
            continue
        slug = slugify(judul, "-")
        kelas = "toc-bagian" if lvl == "#" else "toc-bab"
        if lvl == "##" and not judul.startswith(("Bab", "Lampiran", "Pengantar")):
            continue
        baris.append(f'<li class="{kelas}"><a href="#{slug}">{html.escape(judul)}</a></li>')
    baris.append('<li class="toc-buku"><a href="#buku-contoh">Buku 2 · Contoh dan Studi Kasus</a></li>')
    for judul in re.findall(r"(?m)^## (\d+\. .+)$", md_contoh):
        slug = slugify(judul, "-")
        baris.append(f'<li class="toc-bab"><a href="#{slug}">{html.escape(judul)}</a></li>')
    return "<ol class=\"toc\">" + "\n".join(baris) + "</ol>"


CSS = r"""
@page {
  size: 148mm 210mm;
  margin: 16mm 14mm 18mm 14mm;
  @bottom-center { content: counter(page); font: 600 8pt Poppins, sans-serif; color: #6b7a8f; }
  @top-right { content: "threads-skill"; font: 500 7pt Poppins, sans-serif; color: #a3b0c0; }
}
@page cover { margin: 0; @bottom-center { content: none; } @top-right { content: none; } }
@page polos { @bottom-center { content: none; } @top-right { content: none; } }
:root {
  --navy: #14233c; --sage: #4f6f5c; --sage-muda: #e6efe8; --kuning: #f2b33d;
  --kuning-muda: #fdf3dc; --merah: #c2463a; --merah-muda: #fbe6e3;
  --ungu-muda: #ecebf7; --ungu: #5b55a3; --abu: #6b7a8f; --garis: #d9dee6; --kertas: #fffdf8;
}
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 9.6pt;
  line-height: 1.55; color: #1d2633; margin: 0; hyphens: auto; }
h1, h2, h3, h4 { hyphens: manual; font-family: Poppins, "Helvetica Neue", sans-serif; color: var(--navy);
  line-height: 1.25; break-after: avoid; }
h1 { font-size: 20pt; font-weight: 800; margin: 0 0 8pt; }
h2 { font-size: 14.5pt; font-weight: 700; margin: 0 0 8pt; padding-bottom: 5pt;
  border-bottom: 2.5pt solid var(--kuning); break-before: page; }
h3 { font-size: 11pt; font-weight: 700; margin: 14pt 0 5pt; color: var(--sage); }
p { margin: 0 0 7pt; orphans: 3; widows: 3; }
.ikat { break-inside: avoid; }
a { color: var(--sage); text-decoration: none; }
strong { color: var(--navy); }
ul, ol { padding-left: 15pt; margin: 0 0 8pt; }
li { margin-bottom: 2.5pt; }
hr { display: none; }
code { font-family: Menlo, "SF Mono", monospace; font-size: 8pt; background: #eef1f5;
  padding: 0.5pt 3pt; border-radius: 3pt; color: #1d2633; }
pre { background: var(--navy); color: #f4f1e8; border-radius: 6pt; padding: 7pt 7pt;
  margin: 0 0 9pt; white-space: pre-wrap; word-break: break-word; break-inside: avoid;
  border-left: 3pt solid var(--kuning); }
pre code { background: none; color: inherit; padding: 0; font-size: 6.9pt; line-height: 1.5; }
table { width: 100%; border-collapse: collapse; margin: 0 0 10pt; font-size: 8pt;
  break-inside: auto; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
th { background: var(--navy); color: #fff; font-family: Poppins, sans-serif; font-weight: 600;
  text-align: left; padding: 4pt 5pt; font-size: 7.8pt; }
td { padding: 4pt 5pt; border-bottom: 0.6pt solid var(--garis); vertical-align: top; }
tr:nth-child(even) td { background: #f6f8fa; }
td code { font-size: 7.2pt; }
.kotak { border-radius: 6pt; padding: 7pt 9pt 2pt 9pt; margin: 0 0 9pt; break-inside: avoid;
  border-left: 4pt solid; font-size: 9pt; }
.kotak p { margin-bottom: 5pt; }
.kotak.tips { background: var(--kuning-muda); border-color: var(--kuning); }
.kotak.ingat { background: var(--sage-muda); border-color: var(--sage); }
.kotak.awas { background: var(--merah-muda); border-color: var(--merah); }
.kotak.teknis { background: var(--ungu-muda); border-color: var(--ungu); }
blockquote { margin: 0 0 9pt; padding: 6pt 9pt; border-left: 3pt solid var(--garis); color: var(--abu); }
/* sampul */
.sampul { page: cover; height: 210mm; width: 148mm; background: var(--navy); color: #fff;
  position: relative; overflow: hidden; break-after: page; }
.sampul .pita { position: absolute; left: 0; right: 0; top: 0; height: 9mm; background: var(--kuning); }
.sampul .bulat { position: absolute; right: -38mm; bottom: -30mm; width: 120mm; height: 120mm;
  border-radius: 50%; background: var(--sage); opacity: .55; }
.sampul .bulat2 { position: absolute; right: 18mm; bottom: 38mm; width: 34mm; height: 34mm;
  border-radius: 50%; border: 3pt solid var(--kuning); }
.sampul .isi { position: absolute; left: 14mm; right: 14mm; top: 30mm; }
.sampul .label { font: 700 8pt Poppins, sans-serif; letter-spacing: 2pt; color: var(--kuning);
  text-transform: uppercase; }
.sampul h1 { color: #fff; font-size: 30pt; line-height: 1.08; margin: 6mm 0 5mm; }
.sampul h1 span { color: var(--kuning); }
.sampul .sub { font: 500 11pt/1.45 Poppins, sans-serif; color: #dbe3ee; max-width: 105mm; }
.sampul .daftar { margin-top: 9mm; font: 500 8.5pt/1.9 Poppins, sans-serif; color: #fff; }
.sampul .daftar b { color: var(--kuning); }
.sampul .kaki { position: absolute; left: 14mm; bottom: 13mm; font: 500 7.5pt Poppins, sans-serif;
  color: #c6d1de; }
.sampul .kaki b { color: #fff; }
/* halaman bagian */
.bagian { break-before: page; break-after: page; page: polos; height: 170mm; display: flex;
  align-items: center; }
.bagian-isi { border-left: 5pt solid var(--kuning); padding-left: 10pt; }
.bagian-label { font: 700 9pt Poppins, sans-serif; letter-spacing: 2pt; color: var(--sage);
  text-transform: uppercase; }
.bagian h1 { font-size: 24pt; margin-top: 4pt; }
/* pembuka buku */
.pembuka-buku { break-before: page; page: polos; height: 170mm; display: flex; flex-direction: column;
  justify-content: center; }
.pembuka-buku .nomor { font: 800 60pt Poppins, sans-serif; color: var(--kuning); line-height: 1; }
.pembuka-buku h1 { font-size: 24pt; margin-top: 6pt; }
.pembuka-buku p { color: var(--abu); font-size: 10pt; max-width: 100mm; }
/* daftar isi */
.halaman-toc { break-before: page; }
.halaman-toc h2 { break-before: avoid; }
.toc { list-style: none; padding: 0; margin: 0; font-size: 8.6pt; }
.toc li { margin: 0; padding: 2pt 0; border-bottom: 0.5pt dotted var(--garis); }
.toc li.toc-buku { font: 700 10pt Poppins, sans-serif; border: none; margin-top: 9pt; color: var(--navy); }
.toc li.toc-buku a { color: var(--navy); }
.toc li.toc-bagian { font: 600 8.8pt Poppins, sans-serif; margin-top: 5pt; border: none; }
.toc li.toc-bagian a { color: var(--sage); }
.toc li.toc-bab { padding-left: 10pt; }
.toc li.toc-bab a { color: #1d2633; }
.judul-buku-md { display: none; }
.kolofon { break-before: page; page: polos; font-size: 8.5pt; color: var(--abu); }
.kolofon h2 { break-before: avoid; border: none; font-size: 12pt; }
"""


def main():
    panduan = baca("PANDUAN.md")
    contoh = baca("CONTOH.md")
    toc_html = daftar_isi(panduan, contoh)

    panduan = jarak_daftar(buang_daftar_isi(rapikan_link(panduan)))
    contoh = jarak_daftar(buang_daftar_isi(rapikan_link(contoh)))
    panduan = re.sub(r"(?m)^\*Selamat posting\.[^\n]*\*\s*$", "", panduan)
    # judul markdown teratas diganti halaman pembuka buku
    panduan = re.sub(r"(?s)^# threads-skill Buat yang Nggak Mau Ribet\n+### [^\n]+\n", "", panduan)
    contoh = re.sub(r"(?s)^# Buku Contoh threads-skill\n+### [^\n]+\n", "", contoh)

    h_panduan = pisah_bab(ikat_pengantar(kotak_ikon(jadi_html(panduan))))
    h_contoh = ikat_pengantar(kotak_ikon(jadi_html(contoh)))

    sampul = f"""
<section class="sampul">
  <div class="pita"></div><div class="bulat"></div><div class="bulat2"></div>
  <div class="isi">
    <div class="label">Ebook panduan · versi {VERSI}</div>
    <h1>threads-skill<br><span>Buat yang Nggak Mau Ribet</span></h1>
    <div class="sub">Panduan santai memakai 12 skill Claude untuk menulis, mengukur, dan mengatur konten Threads.</div>
    <div class="daftar">
      <b>Buku 1</b> &nbsp;Panduan: 17 bab + lampiran<br>
      <b>Buku 2</b> &nbsp;Contoh: pola, 96 perintah siap salin, 12 studi kasus
    </div>
  </div>
  <div class="kaki"><b>github.com/bangdirtop/threads-skill</b><br>{TANGGAL} · Lisensi MIT</div>
</section>"""

    halaman_toc = f'<section class="halaman-toc"><h2 id="daftar-isi">Daftar Isi</h2>{toc_html}</section>'

    pembuka1 = """<section class="pembuka-buku" id="buku-panduan"><div class="nomor">01</div>
<h1>Panduan</h1><p>Dari pasang sampai ngukur hasil. Nggak perlu dibaca urut, lompat aja ke bab yang kamu butuhkan.</p></section>"""
    pembuka2 = """<section class="pembuka-buku" id="buku-contoh"><div class="nomor">02</div>
<h1>Contoh dan Studi Kasus</h1><p>Pola perintah, 8 contoh siap salin, dan satu studi kasus utuh untuk tiap skill.</p></section>"""

    kolofon = f"""<section class="kolofon"><h2>Tentang ebook ini</h2>
<p>Ebook ini dibuat otomatis dari <code>PANDUAN.md</code> dan <code>CONTOH.md</code> di repo
github.com/bangdirtop/threads-skill dengan <code>ebook/build.py</code>. Kalau panduannya diperbarui,
jalankan script itu lagi.</p>
<p>Tokoh dan angka di studi kasus adalah rekaan. Skor hook, skor humanizer, dan hasil linter
dihitung dengan script di repo yang sama.</p>
<p>Lisensi MIT. Sebagian struktur diadaptasi dari instagram-skills oleh Serge Bulaev (MIT).</p>
<p><b>Selamat posting. Ingat: baris pertama dulu, sisanya belakangan.</b></p>
<p>{TANGGAL} · versi {VERSI}</p></section>"""

    doc = f"""<!doctype html><html lang="id"><head><meta charset="utf-8">
<title>threads-skill Buat yang Nggak Mau Ribet</title><style>{CSS}</style></head><body>
{sampul}{halaman_toc}{pembuka1}{h_panduan}{pembuka2}{h_contoh}{kolofon}</body></html>"""

    for ch in "\u2013\u2014\u2015":
        if ch in doc:
            sys.exit(f"Ada em/en dash ({ch!r}) di naskah. Bersihkan dulu, ebook ini bebas em dash.")

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(doc)

    chrome = next((c for c in CHROME_CANDIDATES if c and os.path.exists(c)), None)
    if not chrome:
        sys.exit(f"Chrome tidak ditemukan. HTML sudah ditulis ke {HTML_OUT}, cetak manual ke PDF.")
    if os.path.exists(PDF_OUT):
        os.remove(PDF_OUT)
    # Chrome di macOS kadang keluar dengan kode bukan nol walaupun PDF berhasil ditulis,
    # jadi yang dicek adalah file hasilnya.
    subprocess.run([
        chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
        "--generate-pdf-document-outline", f"--print-to-pdf={PDF_OUT}",
        "file://" + HTML_OUT,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not os.path.exists(PDF_OUT) or os.path.getsize(PDF_OUT) == 0:
        sys.exit("Chrome gagal membuat PDF.")

    try:
        from pypdf import PdfReader, PdfWriter
        r = PdfReader(PDF_OUT)
        w = PdfWriter(clone_from=r)
        w.add_metadata({"/Title": "threads-skill Buat yang Nggak Mau Ribet",
                        "/Author": "bangdirtop", "/Subject": "Panduan 12 skill Claude untuk Threads"})
        with open(PDF_OUT, "wb") as f:
            w.write(f)
        print(f"PDF: {PDF_OUT} ({len(r.pages)} halaman)")
    except ImportError:
        print(f"PDF: {PDF_OUT}")


if __name__ == "__main__":
    main()
