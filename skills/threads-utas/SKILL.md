---
name: threads-utas
description: >-
  Tulis utas Threads (beberapa postingan bersambung, tiap postingan maksimal
  500 karakter): postingan pertama yang berdiri sendiri, satu gagasan per
  postingan, penutup dengan satu ajakan, dicek per postingan dengan
  lint_post.py. Pakai saat user bilang "bikin utas", "thread panjang",
  "rangkaian postingan", "breakdown jadi beberapa post", atau idenya tidak
  muat di 500 karakter tapi lebih cocok dibaca daripada dilihat.
---

# threads-utas

Utas dibaca dari atas, dan kebanyakan orang hanya membaca postingan pertama.
Jadi postingan pertama harus bernilai walaupun orang berhenti di sana, dan
setiap postingan berikutnya harus memberi alasan untuk lanjut.

## Kapan utas, kapan bukan

- **Utas**: urutan langkah, cerita dengan beberapa babak, argumen yang butuh
  bukti bertahap. Isinya teks.
- **Album** (threads-album): kalau buktinya visual (screenshot, sebelum dan
  sesudah, angka di grafik). Di banyak akun, album bukti menyebar lebih jauh
  daripada utas teks.
- **Satu postingan** (threads-post): kalau idenya satu klaim. Jangan dipanjangkan.

## Bentuk

```
1          HOOK      klaim + janji. Berdiri sendiri. Tanpa "utas 🧵", tanpa
                     "1/7" di depan kalimat pertama.
2          TARUHAN   kenapa ini penting buat pembaca. Satu sampai dua kalimat.
3 ... N-1  ISI       satu gagasan per postingan. Tiap postingan bisa di-quote
                     sendirian tanpa konteks.
N          PENUTUP   ringkasan satu kalimat + satu ajakan. Link, kalau ada,
                     di sini.
```

Panjang kerja 4 sampai 8 postingan. Di atas 10, pertimbangkan album atau
lampiran teks panjang kalau fitur itu tersedia di akun user.

## Aturan

- **Postingan pertama bernilai sendirian.** Tes: kalau hanya postingan 1 yang
  dibaca, apakah orang tetap dapat sesuatu? Kalau tidak, tulis ulang.
- **Jangan "utas di bawah 👇" sebagai isi.** Itu bukan hook, itu petunjuk arah.
- **Penomoran boleh di akhir postingan** (misalnya "(3/6)") kalau user suka,
  tapi jangan pernah membuka kalimat pertama dengan nomor.
- **Satu tag topik**, di postingan pertama atau terakhir, bukan di semua.
- **Setiap postingan di bawah 500 karakter.** Lebih pendek lebih baik.
- **Postingan tengah yang kuat bisa di-quote orang.** Tulis paling tidak satu
  kalimat di tengah utas yang layak di-screenshot.

## Alur kerja

1. Tulis hook lewat threads-hook (tiga kandidat, skor, pilih).
2. Susun kerangka: daftar satu baris per postingan. Tunjukkan ke user dulu.
3. Setelah disetujui, tulis semuanya di satu file, pisahkan dengan baris `---`.
4. Jalankan threads-human pada seluruh file.
5. Jalankan `python3 ../threads-post/lint_post.py utas.txt`. Linter memeriksa
   tiap postingan terhadap batas 500 karakter, em dash, tag topik, dan link di
   postingan pertama.
6. Cetak utas siap salin per postingan, lalu ringkasan:

```
UTAS SIAP  ·  6 postingan
hook:       #15 Catatan Gagal, skor 81 KUAT
terpanjang: postingan 4, 462/500
ajakan:     satu, di postingan 6
link:       postingan 6
linter:     SIAP
```

User yang memposting. Catat ke `~/.claude/threads/log.md` kalau user setuju.
