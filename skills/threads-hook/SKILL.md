---
name: threads-hook
description: >-
  Perpustakaan 26 rumus baris pertama untuk Threads, alat skor hook
  (hookscore.py), dan cara membongkar postingan orang lain untuk diambil
  bentuknya. Pakai saat user minta "hook", "baris pertama", "opening", "kasih
  ide pembuka", "kenapa postingan ini rame", "bongkar postingan ini", "ambil
  polanya", atau menempel postingan Threads orang lain untuk dipelajari.
---

# threads-hook

Dua alat di folder ini:

```bash
python3 hookscore.py kandidat.txt          # urutkan beberapa kandidat (satu per baris)
python3 hookscore.py --hook "satu baris"   # nilai satu baris
```

`hooks.json` berisi 26 rumus. Tiap rumus punya pola, contoh, tujuan utama,
pola deteksi, dan cara rumus itu biasanya rusak. Baca bagian "rusak_jika"
sebelum memakai rumusnya.

## Mode 1: menulis hook

1. Ambil satu hal spesifik dari user: kejadian, angka, biaya.
2. Pilih tiga rumus berbeda yang benar-benar cocok. Bukan tiga variasi dari
   satu rumus.
3. Tulis ketiganya, jalankan `hookscore.py`, tunjukkan peringkatnya.
4. Skor di bawah 50 artinya hook belum ketemu. Jangan dipoles, ganti rumus
   atau minta bahan yang lebih spesifik.

Batas alat ini harus disampaikan jujur: skor menyaring baris yang lemah
(sapaan, basa-basi, tanpa isi konkret, isi penting di ujung). Skor tidak
memprediksi mana dari dua hook bagus yang akan lebih ramai. Untuk itu, data
akun user sendiri lewat threads-audit lebih bisa dipercaya.

## Mode 2: membongkar postingan orang lain

User menempel teks postingan (dan deskripsi album atau videonya bila ada).
Kalau user hanya memberi URL dan sesi ini tidak punya alat baca Threads,
minta user menempel teksnya.

Keluarkan:

- **Rumus** dari 26 rumus, dengan tingkat keyakinan. Kalau dua rumus cocok,
  sebut keduanya. Kalau tidak ada yang cocok, katakan itu, karena bisa jadi
  rumus baru yang layak ditambahkan ke `hooks.json`.
- **Bentuk**: teks saja, teks + gambar, album, video, utas, polling.
- **Bedah struktur**: baris pertama, isi, penutup (apa yang memancing repost,
  simpan, atau balasan), dan perangkat pemicu (angka, nama, celah rasa ingin
  tahu).
- **Tujuan utama** yang dikejar postingan itu.
- **Kenapa berhasil**, satu sampai tiga kalimat.
- **Templat kosong** dengan `{slot}` yang mengikuti bentuk aslinya, siap diisi
  cerita user sendiri.
- **Peringatan**: hal di postingan itu yang jangan ditiru (em dash, kata klise
  AI, pancingan refleks, banyak tag).

Ambil rumusnya, jangan pernah tirunya. Bentuk hook, struktur, panjang boleh
diambil. Kalimat, suara, dan ceritanya milik orang itu.

## Aturan hook di Threads

- Baris pertama di bawah 120 karakter, idealnya 5 sampai 14 kata.
- Angka ganjil lebih dipercaya daripada angka bulat: Rp 4.217.000 lawan
  Rp 4 juta.
- Isi penting di depan. "Rp 4,2 juta habis" lebih kuat daripada "Akhirnya saya
  sadar setelah kehilangan Rp 4,2 juta".
- Bicara ke satu orang: kamu, bukan kalian semua.
- Tanpa sapaan, tanpa "di thread ini", tanpa emoji di karakter pertama, tanpa
  em dash.
