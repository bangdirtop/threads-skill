---
name: threads-balas
description: >-
  Dua mode: (1) tangani balasan di bawah postingan Threads milik user, disortir
  dulu mana yang layak dijawab; (2) tulis balasan di postingan orang lain yang
  terdengar seperti orang dengan pendapat, bukan bot. Pakai saat user menempel
  balasan di postingannya, bilang "balas ini", "urus kolom balasan", "ada yang
  nyinyir", "komen di postingan ini", "ronde engage", atau minta sekumpulan
  balasan untuk akun-akun di daftar engage.
---

# threads-balas

Di Threads, percakapan adalah bahan bakar. Balasan di jam pertama, balasan
balik dari pembuat postingan, dan quote membuat postingan terus diedarkan.
Balasan di postingan orang besar bisa dilihat lebih banyak orang daripada
postingan user sendiri.

Tapi nilai tiap balasan tidak sama, jadi skill ini menyortir sebelum menulis.

## Mode 1: kolom balasan postingan sendiri

User menempel balasan beserta handle-nya. Screenshot boleh. Jangan scraping.

### Sortir dulu

Masukkan tiap balasan ke satu dari enam kelompok dan sebutkan jumlahnya:

| kelompok | isinya | dapat apa |
| --- | --- | --- |
| **KATA KUNCI** | kata yang diminta user untuk diketik | barang yang dijanjikan, dikirim manual atau lewat alat resmi |
| **CALON PEMBELI** | orang yang menceritakan masalah yang user selesaikan | jawaban sungguhan di depan umum, lalu satu pintu |
| **ISI** | menambah data, membantah, memperluas | balasan terpanjang di utas |
| **PERTANYAAN** | pertanyaan yang juga dimiliki banyak orang | jadi postingan baru, bukan cuma balasan |
| **DUKUNGAN** | "mantap", emoji, tag teman | suka, dan 3 sampai 8 kata paling banyak |
| **KEBISINGAN** | jualan, spam, niat buruk, pancingan | tidak dibalas, atau satu baris lalu selesai |

Tulis dalam urutan itu dan berhenti saat nilainya habis.

### Langkah yang paling sering terlewat

Kalau satu pertanyaan di kolom balasan juga dimiliki puluhan orang, **jawab
dengan postingan baru** yang mengutip (quote) balasan itu. Penanyanya mendapat
notifikasi, dan pertanyaan dengan permintaan nyata jadi postingan dengan hook
yang sudah tertulis. Serahkan ke threads-post sebagai rumus #16.

### Cara membalas

- **Jawab pertanyaannya.** Kalau ditanya caranya, beri caranya di balasan.
  Jangan suruh DM untuk jawaban yang bisa diberikan di sini.
- **Sebut namanya sekali** di awal, tanpa tanda seru.
- **Samakan panjangnya.** Komentar empat kata tidak dibalas empat baris.
- **Ke pengkritik:** akui bagian yang benar dengan kata-katanya, lalu pegang
  posisi. Jangan hapus, jangan defensif, jangan membalas dua kali di utas yang
  sama.
- **Ke pembenci:** tidak dibalas. Balasan adalah jangkauan, dan itu yang mereka
  cari. Sembunyikan atau batasi kalau kasar. Memakai kontrol balasan bukan
  kalah.
- **Ke calon pembeli:** jawab penuh di depan umum. Pintunya satu kalimat di
  akhir, berupa tawaran bantuan, bukan jualan.

## Mode 2: membalas postingan orang lain

User menempel teks postingan dan nama akunnya. Jangan buka feed dengan alat
browser untuk mencari sendiri, dan jangan memposting apa pun.

### Sembilan jenis balasan

Pilih berdasarkan isi postingannya. Jangan selalu jenis 1.

| # | jenis | kapan | bentuk |
| --- | --- | --- | --- |
| 1 | **Tambah data** | postingan membuat klaim yang bisa didukung angka | "Sama di kami: 40% dari..." |
| 2 | **Kasus yang hilang** | benar tapi belum lengkap | "Ini berlaku sampai {kondisi}." |
| 3 | **Bantah dengan hormat** | kamu benar-benar menganggapnya salah | sebut yang disetujui, lalu bedanya |
| 4 | **Perpanjang satu baris** | ada satu kalimat terbaik | kutip, lalu bangun di atasnya |
| 5 | **Tanya yang sebenarnya** | postingan melewatkan bagian sulit | satu pertanyaan, spesifik |
| 6 | **Bukti pengalaman** | kamu pernah melakukan hal itu | apa yang terjadi, dua kalimat |
| 7 | **Koreksi** | ada fakta yang salah | benar, singkat, sopan, yakin |
| 8 | **Bingkai lain** | fakta benar, bingkai salah | "Cara lain membacanya:" |
| 9 | **Satu baris** | postingan tidak butuh tambahan | di bawah 10 kata, harus lucu atau benar |

### Aturan

- **Satu sampai tiga kalimat.**
- **Jangan buka dengan** "Mantap", "Setuju banget", "Keren", "Ini sih",
  "Daging", atau nama pembuat postingan dengan tanda seru.
- **Jangan balasan emoji saja**, jangan emoji di karakter pertama.
- **Jangan ulangi isi postingan.** Semua orang baru membacanya.
- **Satu gagasan.**
- **Katakan hal spesifik.** Kalau balasannya bisa ditempel di postingan mana
  pun dengan topik sama, itu kebisingan.
- **Jangan pernah jualan.** Bukan produk, bukan link, bukan "cek profil saya".
- **Lebih awal lebih baik.** Balasan di jam pertama ikut terbawa saat
  postingannya menyebar.
- **Quote** dipakai saat kamu punya tambahan yang layak jadi postingan sendiri.
  Kalau cuma setuju, balas biasa saja.

## Keluaran

Mode 1: satu blok dikelompokkan per kelompok, tiap balasan siap salin dan
sudah lewat threads-human.

Mode 2: **dua pilihan dari jenis berbeda**, diberi label, plus satu baris
tentang mana yang akan kamu kirim dan kenapa.

```
PILIHAN BALASAN  (di postingan @akun tentang harga jasa)

[6 · Bukti pengalaman]
Kami naikkan harga 40% Maret lalu dan cuma kehilangan satu klien, yang memang
paling banyak minta revisi.

[3 · Bantah dengan hormat]
Setuju soal patokan harga. Yang saya ragukan bagian menaikkan di tengah
proyek. Kami pernah, dan itu bikin satu perpanjangan kontrak batal.

Kirim yang pertama. Ada angkanya dan ada yang dikorbankan.
```

Mode batch untuk ronde engage: minta 5 sampai 10 postingan sekaligus, beri
satu balasan per postingan, dan catat di `~/.claude/threads/log.md` siapa saja
yang sudah dibalas minggu ini. Membalas tiga akun yang sama setiap hari itu
terlihat.

## Jangan pernah

Jangan memposting otomatis, jangan mengotomatiskan balasan ke postingan orang
lain, dan jangan memakai alat browser untuk memposting atas nama user.
Interaksi otomatis melanggar ketentuan Meta dan membuat akun dibatasi. Balasan
otomatis untuk kata kunci di postingan sendiri hanya boleh lewat alat resmi
atau mitra yang disetujui, dan isinya harus diuji dulu: balasan bot yang salah
(misalnya teks kosong) tidak bisa ditarik setelah terkirim.
