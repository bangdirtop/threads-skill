---
name: threads-profil
description: >-
  Beri skor profil Threads dari 100 dan tulis ulang bagian yang kehilangan
  poin: foto, nama, bio, link, postingan yang disematkan, dan beberapa
  postingan teratas yang dilihat pengunjung. Pakai saat user bilang "cek
  profil saya", "perbaiki bio", "kenapa orang nggak follow", "skor akun
  Threads saya", atau menempel profilnya dan bertanya bagaimana kesannya.
---

# threads-profil

Profil bukan etalase yang dijelajahi. Profil adalah **layar keputusan** yang
didatangi dari satu postingan, dan punya sekitar tiga detik untuk menjawab
satu pertanyaan: apakah ada lagi yang seperti tadi di sini, dan apakah ini
untuk saya.

## Masukan

Minta user menempel atau screenshot: nama, handle, bio, link, postingan yang
disematkan, dan lima postingan teratas di profil. Screenshot bagian atas
profil plus satu layar gulir sudah cukup.

Jangan login ke Threads atau Instagram atas nama user.

## Skor

| # | bagian | poin | penuh kalau | biasanya gagal karena |
| --- | --- | --- | --- | --- |
| 1 | Foto | 8 | wajah jelas memenuhi bingkai, kontras tinggi, terbaca saat kecil | logo kecil, foto jauh, latar ramai |
| 2 | Nama | 12 | nama + kata yang dicari orang, misal "Rina, Konten AI" | nama saja |
| 3 | Handle | 6 | pendek, mudah diingat, sama dengan merek | angka dan garis bawah acak |
| 4 | Bio baris pertama | 14 | untuk siapa dan apa yang berubah buat mereka | jabatan, deretan kata sifat, emoji |
| 5 | Bio sisanya | 8 | satu bukti atau satu tawaran terang | daftar identitas dipisah garis tegak |
| 6 | Link | 10 | satu tujuan yang cocok dengan janji di bio | beranda umum, atau lima link yang jadi menu |
| 7 | Postingan disematkan | 14 | postingan terbaik yang membuktikan apa yang akan didapat follower | tidak ada yang disematkan |
| 8 | Lima postingan teratas | 12 | satu niche, terbaca sekilas, ada bukti | campur aduk topik, repost tanpa komentar |
| 9 | Konsistensi tema | 8 | jelas akun ini tentang apa dalam tiga detik | ganti topik tiap hari |
| 10 | Bukti sosial | 8 | angka atau hasil nyata terlihat di bio atau sematan | tidak ada bukti |

Total 100. Jujur. Kebanyakan profil di putaran pertama dapat 30 sampai 50.
Skor yang murah hati tidak berguna.

```
SKOR PROFIL  41/100

  nama              3/12   nama saja, tidak ada kata yang dicari
  bio baris 1       4/14   jabatan dan dua emoji
  disematkan        0/14   tidak ada
  link              4/10   beranda, bukan halaman tawaran
  ...
```

## Tulis ulang, urut dari poin yang paling banyak hilang

Jangan tulis ulang semuanya sekaligus. User harus benar-benar mengubah tiap
bagian satu per satu.

1. **Postingan disematkan.** Perbaikan paling besar dan cuma butuh beberapa
   ketukan. Pilih postingan dengan kelipatan dan sebaran tertinggi dari
   threads-audit, yang paling jelas menunjukkan isi akun.
2. **Nama.** Format `{Nama}, {apa yang dikerjakan, dengan kata yang dicari}`.
   Beri tiga pilihan. Catatan: di beberapa akun nama dan foto mengikuti
   Instagram yang terhubung, jadi perubahan bisa memengaruhi keduanya.
3. **Bio baris pertama.** Untuk siapa dan apa yang berubah. Bukan jabatan,
   bukan kata sifat. Sisa ruangnya untuk satu bukti atau satu tawaran. Batas
   bio 150 karakter.
4. **Link.** Satu tujuan yang cocok dengan janji bio. Threads mengizinkan
   beberapa link (cek di aplikasi), tapi dua link sudah jadi menu, dan menu
   mengubah lebih buruk daripada pintu.
5. **Lima postingan teratas.** Kalau postingan terbaru keluar niche, posting
   satu yang di dalam niche sebelum mendorong orang ke profil.

## Keluaran

Tabel skor, lalu tulisan ulang sebagai blok siap salin dalam urutan perbaikan,
masing-masing sudah lewat threads-human (tanpa em dash). Skor ulang di akhir
dan tunjukkan selisihnya dengan jujur. Kalau tulisan ulang sampai 82 dan
bukan 98, katakan 82, dan sebutkan sisanya, yang biasanya postingan sematan
yang belum ada atau kebiasaan posting di satu niche. Itu bukan tulisan ulang.

Skill ini tidak mengubah apa pun di Threads. User mengedit tiap bagian.
