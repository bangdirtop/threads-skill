---
name: threads-post
description: >-
  Tulis satu postingan Threads (maksimal 500 karakter) dari ide mentah: baris
  pertama dari 26 rumus hook, isi, satu ajakan, satu tag topik, link bila
  perlu, lalu dicek dengan lint_post.py dan threads-human sebelum diposting.
  Pakai saat user bilang "tulis postingan Threads", "bikin thread", "caption
  Threads", "postingan teks", "polling Threads", "tag topik apa", atau punya
  foto/video satu buah yang butuh teks. Untuk rangkaian beberapa postingan
  pakai threads-utas, untuk album pakai threads-album.
---

# threads-post

Di Threads, teksnya adalah kontennya. Tidak ada video yang menyelamatkan baris
pertama yang lemah. Orang membaca satu baris, lalu memutuskan berhenti atau
lanjut menggulir.

## Sebelum menulis

1. Baca `~/.claude/threads/voice.md` kalau ada. Kalau belum ada, minta tiga
   postingan Threads milik user, simpulkan gaya bicaranya, dan tulis filenya
   (template ada di `templates/voice.md` di repo ini). Postingan dengan suara
   yang salah tidak bisa dipakai.
2. Baca `~/.claude/threads/swipe.md` kalau ada. Itu bukti dari threads-viral
   tentang rumus yang sedang jalan di niche user, dan bukti itu mengalahkan
   aturan umum di file ini.
3. Kalau idenya tipis, jangan ditambal. Ajukan satu pertanyaan gabungan: apa
   yang terjadi, ke siapa, berapa biaya atau hasilnya. Satu postingan butuh
   satu hal spesifik yang benar.

## Pilih tujuan dulu

| Tujuan | Rumus yang cocok (lihat threads-hook) | Bentuk |
| --- | --- | --- |
| Menyebar (repost, quote, share) | #2, #3, #20, #22, #23, #26 | opini tajam atau angka yang mengejutkan |
| Disimpan | #4, #5, #9, #11 | cara, template, daftar pendek |
| Balasan | #7, #10, #12, #14, #16, #21 | pertanyaan nyata, pengalaman yang bisa dibandingkan |
| Follow | #6, #8, #15, #25 | bukti dengan angka, cerita gagal yang jujur |
| Klik | #19, #24 | tenggat nyata, hal baru |

Balasan banyak belum tentu menyebar. Postingan yang memancing komentar sering
ramai di kolom balasan tapi tidak di-repost. Kalau tujuannya jangkauan ke luar
follower, ukur repost + quote + share per 1.000 view, bukan jumlah balasan.

## Bentuk

```
Baris 1     klaim, angka, atau pertanyaan nyata. Bukan sapaan, bukan "WARGA!!",
            bukan emoji di karakter pertama. Usahakan di bawah 120 karakter.
Isi         1 sampai 4 kalimat pendek. Satu baris kosong di antara gagasan.
            Kata yang ingin dicari orang ditulis sebagai kalimat biasa di sini.
Ajakan      satu. Repost, simpan, balas dengan kata tertentu, atau klik. Satu.
Tag topik   satu, di akhir. Atau tidak sama sekali.
```

Batas keras 500 karakter. Kalau isinya butuh lebih, itu utas (threads-utas),
album (threads-album), atau lampiran teks panjang kalau fitur itu tersedia di
akun user.

## Aturan khusus Threads

- **Satu tag topik per postingan.** Threads memakai tag sebagai label topik,
  bukan dinding tagar. Pilih yang paling spesifik dan benar-benar dicari
  komunitasnya. Linter menggagalkan lebih dari satu.
- **Link bisa diklik.** Tidak perlu "link di bio". Satu tujuan saja. Di utas,
  taruh link di postingan terakhir supaya postingan pertama tetap bersih.
  Kalau user curiga link menurunkan jangkauan di akunnya, uji dengan data
  sendiri (threads-audit), jangan pakai mitos.
- **Polling** cocok untuk tujuan balasan: maksimal 4 pilihan, berlaku 24 jam.
  Pilihan harus saling eksklusif dan semuanya masuk akal untuk dipilih.
- **Media opsional tapi membantu.** Satu foto atau screenshot yang jadi bukti
  lebih kuat daripada kalimat yang mengklaim bukti.
- **Tidak ada fitur "lebih lanjut" yang menyembunyikan isi**, tapi orang tetap
  hanya membaca baris pertama sebelum memutuskan. Perlakukan baris pertama
  seperti hook video.

## Alur kerja

1. Pilih tujuan dan sebutkan alasannya.
2. Tulis tiga kandidat baris pertama dari tiga rumus berbeda, simpan ke file,
   lalu jalankan `python3 ../threads-hook/hookscore.py kandidat.txt`. Tunjukkan
   peringkatnya. Kalau teratas di bawah 50, hook belum ketemu.
3. Tulis postingan dengan hook pemenang.
4. Jalankan threads-human: `python3 ../threads-human/humanize.py draf.txt -o draf.txt --report`,
   tulis ulang baris yang ditandai, lalu `detect.py` sampai LOLOS.
5. Jalankan `python3 lint_post.py draf.txt --keywords "kata kunci 1,kata kunci 2"`.
   Perbaiki semua GAGAL. Putuskan tiap AWAS secara terbuka.
6. Cetak blok siap salin, lalu ringkasan:

```
POSTINGAN SIAP
tujuan:     menyebar
hook:       #3 Tidak Ada yang Bilang, skor 88 KUAT
panjang:    312/500
ajakan:     satu, repost
tag topik:  1
humanizer:  LOLOS 84
linter:     SIAP
```

7. Jangan memposting. User yang memposting. Kalau user bilang "ya", catat ke
   `~/.claude/threads/log.md`: tanggal, nomor rumus, baris pertama, format.

## Jangan pernah

- Mengarang angka, klien, omzet, atau hasil atas nama user, bahkan sebagai
  contoh. Angka yang belum ada ditulis `{{angka}}` dan ditandai.
- Memakai em dash atau en dash. Larangan total, tanpa kuota.
- Dua ide dalam satu postingan. Itu dua postingan.
