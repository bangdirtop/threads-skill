---
name: threads-album
description: >-
  Rancang album Threads (postingan dengan beberapa foto atau video yang
  digeser): teks pengantar, urutan dan isi tiap slide, slide bukti, slide
  ringkasan, serta file gambar 1080x1350. Juga mencakup video pendek di
  Threads. Pakai saat user bilang "album", "carousel Threads", "slide",
  "postingan bukti", "screenshot insight", "sebelum sesudah", "video buat
  Threads", atau punya ide berbentuk daftar atau langkah yang mati kalau cuma
  teks.
---

# threads-album

Album di Threads adalah tempat bukti. Teks di atasnya membuat orang berhenti,
gambar di bawahnya membuat orang percaya dan me-repost. Untuk akun yang
menjual keahlian, album berisi bukti (screenshot, angka, sebelum dan sesudah)
sering menjadi format yang paling jauh menyebar ke luar follower.

## Kapan album

- Ada **bukti visual**: screenshot insight, hasil kerja, perbandingan.
- Ada **urutan** yang perlu dilihat: langkah, kerangka, sebelum dan sesudah.
- Ada **sesuatu untuk diambil**: prompt, template, daftar yang layak disimpan.

Kalau idenya satu klaim tanpa bukti visual, pakai threads-post. Kalau isinya
argumen teks panjang, pakai threads-utas.

## Bentuk

```
Teks        postingan pengantar, aturan threads-post berlaku penuh:
            baris pertama hook, maksimal 500 karakter, satu ajakan.
Slide 1     SAMPUL. Janji dalam 6 kata atau kurang, terbaca di layar HP.
Slide 2     BUKTI TERKUAT. Taruh yang paling meyakinkan di depan, karena
            makin jauh slide makin sedikit yang melihat.
Slide 3..   SATU HAL PER SLIDE. Judul 3 sampai 7 kata, paling banyak 25 kata
            di bawahnya. Lebih dari itu, jadikan dua slide.
Slide N-1   RINGKASAN. Semuanya dalam satu daftar. Ini slide yang di-screenshot
            dan dikirim orang.
Slide N     AJAKAN. Satu. Repost, simpan, atau balas dengan kata tertentu.
```

Panjang kerja 4 sampai 10 slide. Threads menerima hingga 20 item per album
(cek di aplikasi, batasnya bisa berubah), tapi 20 hampir tidak pernah
selesai digeser.

## Aturan slide

- **Sampul menentukan 80% hasil.** Enam kata, huruf besar, kontras tinggi.
- **Screenshot asli lebih kuat dari desain ulang.** Kalau buktinya insight,
  pakai screenshot insight-nya. Sensor data pribadi orang lain.
- **Beri nomor slide** (3/8). Orang lebih mau menyelesaikan kalau ujungnya
  terlihat.
- **Handle kecil di pojok tiap slide.** Screenshot beredar tanpa kamu.
- **Teks alternatif** untuk sampul paling tidak.
- **Jangan dinding teks di gambar.** Kalau tidak terbaca dalam 2 detik di HP,
  pecah.

## Video di Threads

Threads menerima video (hingga 5 menit, cek di aplikasi). Video berjalan
otomatis tanpa suara di feed, jadi:

- **Bingkai pertama harus bergerak dan berteks.** Kartu hook muncul di detik 0,
  enam kata atau kurang.
- **Teks terbakar di video** untuk isi yang diucapkan. Kebanyakan orang menonton
  tanpa suara dulu.
- **15 sampai 45 detik** adalah rentang kerja. Satu ide per video.
- **Teks postingan di atas video** tidak mengulang hook video. Tugasnya memberi
  konteks dan satu ajakan (Job A). Kalau video tanpa hook, teks yang jadi hook
  (Job B).
- Video yang dibuat untuk Reels atau Shorts boleh dipakai ulang, tapi tulis
  teks pengantarnya baru untuk Threads.

## Membuat file

Ukuran 1080x1350 (4:5), JPG atau PNG. Buat sebagai HTML, satu `<section>` per
slide dengan `width:1080px; height:1350px`, lalu cetak ke gambar dengan alat
yang sudah ada di proyek user (Chrome headless, Playwright, atau sejenisnya).
Huruf paling kecil 32px. Satu warna aksen. Kalau proyek punya skill merek atau
sistem desain, pakai itu, jangan mengarang palet.

## Alur kerja

1. Teks slide dulu, sebagai daftar bernomor yang bisa dibaca user dalam 10
   detik dan diedit sebelum apa pun dirender.
2. Teks pengantar lewat threads-post (hook diskor, lint_post.py).
3. Jalankan threads-human pada teks slide dan teks pengantar.
4. Render file hanya setelah user menyetujui teksnya.

```
ALBUM  ·  7 slide
1  SAMPUL   {{N}} HARI, {{N}} FOLLOWER
2  BUKTI    screenshot insight hari terakhir
3           Hari 1: {{view hari 1}}
...
6  RINGKAS  Semua angka dalam satu tabel
7  AJAKAN   Repost kalau kamu juga mulai dari nol.

Teks pengantar: hook #6 Bukti Angka, 288/500, satu ajakan, linter SIAP.
```

User yang mengunggah. Tidak ada yang diposting oleh skill ini.
