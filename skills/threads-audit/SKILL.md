---
name: threads-audit
description: >-
  Bedah postingan Threads yang sudah diposting user: mana yang benar-benar
  berhasil, kenapa, dan apa yang harus dihentikan. Pakai saat user menempel
  insight Threads atau daftar postingannya dan bertanya "apa yang jalan",
  "kenapa ini sepi", "baca insight saya", "audit akun saya", atau ingin tahu
  harus memperbanyak apa.
---

# threads-audit

Satu-satunya sumber jujur tentang apa yang jalan di sebuah akun adalah akun
itu sendiri. Semua aturan di semua panduan, termasuk di repo ini, hanyalah
dugaan awal. 30 postingan terakhir user adalah buktinya.

## Masukan

Minta yang dimiliki user:

- Insight per postingan: view, suka, balasan, repost, quote, share, dan
  follower baru bila ada. Screenshot boleh.
- Atau daftar postingan dengan view-nya saja. Cukup untuk putaran pertama.
- Ekspor dari alat penjadwal atau konektor (misalnya statistik konten dari
  Repliz) juga boleh.

Baca juga `~/.claude/threads/log.md` kalau ada, karena di situ tercatat rumus
hook tiap postingan.

## Yang diukur

View mentah adalah angka paling tidak berguna, karena kebanyakan ditentukan
oleh jumlah follower. Hitung ini dan tunjukkan cara hitungnya:

| metrik | cara | artinya |
| --- | --- | --- |
| **Kelipatan** | view / median view akun | hit sungguhan atau hari biasa |
| **Sebaran** | (repost + quote + share) per 1.000 view | apakah orang mau menaruh namanya di postingan itu. Sinyal terkuat |
| **Balasan** | balasan per 1.000 view | apakah memancing percakapan |
| **Suka** | suka per 1.000 view | sinyal lemah, murah diberikan |
| **Follow** | follower baru per 1.000 view, bila ada | apakah profil mengubah perhatian jadi follow |

Urutkan berdasarkan kelipatan dan sebaran, bukan view. Postingan 4.000 view
dengan 60 repost mengalahkan postingan 40.000 view dengan 8 repost.

## Bedakan ramai dan menyebar

Postingan pancingan komentar ("kalian tim A atau B?") sering punya balasan
per 1.000 view sangat tinggi tapi sebaran hampir nol. Kolom balasannya ramai,
tapi postingannya tidak pergi ke mana-mana. Kalau tujuannya jangkauan, jangan
salah membaca balasan sebagai keberhasilan.

## Cari polanya

Letakkan lima teratas dan lima terbawah berdampingan, lalu cari pembedanya.
Berani menyimpulkan hal yang tidak disukai user:

- **Baris pertama.** Rumus mana (dari threads-hook) yang ada di lima teratas?
- **Format.** Teks, album, video, utas, polling.
- **Ada bukti atau tidak.** Screenshot, angka, sebelum dan sesudah.
- **Tema.** Di dalam niche atau di luar niche.
- **Panjang teks.**
- **Apakah user membalas di jam pertama.**
- **Hari dan jam.** Periksa **terakhir**, hanya kalau yang lain tidak
  menunjukkan apa-apa. Hampir tidak pernah jadi penyebab.

Nyatakan temuan sebagai klaim beserta buktinya, dan sebutkan tingkat
keyakinannya. Dengan 30 postingan pola bisa terlihat. Dengan 6 belum, dan
mengatakan itu lebih baik daripada mengarang pola.

## Pembeda yang menghemat berbulan-bulan

**Postingan yang dapat view tapi tidak dapat follower bukan postingan gagal,
itu masalah profil.** Postingan yang tidak dapat view adalah masalah baris
pertama. Pisahkan keduanya sebelum memberi saran. Kalau sebaran tinggi tapi
follow rendah, berhenti menulis ulang hook dan pindah ke threads-profil.

## Keluaran

```
AUDIT  ·  31 postingan  ·  1 - 30 Nov  ·  median view 1.150

5 TERATAS (kelipatan)
  12,4x  album bukti      14.300 view  sebaran 7,2/1k  balasan 3,8/1k
   ...
5 TERBAWAH
   0,4x  luar niche          460 view  sebaran 0,0/1k
   ...

KATA DATA
1. Album bukti adalah mesin akun ini. Median 12,4x lawan 0,9x sisanya. n=6.
2. Pancingan komentar ramai tapi tidak menyebar: balasan 31/1k, sebaran 0,8/1k.
3. Postingan luar niche: tidak satu pun di atas 1,2x. Hentikan.
4. Jam dan hari tidak membedakan. Berhenti mengatur jam.

STOP: postingan luar niche.
PERBANYAK: album bukti dengan angka.
```

Lalu serahkan kesimpulannya ke threads-plan supaya minggu depan disusun dari
bukti user sendiri, dan ke threads-viral supaya swipe file disaring ke rumus
yang jalan untuk akun ini.
