---
name: threads-viral
description: >-
  Cari postingan Threads yang benar-benar sedang jalan di niche user, urutkan
  berdasarkan seberapa jauh tiap postingan mengalahkan median akunnya sendiri,
  beri nama rumus hook-nya, baca statistik profil pesaing, lalu jadikan swipe
  file untuk ditulis ulang. Pakai saat user bilang "cari yang viral", "apa
  yang lagi jalan", "riset niche", "bongkar akun ini", "bikin swipe file",
  "kenapa postingan ini rame", "bandingkan dengan akun X", atau bertanya
  harus bikin apa tanpa punya bukti.
---

# threads-viral

Skill riset. Skill lain menulis, yang ini melihat. Jalankan bulanan, bukan
harian. Rumus bertahan satu musim.

```bash
python3 swipe.py kumpulan.tsv --out ~/.claude/threads/swipe.md
```

## Satu ide yang membuat ini berguna

**View mentah bukan bukti.** Akun 500 rb follower yang dapat 100 rb view sedang
sepi. Akun 3 rb follower yang dapat 100 rb view menemukan sesuatu, dan sesuatu
itu bisa ditiru bentuknya.

Jadi semuanya diurutkan dengan **kelipatan**: view dibagi median view akun itu
sendiri. Di atas 3x adalah sinyal. Di bawah 1,5x adalah hari biasa akun itu dan
tidak mengajarkan apa-apa.

Kumpulkan akun yang ukurannya **paling jauh 10x ukuran akun user**. Rumus yang
jalan di 1 juta follower sering jalan karena sudah 1 juta follower.

## Langkah 1: pilih akun

Minta 6 sampai 12 akun dari user, atau usulkan lalu minta persetujuan:

- **4 langsung**: niche sama, jualan sama, sedikit di depan.
- **4 bersebelahan**: niche beda, audiens sama. Format sering dipinjam dari
  sini sebelum ada yang memakainya di niche user.
- **2 sampai 4 besar**: hanya untuk format, bukan untuk frekuensi atau nada.

Pakai juga postingan yang di-**simpan** user di Threads. Itu korpus yang paling
relevan dan sudah tersaring selera user.

## Langkah 2: lihat

Pakai alat baca yang memang ada di sesi ini, misalnya browser bawaan, ekstensi
Chrome milik user, atau konektor yang bisa mencari konten Threads (contohnya
konektor Repliz dengan pencarian konten dan konten per pengguna). Volumenya
kecil, cukup dibaca.

**Aturan yang tidak bisa ditawar:**

- **Jangan pernah login ke Threads atau Instagram atas nama user dan jangan
  minta kata sandi.** Kalau halaman butuh login, user yang sudah login.
- **Ini membaca, bukan scraping.** Sepuluh akun, belasan postingan per akun,
  dengan kecepatan manusia. Jangan membuat crawler, jangan memakai jasa
  scraping massal, jangan diulang di latar belakang.
- **Tiru rumusnya, bukan postingannya.** Bentuk hook, struktur, panjang, format.
  Bukan kalimatnya, bukan suaranya. Cantumkan akun sumber di tiap baris swipe
  file.

**Yang dicatat per postingan:**

| kolom | catatan |
| --- | --- |
| akun | handle |
| follower | dari profil |
| median | lihat 12 postingan terakhir, ambil view yang di tengah |
| views | postingan ini |
| hook | baris pertama apa adanya, termasuk salah ketiknya |
| format | teks, album, video, utas, polling |
| balasan, repost | opsional, untuk melihat apakah ramai atau menyebar |

Median adalah kolom terpenting. Tanpa median, kamu kembali mengurutkan
berdasarkan jumlah follower, dan itu yang mau dihindari skill ini.

## Langkah 3: urutkan

Isi file TSV dengan header, lalu jalankan:

```
akun	follower	median	views	hook	format
@contoh	4800	1100	38000	Tidak ada yang bilang kalau 20 postingan pertama memang sepi	album
```

```bash
python3 swipe.py kumpulan.tsv --out ~/.claude/threads/swipe.md
```

Script menghitung kelipatan, memberi nama rumus dari 26 rumus di
threads-hook, memberi skor hook, dan membandingkan sepertiga atas dengan
sepertiga bawah. Angka boleh ditulis 12rb atau 1,2jt.

## Langkah 4: baca profil pesaing

Untuk akun yang dibandingkan, catat yang memang terlihat publik: follower,
jumlah postingan, bio, frekuensi posting kira-kira, dan format yang paling
sering. Jangan menyiratkan bisa melihat siapa yang menyukai atau membalas
postingan akun lain.

## Langkah 5: katakan artinya, hati-hati

Laporkan tiga hal saja:

1. **Rumus yang dominan** di sepertiga atas, dengan jumlah. Dua rumus yang
   masing-masing muncul empat kali di enam akun adalah temuan. Satu rumus yang
   muncul dua kali belum.
2. **Kesamaan struktur** di sepertiga atas yang tidak ada di bawah: panjang
   hook, format (album lawan teks), ada bukti visual atau tidak, letak ajakan.
3. **Yang tak terklasifikasi.** Hook yang tidak dikenali script bisa jadi
   kebisingan atau rumus baru yang belum ada di `hooks.json`. Baca manual. Ini
   kolom paling berharga.

Sebutkan ukuran sampel dan tingkat keyakinan dengan kata-kata biasa. 40
postingan dari 6 akun bisa mendukung klaim. 12 postingan belum.

## Langkah 6: jadikan bahan tulis

Untuk tiga rumus teratas, tulis **versi user**: cerita dan angka user sendiri
dalam bentuk yang sedang jalan. Serahkan ke threads-post, threads-utas, atau
threads-album dengan nomor rumus sudah dipilih.

Jangan pernah menyerahkan "bikin yang kayak gini". Serahkan baris pertama yang
bisa user posting besok.

Tulis hasil ke `~/.claude/threads/swipe.md`. threads-post dan threads-plan
membacanya. Skill ini tidak memposting, mengikuti, menyukai, atau mengirim
pesan apa pun.
