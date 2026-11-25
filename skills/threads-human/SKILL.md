---
name: threads-human
description: >-
  Hapus jejak mesin dari draf apa pun sebelum diposting ke Threads: em dash
  dan en dash (dilarang total), karakter tak terlihat, kata klise AI bahasa
  Indonesia dan Inggris, pola struktur AI, lalu beri skor lima pemeriksaan.
  Pakai setiap kali teks harus terdengar manusia, saat user bilang
  "humanize", "kok kayak AI", "hapus em dash", "rapikan biar natural", dan
  sebelum postingan, utas, balasan, komentar, atau DM ditunjukkan ke user.
---

# threads-human

Dua alat di folder ini, keduanya benar-benar jalan. Pakai, jangan dikira-kira.

```bash
python3 humanize.py draf.txt --report            # bersihkan + tampilkan perubahan
python3 humanize.py draf.txt -o bersih.txt       # simpan hasil
python3 detect.py draf.txt                       # skor lima pemeriksaan
python3 detect.py sebelum.txt sesudah.txt        # buktikan selisihnya
```

Keduanya membaca `slop.json`: daftar kata dan frasa klise beserta gantinya,
karakter tak terlihat, tanda tipografi, dan pola struktur. File itu memang
untuk diedit. Kalau ada kata yang memang dipakai user sehari-hari, hapus dari
daftar.

## Aturan em dash: larangan total

Em dash (U+2014) dan en dash (U+2013) **tidak boleh ada sama sekali**. Tidak ada kuota,
tidak ada "satu per 100 kata". `humanize.py` mengganti semuanya dengan koma
(atau tanda hubung biasa bila di antara dua angka, misalnya 10-20), dan
`detect.py` memberi putusan GAGAL kalau masih tersisa satu saja, berapa pun
skor lainnya.

Saat menulis ulang, ganti em dash dengan koma, titik dua, tanda kurung, atau
pecah jadi dua kalimat yang sama-sama utuh. Jangan memecah jadi potongan
kalimat pendek demi drama.

## Yang diperbaiki otomatis

1. **Karakter tak terlihat**: zero-width space dan joiner, word joiner, soft
   hyphen, BOM, penanda arah teks. Keyboard tidak menghasilkan karakter ini.
   Spasi aneh (non-breaking, narrow) jadi spasi biasa.
2. **Tipografi**: kutip melengkung jadi lurus, elipsis satu karakter jadi tiga
   titik, bullet jadi tanda hubung, em/en dash dihapus.
3. **Leksikon klise**: "di era digital ini", "tidak bisa dipungkiri",
   "krusial", "signifikan", "komprehensif", "menyelami", "game changer",
   "tanpa basa-basi", "simak sampai habis", serta versi Inggrisnya (delve,
   leverage, robust, seamless, crucial). Huruf kapital dipertahankan, URL tidak
   disentuh.

## Yang hanya ditandai

Pola struktur butuh penilaian, jadi ditandai dan ditulis ulang manual:

- "bukan sekadar X, tapi Y" dan "bukan hanya X tapi juga Y"
- Pertanyaan satu kata untuk efek: "Hasilnya?", "Kenapa?", "Rahasianya?"
- Tumpukan pendek: "Tanpa X. Tanpa Y. Cuma Z." dan "Cepat. Murah. Efektif."
- Pengumuman kejujuran: "jujur aja", "real talk", "ngl", "POV:" yang bukan POV
- Pembuka basa-basi: "di utas ini saya akan"
- Pancingan refleks: "jangan lupa follow", "repost kalau setuju", "tag temen"
- Tiga kata kapital beruntun, daftar berpoin emoji
- Lebih dari satu tiga serangkai, lebih dari satu tag topik
- Dua atau lebih baris satu kata untuk drama

Tulis ulang tiap baris yang ditandai dengan mempertahankan maknanya, lalu
jalankan `detect.py` lagi. Bagian inilah yang menaikkan skor dari TINJAU ke
LOLOS, dan script tidak bisa melakukannya.

## Lima pemeriksaan

| Cek | Mengukur | Tanda mesin |
| --- | --- | --- |
| VARIASI | variasi panjang kalimat | semua kalimat sama panjang |
| KONKRET | angka, nama, nominal per 100 kata | kata benda abstrak, tanpa angka |
| SLOP | kata klise per 100 kata | kosakata stok |
| JEJAK | karakter tak terlihat, kutip melengkung, em/en dash | tipografi terlalu sempurna |
| SUARA | kamu/saya, ragam lisan, tanpa pola struktur AI | terdengar seperti rilis pers |

Skor = 60% rata-rata + 40% pemeriksaan terlemah, karena satu sinyal sudah
cukup membongkar. LOLOS butuh skor 70 ke atas dan tidak ada pemeriksaan di
bawah 55. Satu em dash = GAGAL.

## Jangan berlebihan

Hasil humanizer punya sidik jarinya sendiri. Setelah menulis ulang, baca
sekali lagi dan tanya:

- Apakah saya menambahkan kalimat pendek beruntun atau "Hasilnya?" yang baru?
- Apakah saya menambahkan pengakuan berbingkai ("jujur ya, ini berat") atau
  keraguan yang tidak ditulis user? Hapus bingkainya, sisakan faktanya.
- Apakah gaya user ikut hilang: huruf kecil di awal, "wkwk", emoji yang memang
  dipakainya? Kembalikan.

Kalau tidak yakin sebuah pola itu milik user atau milik mesin, biarkan.

## Katakan dengan jujur

Ini lima heuristik lokal yang berjalan di komputer user. Tidak memanggil
GPTZero, Originality, Turnitin, atau detektor lain, dan tidak bisa menjanjikan
hasil mereka. Pada teks sependek postingan Threads, skor detektor mana pun
tidak bisa diandalkan. Yang dijaga di sini adalah pembaca manusia yang
menggulir lewat karena tulisanmu terdengar seperti akun brand.

## Urutan kerja

1. `humanize.py draf.txt -o bersih.txt --report`
2. Tulis ulang baris yang ditandai.
3. `detect.py draf.txt bersih.txt` untuk menunjukkan sebelum dan sesudah.
4. Kalau belum LOLOS, perbaiki pemeriksaan terlemah dan ulangi. Dua putaran
   itu wajar. Lima putaran artinya drafnya ditulis dengan rumus, dan solusinya
   draf baru.
5. Tunjukkan teks bersih beserta skornya ke user. Jangan skornya saja.
