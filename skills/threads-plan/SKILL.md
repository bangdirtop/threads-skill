---
name: threads-plan
description: >-
  Susun minggu di Threads: apa yang diposting, format apa (teks, album, utas,
  video, polling), jam berapa, rumus hook mana, dan daftar 10 akun untuk
  dibalas tiap hari. Pakai saat user bilang "rencana minggu ini", "posting
  apa", "kalender konten Threads", "nggak ada ide", atau ingin jadwal posting
  dan daftar engage.
---

# threads-plan

Ruang kendali. Skill lain mengeksekusi, skill ini memutuskan apa yang
dieksekusi. Jalankan seminggu sekali di hari yang sama.

## Masukan

Baca `~/.claude/threads/voice.md`, `swipe.md`, dan `log.md` kalau ada. Swipe
file adalah bukti user sendiri tentang rumus yang sedang jalan dan mengalahkan
aturan di file ini. Log mencegah tema yang sama diulang dalam dua minggu.
Kalau ada hasil threads-audit, itu dasar paling kuat.

Kalau belum ada, tanyakan empat hal sekaligus lalu catat:

1. Apa yang user jual, dan ke siapa.
2. Tiga atau empat tema yang ingin dikenal darinya.
3. Apa yang benar-benar terjadi minggu ini: obrolan klien, angka, kesalahan,
   sesuatu yang dibuat, perdebatan. Dari sinilah postingan lahir.
4. Sepuluh akun yang layak didatangi.

## Apa yang diposting

Empat sampai tujuh postingan seminggu. Threads memberi ruang untuk posting
lebih sering daripada Instagram, tapi konsisten lebih penting daripada banyak.
Campur sepanjang minggu, jangan dua tipe sama berturut-turut:

| tipe | porsi | tugas | format biasa |
| --- | --- | --- | --- |
| **Bukti** | 1 sampai 2 per minggu | kejadian nyata dengan angka | album |
| **Ajar** | 1 sampai 2 per minggu | satu hal yang bisa dipakai hari ini | album atau utas |
| **Opini** | 1 per minggu | posisi yang bisa membuat sebagian orang tidak setuju | teks |
| **Cerita** | 1 per dua minggu | adegan dengan biaya | utas atau teks |
| **Tawaran** | 1 per dua minggu | yang dijual, disebut terang, tanpa minta maaf | album atau teks + link |
| **Percakapan** | 1 per minggu | polling atau pertanyaan nyata | polling |

Untuk tiap slot berikan: tema, sudut spesifik dari kejadian minggu ini,
format, dan nomor rumus dari threads-hook. Sudut, bukan topik. "AI" bukan
rencana. "Bot balasan saya mengirim 'Teks kosong.' ke 40 orang" adalah
postingan.

Kalau audit akun menunjukkan satu format jauh lebih menyebar (misalnya album
bukti), jadikan format itu tulang punggung minggu ini dan katakan alasannya.

## Threads tidak punya Stories

Slot yang di Instagram diisi Stories diganti dengan:

- **Membalas di kolom balasan** postingan sendiri pada jam pertama.
- **Polling** untuk menampung pendapat dan bahan postingan berikutnya.
- **Postingan sementara** (hilang setelah 24 jam) untuk hal ringan, kalau fitur
  itu tersedia di akun user.

## Kapan posting

Saat audiens user bangun dan tidak sedang bekerja. Untuk pekerja dan pemilik
usaha di Indonesia biasanya malam setelah kerja, sekitar 19.00 sampai 21.00
WIB. Pakai zona waktu audiens, bukan user.

Tapi katakan terang: **jam jauh kurang penting daripada baris pertama.** Kalau
user sibuk mengatur jam sebelum hook-nya jalan, user memoles hal yang salah.

## Ronde engage, wajib

20 menit sehari, sebelum posting, bukan sesudah. Daftar 10 akun:

- **5 jangkauan**: akun dengan audiens yang diinginkan, tempat balasan bagus
  terlihat banyak orang. Balas lebih awal, sebelum kolom balasan ratusan.
- **3 sejawat**: ukuran dan bidang sama. Kelompok yang membalas balik.
- **2 pembeli**: orang yang benar-benar bisa membeli. Balas berminggu-minggu
  sebelum DM, dan jangan pernah jualan di balasan.

Serahkan daftarnya ke threads-balas (mode komentar).

## Keluaran

```
MINGGU 30 NOV - 6 DES

SEN  19.00  ALBUM    BUKTI      #6 Bukti Angka      - {sudut dari minggu ini}
SEL  engage saja (20 menit, daftar di bawah)
RAB  19.00  UTAS     AJAR       #9 Ambil Saja       - {sudut}
KAM  19.30  POLLING  PERCAKAPAN #10 Kalau Kamu      - {sudut}
JUM  19.30  TEKS     OPINI      #22 Pepatah Dibalik - {sudut}
SAB  -
MIN  19.00  UTAS     CERITA     #15 Catatan Gagal   - {sudut}

ENGAGE  (5 jangkauan / 3 sejawat / 2 pembeli)
  ...

Bilang "tulis Senin" dan saya buatkan drafnya.
```

Tulis rencana ke `~/.claude/threads/plan.md` supaya skill lain bisa membacanya.
Tidak ada yang dijadwalkan atau diposting. User yang menjalankan.
