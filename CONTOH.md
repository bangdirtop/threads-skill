# Buku Contoh threads-skill

### Pola, contoh, dan studi kasus untuk 12 skill

Pendamping [PANDUAN.md](PANDUAN.md). Kalau PANDUAN menjelaskan **cara kerja**
tiap skill, buku ini menunjukkan **cara memakainya**:

- **Pola**: kerangka perintah yang tinggal diisi.
- **Contoh**: 8 perintah siap salin per skill, dari yang paling sederhana
  sampai yang paling lengkap.
- **Studi kasus**: satu cerita utuh dari masalah sampai hasil.

> 📌 **Tentang tokoh di buku ini.** Rina, Bayu, dan Sari adalah tokoh
> **rekaan**, begitu juga semua angka di studi kasus. Tapi skor hook,
> skor humanizer, dan hasil linter di sini **dihitung beneran** pakai script
> di repo ini, bukan dikarang. Jadi kalau kamu menjalankan teks yang sama,
> hasilnya sama.

**Tokoh:**

| Tokoh | Usaha | Akun |
| --- | --- | --- |
| **Rina** | jualan kopi susu literan, Bekasi | 1.900 follower |
| **Bayu** | editor video lepas yang pakai AI | 4.200 follower |
| **Sari** | affiliate Shopee alat dapur, akun baru | 900 follower |

> 💡 Pakai plugin? Awali nama skill dengan `threads-skill:`, misalnya
> `/threads-skill:threads-post`. Disalin langsung ke `~/.claude/skills`?
> Cukup `/threads-post`. Di buku ini ditulis versi plugin.

---

## Daftar Isi

1. [threads-hook](#1-threads-hook)
2. [threads-post](#2-threads-post)
3. [threads-utas](#3-threads-utas)
4. [threads-album](#4-threads-album)
5. [threads-human](#5-threads-human)
6. [threads-audit](#6-threads-audit)
7. [threads-viral](#7-threads-viral)
8. [threads-plan](#8-threads-plan)
9. [threads-balas](#9-threads-balas)
10. [threads-dm](#10-threads-dm)
11. [threads-profil](#11-threads-profil)
12. [threads-repurpose](#12-threads-repurpose)
13. [Alur gabungan: satu minggu Rina](#13-alur-gabungan-satu-minggu-rina)

---

## 1. threads-hook

### Pola

```
/threads-skill:threads-hook bikinin [jumlah] hook soal [kejadian + angka],
tujuannya biar orang [repost / simpan / balas / follow / klik]
```

Bahan paling penting: **satu kejadian nyata dengan angka.** Tanpa itu, hook
yang keluar pasti umum.

### Contoh

1. ```
   /threads-skill:threads-hook bikinin 3 hook soal omzet saya naik dari
   Rp 6 juta ke Rp 8,4 juta setelah ganti foto produk
   ```
2. ```
   /threads-skill:threads-hook skor hook ini: "Akhirnya saya sadar soal iklan"
   ```
3. ```
   /threads-skill:threads-hook bikinin hook pakai rumus #15 Catatan Gagal
   soal 12 video pertama saya yang sepi
   ```
4. ```
   /threads-skill:threads-hook 3 hook yang tujuannya bikin orang nyimpen,
   soal template balasan chat pembeli
   ```
5. ```
   /threads-skill:threads-hook hook ini skornya 48, kenapa lemah dan
   gimana benerinnya: "Mau cerita soal pengalaman jualan aku"
   ```
6. ```
   Bongkar postingan ini, ambil rumusnya, kasih templat kosong:
   [tempel postingan orang]
   ```
7. ```
   /threads-skill:threads-hook bandingkan 5 hook ini, urutkan, dan bilang
   mana yang kamu pilih: [tempel 5 baris]
   ```
8. ```
   /threads-skill:threads-hook bikinin hook adu langsung (#17) soal
   Canva lawan CapCut buat bikin konten jualan, saya pakai dua-duanya 2 bulan
   ```

### Studi kasus: Rina dan hook yang dibuka "Halo warga"

**Masalah.** Rina selalu buka postingan dengan "Halo warga Threads, aku mau
cerita...". View-nya mentok di bawah 1.000.

**Yang dikasih ke Claude.**

```
/threads-skill:threads-hook bikinin 3 hook. Kejadiannya: dulu saya jualan
20 botol kopi literan sehari, sekarang 85. Saya juga pernah bayar endorse
Rp 1,2 juta dan yang beli cuma 3 orang.
```

**Hasil (skor asli dari hookscore.py):**

```
HOOK (diurutkan)
   91  KUAT   Rp 1,2 juta habis buat endorse, yang beli cuma 3 orang.
   78  KUAT   Dulu jualan kopi literan cuma 20 botol sehari. Sekarang 85.
   15  LEMAH  Halo warga Threads, aku mau cerita soal jualan kopi aku nih
```

**Pelajaran.**
- Hook lama Rina dapat 15 karena dibuka sapaan, nggak ada angka, dan nggak
  ada yang dipertaruhkan.
- Dua hook baru langsung naruh angka di depan.
- Rina punya **dua cerita**, jadi dua postingan. Bukan satu postingan berisi
  dua cerita.

---

## 2. threads-post

### Pola

```
/threads-skill:threads-post tulis postingan soal [kejadian + angka].
Tujuannya [repost / simpan / balas / follow / klik].
[Opsional: kata yang ingin dicari orang, tag topik, link]
```

### Contoh

1. ```
   /threads-skill:threads-post tulis postingan soal pembeli saya yang order
   ulang 3 kali seminggu gara-gara kartu ucapan tulisan tangan
   ```
2. ```
   /threads-skill:threads-post tujuannya biar orang nyimpen: 4 template
   balasan chat buat pembeli yang nanya "masih ada kak?"
   ```
3. ```
   /threads-skill:threads-post bikin polling 4 pilihan: kendala terbesar
   kalian jualan online. Tujuannya cari bahan postingan minggu depan
   ```
4. ```
   /threads-skill:threads-post opini: jualan online nggak butuh logo bagus
   di 6 bulan pertama. Bukti saya: 140 order pertama tanpa logo
   ```
5. ```
   /threads-skill:threads-post saya punya 1 foto sebelum dan sesudah
   kemasan baru. Tulis teksnya, tujuannya repost
   ```
6. ```
   /threads-skill:threads-post tenggat: harga kelas naik 1 Desember.
   Link pendaftaran: [link]. Satu ajakan saja, klik
   ```
7. ```
   /threads-skill:threads-post cek draf saya pakai lint_post, kata kunci
   "kopi literan": [tempel draf]
   ```
8. ```
   /threads-skill:threads-post tulis postingan dengan hook #16 Pertanyaan
   Apa Adanya. Pertanyaannya: "kak kopinya tahan berapa hari di kulkas?"
   ```

### Studi kasus: Rina menulis postingan 85 botol

**Masalah.** Rina sudah punya hook (78, dari studi kasus #1). Sekarang perlu
postingan utuh.

**Yang dikasih ke Claude.**

```
/threads-skill:threads-post pakai hook "Dulu jualan kopi literan cuma 20
botol sehari. Sekarang 85." Yang saya ubah: tanggal produksi ditulis tangan
di botol. Biayanya cuma spidol. Tujuan: disimpan. Kata kunci: kopi literan.
```

**Hasil.**

```
Dulu jualan kopi literan cuma 20 botol sehari. Sekarang 85.

Yang saya ubah cuma satu: botolnya saya kasih tanggal produksi tulisan tangan. Pembeli jadi percaya kopinya baru, terus pesan ulang tiap Senin.

Biaya tambahannya Rp 0, cuma spidol.

Simpan kalau kamu juga jualan minuman literan.

#kopiliteran
```

```
POSTINGAN SIAP
tujuan:     simpan
hook:       #5 Waktu Dipangkas, skor 78 KUAT
panjang:    304/500
ajakan:     satu, simpan
tag topik:  1
humanizer:  LOLOS 100
linter:     SIAP
```

**Pelajaran.** Satu ide (tanggal produksi), satu angka sebelum dan sesudah,
satu biaya (Rp 0), satu ajakan, satu tag. Nggak ada yang lain.

---

## 3. threads-utas

### Pola

```
/threads-skill:threads-utas bikin utas [jumlah] postingan soal [topik + angka].
Postingan pertama harus bisa berdiri sendiri. Link di postingan terakhir: [link]
```

### Contoh

1. ```
   /threads-skill:threads-utas 5 langkah saya naikin harga jasa edit dari
   Rp 150 rb ke Rp 1,2 juta dalam 8 bulan
   ```
2. ```
   /threads-skill:threads-utas cerita gagal: stok 300 botol basi karena
   kulkas mati. Apa yang saya ubah sesudahnya
   ```
3. ```
   /threads-skill:threads-utas bikinin kerangka dulu, satu baris per
   postingan, jangan langsung ditulis: cara riset harga pesaing
   ```
4. ```
   /threads-skill:threads-utas pecah artikel ini jadi utas 6 postingan:
   [tempel artikel]
   ```
5. ```
   /threads-skill:threads-utas cek utas saya, pisahkan tiap postingan
   dengan ---: [tempel utas]
   ```
6. ```
   /threads-skill:threads-utas postingan pertama utas saya terlalu panjang,
   pendekkan jadi di bawah 120 karakter tanpa buang angkanya
   ```
7. ```
   /threads-skill:threads-utas bikin utas argumen: kenapa reseller kecil
   jangan perang harga. Tiap postingan satu alasan dengan angka
   ```
8. ```
   /threads-skill:threads-utas ubah utas ini jadi album kalau lebih cocok,
   dan bilang alasannya: [tempel utas]
   ```

### Studi kasus: Bayu dan harga jasa edit

**Masalah.** Bayu punya cerita panjang soal naik harga. Nggak muat 500
karakter, dan buktinya bukan gambar, jadi utas.

**Hasil (8 postingan):**

```
Klien pertama saya bayar Rp 150 rb per video. Sekarang Rp 1,2 juta. Ini 5 hal yang saya ubah dalam 8 bulan.
---
Kalau kamu editor pemula, harga murah itu bukan strategi. Itu jebakan. Klien murah minta revisi paling banyak.
---
1. Saya berhenti kirim file mentah. Klien selalu dapat 3 detik pertama yang sudah dipoles, bahkan di draf.
---
2. Saya pakai AI buat subtitle dan potong jeda. Waktu edit 1 video turun dari 5 jam ke 2 jam.
---
3. Portofolio saya isinya angka: view sebelum dan sesudah saya edit, bukan cuma video cantik.
---
4. Revisi saya batasi 2 kali. Revisi ketiga bayar Rp 100 rb.
---
5. Harga saya naikkan tiap 3 klien baru. Yang pergi cuma klien yang paling banyak minta revisi.
---
Ringkasnya: poles 3 detik pertama, pakai AI buat kerja kasar, jual angka, batasi revisi, naik pelan-pelan. Link contoh portofolio: example.com/porto
```

```
UTAS SIAP  ·  8 postingan
hook:       skor 91 KUAT
terpanjang: postingan 8, 147/500
ajakan:     link di postingan terakhir
linter:     SIAP
```

**Pelajaran.**
- Postingan 1 sudah bernilai sendirian: orang tahu dari Rp 150 rb ke
  Rp 1,2 juta walaupun berhenti di situ.
- Tiap postingan tengah bisa di-quote tanpa konteks.
- Link ditaruh di akhir, bukan di postingan pertama.

---

## 4. threads-album

### Pola

```
/threads-skill:threads-album bikin album dari [bukti apa saja].
Tujuannya [simpan / repost / follow]. Teks slide dulu, gambar nanti.
```

### Contoh

1. ```
   /threads-skill:threads-album bikin album dari screenshot komisi 14 hari,
   tujuannya biar orang nyimpen
   ```
2. ```
   /threads-skill:threads-album album sebelum dan sesudah kemasan,
   3 pasang foto, tujuannya repost
   ```
3. ```
   /threads-skill:threads-album 6 slide: template balasan chat pembeli,
   slide terakhir ringkasan yang enak di-screenshot
   ```
4. ```
   /threads-skill:threads-album teks slide-nya sudah oke, sekarang buatkan
   file gambar 1080x1350, warna aksen oranye
   ```
5. ```
   /threads-skill:threads-album saya punya video 40 detik, tuliskan teks
   pengantar dan kartu teks untuk 3 detik pertama
   ```
6. ```
   /threads-skill:threads-album slide 2 saya kepanjangan, pecah jadi dua
   slide, maksimal 25 kata per slide
   ```
7. ```
   /threads-skill:threads-album bikin album perbandingan harga 5 toko,
   satu toko per slide, slide ringkasan pakai tabel
   ```
8. ```
   /threads-skill:threads-album ubah utas ini jadi album 7 slide:
   [tempel utas]
   ```

### Studi kasus: Sari dan 14 hari affiliate

**Masalah.** Sari punya 14 screenshot komisi harian tapi bingung nyusunnya.
Kalau diposting sebagai teks, nggak ada yang percaya.

**Teks slide (disetujui Sari sebelum gambar dibuat):**

```
1  SAMPUL   14 HARI, RP 2,3 JUTA
2  BUKTI    screenshot total komisi 14 hari
3           Video jenis 1: unboxing
4           Video jenis 2: sebelum dan sesudah masak
5           Video jenis 3: perbandingan harga
6           Komisi per hari (grafik)
7  RINGKAS  3 jenis video, Rp 0 iklan, Rp 2.317.000 komisi
8  AJAKAN   Simpan kalau mau mulai dari nol.
```

**Teks pengantar:**

```
14 hari affiliate alat dapur, komisi Rp 2.317.000. Tanpa iklan.

Akun baru, 900 follower. Videonya cuma 3 jenis: unboxing, sebelum dan sesudah masak, sama perbandingan harga.

Screenshot komisi per hari ada di album.

Simpan kalau kamu mau mulai affiliate dari nol.
```

Skor hook 80 KUAT · humanizer LOLOS 96 · 265/500 · linter SIAP.

**Pelajaran.**
- Bukti terkuat (total komisi) di slide 2, bukan di akhir.
- Angka ganjil (Rp 2.317.000) lebih dipercaya daripada "Rp 2 jutaan".
- Teks slide disetujui dulu, gambar dibuat belakangan. Hemat waktu kalau
  ada yang perlu diubah.

---

## 5. threads-human

### Pola

```
/threads-skill:threads-human rapikan ini biar nggak kayak AI:
[tempel teks]
```

### Contoh

1. ```
   /threads-skill:threads-human rapikan caption ini: [tempel]
   ```
2. ```
   /threads-skill:threads-human cek aja, jangan diubah, kasih skor dan
   tandai yang kerasa AI: [tempel]
   ```
3. ```
   /threads-skill:threads-human bandingkan versi lama dan versi baru ini,
   kasih selisih skornya: [tempel dua versi]
   ```
4. ```
   /threads-skill:threads-human hapus semua em dash di teks ini tanpa
   bikin kalimatnya patah-patah: [tempel]
   ```
5. ```
   /threads-skill:threads-human skor KONKRET saya rendah, saya punya angka
   ini: [angka]. Masukkan tanpa ngubah maksudnya
   ```
6. ```
   /threads-skill:threads-human saya selalu nulis huruf kecil semua dan
   pakai "wkwk". Jangan dihilangkan, itu gaya saya
   ```
7. ```
   Kata "signifikan" itu memang sering saya pakai. Hapus dari daftar slop
   di slop.json
   ```
8. ```
   /threads-skill:threads-human rapikan 5 balasan komentar ini sekaligus:
   [tempel]
   ```

### Studi kasus: caption hasil AI mentah

**Sebelum** (ditulis AI lain, ditempel apa adanya):

```
Di era digital ini, jualan online bukan sekadar upload foto [EM DASH] tapi strategi yang krusial.

Hasilnya? Omzet meningkat secara signifikan. Cepat. Mudah. Efektif.

Jangan lupa follow dan repost kalau setuju! #jualanonline #umkm #bisnis
```

*(Tanda [EM DASH] di atas menggantikan karakter aslinya, karena buku ini
sendiri bebas em dash.)*

**Yang dibetulkan otomatis:** 1 em dash, "di era digital ini" dihapus,
"secara signifikan" jadi "jauh", "krusial" jadi "penting".

**Yang ditandai untuk ditulis ulang:** "bukan sekadar X, tapi Y",
"Hasilnya?", "Cepat. Mudah. Efektif.", pancingan "jangan lupa follow" dan
"repost kalau setuju", 3 tag topik.

**Sesudah** (ditulis ulang dengan angka asli dari pemiliknya):

```
Jualan online saya baru jalan setelah berhenti cuma upload foto produk.

Sekarang tiap foto saya kasih satu kalimat: dipakai buat apa, sama siapa. Omzet Oktober naik dari Rp 6,1 juta ke Rp 8,4 juta.

Kamu jualan apa? Coba tulis satu kalimat itu buat produk terlarismu.

#jualanonline
```

**Skor (detect.py):**

```
            sebelum   sesudah
VARIASI       100       100
KONKRET         0        93
SLOP            0       100
JEJAK          50       100
SUARA           0       100
SKOR           18        96
PUTUSAN     GAGAL     LOLOS      selisih +78
```

**Pelajaran.** Script cuma bisa mengganti kata. Lompatan dari 18 ke 96
datang dari **dua hal yang dikerjakan manusia**: menulis ulang pola kalimat,
dan memasukkan angka asli.

---

## 6. threads-audit

### Pola

```
/threads-skill:threads-audit akun @[namaakun]
[lampirkan: screenshot insight / daftar postingan + view / atau minta tarik dari konektor]
```

### Contoh

1. ```
   /threads-skill:threads-audit akun @namaakun, tarik datanya dari Repliz
   ```
2. ```
   /threads-skill:threads-audit ini 15 screenshot insight saya: [lampirkan]
   ```
3. ```
   /threads-skill:threads-audit ini daftar 30 postingan dan view-nya,
   cukup buat putaran pertama: [tempel]
   ```
4. ```
   /threads-skill:threads-audit kenapa postingan ini rame komentar tapi
   view-nya sepi? [tempel angka]
   ```
5. ```
   /threads-skill:threads-audit bandingkan album lawan teks di akun saya,
   mana yang lebih menyebar
   ```
6. ```
   /threads-skill:threads-audit audit ulang, bandingkan dengan audit
   minggu lalu di ~/.claude/threads/audit/
   ```
7. ```
   /threads-skill:threads-audit view saya banyak tapi follower nggak naik.
   Ini masalah hook atau profil?
   ```
8. ```
   /threads-skill:threads-audit lalu langsung perbarui plan.md minggu
   depan dari hasilnya
   ```

### Studi kasus: Rina, 12 postingan

**Data (rekaan), median view 1.200:**

```
 11,8x  album sebelum-sesudah botol  14.200 view  sebaran 8,5  balasan   2,7
  8,2x  album omzet harian            9.800 view  sebaran 9,0  balasan   3,1
  5,2x  album 3 kesalahan botol       6.300 view  sebaran 8,1  balasan   3,5
  1,8x  polling aren vs pandan        2.100 view  sebaran 1,4  balasan  90,5
  1,6x  video racik kopi              1.900 view  sebaran 4,7  balasan   6,3
  1,1x  teks pancingan tim aren       1.300 view  sebaran 0,8  balasan 107,7
  0,9x  teks harga naik               1.100 view  sebaran 1,8  balasan  13,6
  0,8x  gambar menu baru                900 view  sebaran 1,1  balasan   4,4
  0,6x  teks curhat                     700 view  sebaran 1,4  balasan  12,9
  0,5x  teks tips sabar                 640 view  sebaran 0,0  balasan   3,1
  0,4x  teks promo                      520 view  sebaran 0,0  balasan   1,9
  0,4x  teks luar niche sepak bola      480 view  sebaran 0,0  balasan   6,2
```

**Kata data:**
1. Tiga album bukti semuanya di atas 5x dengan sebaran 8 sampai 9. Ini
   mesin akun Rina. n=3, belum banyak, tapi selisihnya besar.
2. Polling dan pancingan "tim aren" balasannya 90 sampai 108 per 1.000
   view, tapi sebarannya cuma 0,8 sampai 1,4. Rame, nggak menyebar.
3. Teks luar niche dan teks promo paling bawah.

```
STOP:       teks promo, luar niche
PERBANYAK:  album bukti dengan angka
CATATAN:    12 postingan masih sedikit, audit lagi setelah 30
```

**Pelajaran.** Kalau Rina cuma lihat kolom balasan, dia bakal mengira
pancingan "tim aren" itu postingan terbaiknya. Padahal yang bawa orang baru
adalah album.

---

## 7. threads-viral

### Pola

```
/threads-skill:threads-viral riset niche [niche]. Akun yang dipantau:
[4 langsung, 4 tetangga, 2 besar]. Ukuran akun saya: [follower]
```

### Contoh

1. ```
   /threads-skill:threads-viral usulkan 10 akun buat dipantau di niche
   kopi kekinian, ukuran akun saya 1.900 follower
   ```
2. ```
   /threads-skill:threads-viral ini TSV postingan yang saya kumpulin,
   jalankan swipe.py: [lampirkan file]
   ```
3. ```
   /threads-skill:threads-viral bongkar akun @namaakun: 12 postingan
   terakhir, median, dan mana yang di atas 3x
   ```
4. ```
   /threads-skill:threads-viral cari postingan Threads soal "affiliate
   shopee" 7 hari terakhir pakai Repliz, urutkan pakai kelipatan
   ```
5. ```
   /threads-skill:threads-viral dari swipe file saya, tulis 3 hook versi
   saya sendiri pakai cerita saya: [cerita]
   ```
6. ```
   /threads-skill:threads-viral ini postingan tersimpan saya di Threads,
   rumus apa yang paling sering muncul? [tempel]
   ```
7. ```
   /threads-skill:threads-viral kolom TAK TERKLASIFIKASI ada 4, bacain dan
   bilang mana yang layak jadi rumus baru
   ```
8. ```
   /threads-skill:threads-viral bandingkan follower dan frekuensi posting
   akun saya dengan 3 pesaing ini: [handle]
   ```

### Studi kasus: Rina mengintip 3 akun minuman

**Data yang dikumpulkan Rina (rekaan), dijalankan lewat swipe.py:**

```
SWIPE  ·  9 postingan  ·  3 akun  ·  dasar: median akun sendiri

OUTLIER (di atas 3x)
   23.3x  hook  41  #3 Tidak Ada yang Bilang  @kopi.a   21,000 (median 900)    [album]
          "Tidak ada yang bilang kalau jualan kopi literan itu musuhnya es batu"
    8.0x  hook  84  #1 Pengakuan Biaya        @usaha.b  12,000 (median 1,500)  [album]
          "Rp 2,3 juta habis gara-gara salah pilih botol"
    8.0x  hook  55  #2 Perintah Larangan      @resto.c   4,800 (median 600)    [teks]
          "Berhenti kasih diskon. Kasih bonus gelas"
    6.0x  hook  80  #5 Waktu Dipangkas        @usaha.b   9,000 (median 1,500)  [video]
          "Dulu bikin 50 botol butuh 3 jam. Sekarang 45 menit"

TAK TERKLASIFIKASI (3)
    1.2x  @kopi.a:  "Menurut kalian enak kopi aren atau pandan?"
    0.9x  @usaha.b: "Minggu ini capek banget"
    0.8x  @resto.c: "Yuk mampir ke outlet kami"

SAMPEL: 9 postingan dari 3 akun, belum cukup untuk klaim, anggap petunjuk.
```

**Hook versi Rina (pakai cerita Rina sendiri):**

```
#1  Rp 1,2 juta habis buat endorse, yang beli cuma 3 orang.      skor 91
#3  Tidak ada yang bilang kalau musuh kopi literan itu es batu.  skor 41
```

**Pelajaran, dan ini penting.**
- Hook "es batu" dapat skor 41 tapi postingan aslinya 23x. **Skor hook
  bukan ramalan.** Skor menyaring yang jelas jelek. Yang menang di dunia
  nyata kadang menang karena hal lain: topiknya pas, albumnya bagus.
- Karena itu, swipe file selalu mengurutkan pakai **kelipatan asli**, bukan
  pakai skor.
- 9 postingan dari 3 akun cuma petunjuk. Rina perlu sekitar 40 postingan
  dari 6 akun sebelum boleh menyimpulkan sesuatu.

---

## 8. threads-plan

### Pola

```
/threads-skill:threads-plan susun minggu [tanggal]. Yang terjadi minggu ini:
[kejadian nyata + angka]. Yang saya jual: [produk]. Posting [N] kali.
```

### Contoh

1. ```
   /threads-skill:threads-plan susun minggu depan. Minggu ini saya ganti
   botol, order naik dari 20 ke 85 sehari
   ```
2. ```
   /threads-skill:threads-plan cuma bisa posting 3 kali minggu ini,
   pilihkan 3 slot paling penting
   ```
3. ```
   /threads-skill:threads-plan susun dari hasil audit kemarin di
   ~/.claude/threads/audit/
   ```
4. ```
   /threads-skill:threads-plan minggu depan saya launching kelas, masukkan
   1 slot tawaran dan 2 slot bukti yang mendukung
   ```
5. ```
   /threads-skill:threads-plan cariin 10 akun buat ronde engage: 5 besar,
   3 seukuran, 2 calon pembeli, niche kopi
   ```
6. ```
   Tulis Senin
   ```
7. ```
   /threads-skill:threads-plan saya nggak punya kejadian apa-apa minggu ini.
   Tanyain saya dulu sampai ketemu bahannya
   ```
8. ```
   /threads-skill:threads-plan tukar slot Rabu dan Jumat, lalu skor ulang
   hook-nya
   ```

### Studi kasus: minggu Rina setelah audit

**Yang dikasih ke Claude.**

```
/threads-skill:threads-plan susun minggu depan dari audit kemarin.
Kejadian minggu ini: endorse Rp 1,2 juta cuma dapat 3 pembeli; tanggal
produksi tulisan tangan bikin order 20 jadi 85; saya coba jual aren dan
pandan 30 hari.
```

**Hasil:**

```
SEN  19.00  ALBUM    BUKTI    #5  "Dulu jualan kopi literan cuma 20 botol sehari. Sekarang 85."  (78)
SEL  engage saja
RAB  19.00  ALBUM    CERITA   #1  "Rp 1,2 juta habis buat endorse, yang beli cuma 3 orang."      (91)
KAM  19.30  POLLING  OBROLAN       "Kalian lebih sering beli kopi literan buat kantor atau rumah?"
JUM  19.30  ALBUM    ADU      #17 "Kopi aren lawan kopi pandan: saya jual dua-duanya 30 hari, satunya jauh." (74)
SAB  -
MIN  19.00  TEKS     OPINI    #2  "Berhenti kasih diskon. Kasih bonus gelas, pembeli balik lagi." (55)

ENGAGE  5 jangkauan / 3 sejawat / 2 pembeli
```

**Pelajaran.**
- Tiga slot album, karena audit bilang album adalah mesin akun Rina.
- Hook Minggu skornya 55 (OKE): nggak ada angka. Claude akan minta Rina
  menambahkan angka, misalnya berapa pembeli yang balik setelah dapat bonus
  gelas, sebelum hari Minggu.
- Polling tetap ada sekali, tapi tujuannya cari bahan, bukan jangkauan.

---

## 9. threads-balas

### Pola

```
Mode 1 (kolom balasan sendiri):
/threads-skill:threads-balas urus balasan di postingan saya ini: [tempel balasan + handle]

Mode 2 (postingan orang lain):
/threads-skill:threads-balas tulis balasan buat postingan @[akun] ini: [tempel postingan]
```

### Contoh

1. ```
   /threads-skill:threads-balas sortir 40 balasan ini, bilang jumlah per
   kelompok: [tempel]
   ```
2. ```
   /threads-skill:threads-balas ada yang nyinyir "kopi literan pasti pakai
   pengawet". Balas gimana?
   ```
3. ```
   /threads-skill:threads-balas pertanyaan "tahan berapa hari di kulkas?"
   ditanya 23 orang. Jadikan postingan baru
   ```
4. ```
   /threads-skill:threads-balas ada calon pembeli nanya buat acara kantor
   50 orang. Balas di depan umum dengan satu tawaran bantuan
   ```
5. ```
   /threads-skill:threads-balas tulis 2 pilihan balasan buat postingan
   @akun soal harga jasa, saya punya pengalaman naikin harga 40%
   ```
6. ```
   /threads-skill:threads-balas ronde engage: ini 8 postingan dari daftar
   engage saya, satu balasan per postingan: [tempel]
   ```
7. ```
   /threads-skill:threads-balas mau quote postingan ini dengan data saya
   sendiri, bukan cuma setuju: [tempel]
   ```
8. ```
   /threads-skill:threads-balas balasan ini kasar dan menyerang pribadi.
   Perlu dibalas nggak?
   ```

### Studi kasus: Rina dan si penuduh pengawet

**Balasan masuk di postingan Rina:**

> "Kopi literan pasti pakai pengawet, mana mungkin tahan 5 hari."

**Hasil:**

```
SORTIR  ·  1 balasan  ·  ISI (pengkritik)

Akui yang benar dulu, lalu pegang posisi, sekali saja:

Wajar curiga, kebanyakan kopi literan memang nggak tahan lama. Punya saya
tahan 5 hari karena susunya UHT dan botolnya disterilkan air panas, bukan
pengawet. Tanggal produksinya saya tulis di botol biar bisa dicek sendiri.
```

**Pelajaran.**
- Nggak defensif, nggak hapus komentar, cuma satu balasan.
- Jawaban di depan umum ini sekaligus jadi bahan postingan baru kalau
  pertanyaan sejenis datang lagi.

---

## 10. threads-dm

### Pola

```
/threads-skill:threads-dm tulis DM ke @[akun]. Pemicunya: [apa yang dia
lakukan]. Yang saya mau: [obrolan / jual / kolaborasi]. Kirim lewat [Threads / IG]
```

### Contoh

1. ```
   /threads-skill:threads-dm 31 orang komen "TEMPLATE". Tulis DM kiriman
   kata kuncinya, link: [link]
   ```
2. ```
   /threads-skill:threads-dm @akun sudah 3 minggu saya balas postingannya,
   dia punya kafe. Pesan pertama, tanpa jualan
   ```
3. ```
   /threads-skill:threads-dm ajak kolaborasi @akun: saya kopi literan,
   dia roti. Bikin paket sarapan kantor
   ```
4. ```
   /threads-skill:threads-dm tulis 2 tindak lanjut untuk DM kemarin yang
   belum dibalas, hari ke-4 dan ke-10
   ```
5. ```
   /threads-skill:threads-dm pendekkan DM ini jadi maksimal 4 kalimat:
   [tempel]
   ```
6. ```
   /threads-skill:threads-dm dia jawab polling "buat kantor". Tulis DM
   pertama yang nawarin bantuan, bukan katalog
   ```
7. ```
   /threads-skill:threads-dm saya mau DM 50 owner kafe yang nggak kenal saya.
   Layak nggak?
   ```
8. ```
   /threads-skill:threads-dm periksa DM ini, ada bagian yang kerasa
   spam nggak? [tempel]
   ```

### Studi kasus: Bayu dan 31 komentar "TEMPLATE"

**Situasi.** Bayu posting "komen TEMPLATE, saya kirim template brief video".
31 orang komen.

**Hasil:**

```
{nama}, ini dia: example.com/template-brief

Isi kolom "3 detik pertama" duluan, sisanya gampang.

Kamu biasanya bikin video buat jualan atau buat personal branding?
```

```
tindak lanjut: tidak ada. Ini kiriman kata kunci, bukan outreach.
Kalau dia membalas pertanyaannya, baru lanjut ngobrol.
```

**Pelajaran.**
- Barang dikirim **di pesan pertama**, tanpa syarat.
- Pertanyaannya bisa dijawab dengan 4 kata.
- Bayu pakai fitur balasan otomatis resmi untuk kata kunci. Itu boleh. Yang
  nggak boleh: DM massal ke orang yang nggak komen.

---

## 11. threads-profil

### Pola

```
/threads-skill:threads-profil cek profil saya. Tujuan akun: [follower /
jualan / klien / otoritas]. [lampirkan screenshot profil + 1 layar gulir]
```

### Contoh

1. ```
   /threads-skill:threads-profil skor profil saya dari 100: [screenshot]
   ```
2. ```
   /threads-skill:threads-profil kasih 3 pilihan nama, format
   "Nama, kata yang dicari", maksimal 30 karakter
   ```
3. ```
   /threads-skill:threads-profil tulis ulang bio saya, maksimal 150
   karakter: [bio lama]
   ```
4. ```
   /threads-skill:threads-profil dari hasil audit, postingan mana yang
   harus saya sematkan?
   ```
5. ```
   /threads-skill:threads-profil saya punya 4 link. Mana yang dipakai?
   ```
6. ```
   /threads-skill:threads-profil view saya naik tapi follower nggak.
   Cek profilnya dulu
   ```
7. ```
   /threads-skill:threads-profil lima postingan teratas saya campur aduk,
   apa yang harus diposting dulu sebelum dorong orang ke profil?
   ```
8. ```
   /threads-skill:threads-profil skor ulang setelah saya ganti nama
   dan bio
   ```

### Studi kasus: profil Sari

**Profil lama:**

```
Nama:   Sari
Bio:    Ibu rumah tangga | pecinta masak | affiliate 🛒✨🍳
Link:   linktr.ee/sari (7 link)
Sematan: tidak ada
```

**Skor:**

```
SKOR PROFIL  38/100

  nama              3/12   nama saja, tidak ada kata yang dicari
  bio baris 1       4/14   deretan identitas, bukan untuk siapa
  disematkan        0/14   tidak ada
  link              3/10   7 link, jadi menu
  ...
```

**Tulis ulang, urut dari poin terbesar:**

```
1. Sematkan: album "14 hari, Rp 2.317.000" (postingan terbaiknya)
2. Nama:  Sari, Alat Dapur Murah
3. Bio:   Alat dapur di bawah Rp 100 rb yang beneran kepakai.
          Diuji di dapur sendiri, bukan cuma unboxing.
4. Link:  satu, ke etalase affiliate
```

```
SKOR ULANG  71/100
Sisanya: lima postingan teratas belum satu niche. Posting 3 album alat dapur
dulu sebelum mendorong orang ke profil.
```

**Pelajaran.** Skor naik dari 38 ke 71, bukan 98. Sisanya bukan soal
kata-kata, tapi soal isi akun. Claude bilang terus terang.

---

## 12. threads-repurpose

### Pola

```
/threads-skill:threads-repurpose ubah [jenis sumber] ini jadi postingan
Threads [seminggu / N postingan]: [tempel transkrip / artikel / link]
```

### Contoh

1. ```
   /threads-skill:threads-repurpose transkrip video YouTube 18 menit ini
   jadi seminggu postingan: [tempel]
   ```
2. ```
   /threads-skill:threads-repurpose artikel blog ini jadi 1 album dan
   2 postingan teks: [tempel]
   ```
3. ```
   /threads-skill:threads-repurpose daftar temuannya dulu, jangan langsung
   ditulis: [tempel]
   ```
4. ```
   /threads-skill:threads-repurpose postingan LinkedIn ini, buang semua
   sisa LinkedIn-nya: [tempel]
   ```
5. ```
   /threads-skill:threads-repurpose rekaman live 1 jam ini, cari momen
   yang bisa jadi klip video 30 detik: [transkrip + menit]
   ```
6. ```
   /threads-skill:threads-repurpose naskah Reels saya ini, ubah jadi
   postingan teks Threads: [tempel]
   ```
7. ```
   Tulis Selasa
   ```
8. ```
   /threads-skill:threads-repurpose podcast ini temuannya cuma 3. Tetap
   jadikan 5 postingan?
   ```

### Studi kasus: Bayu dan video YouTube 18 menit

**Sumber.** Video YouTube Bayu, "Cara saya edit video jualan pakai AI",
18 menit.

**Temuan:**

```
TEMUAN  4 klaim, 7 angka, 2 cerita, 3 cara kerja, 1 kesalahan, 5 kalimat kutipan
```

**Minggu:**

```
SEL  TEKS   #2  Perintah Larangan   Berhenti kirim file mentah ke klien
RAB  ALBUM  #13 Sebelum Sesudah     Video yang sama, 3 detik pertama dipoles
JUM  UTAS   #15 Catatan Gagal       Klien yang batal karena revisi ke-5
MIN  VIDEO  #5  Waktu Dipangkas     Klip menit 06:40: potong jeda pakai AI, 5 jam jadi 2 jam

Bilang "tulis Selasa" dan saya buatkan drafnya.
```

**Pelajaran.**
- Satu video jadi empat postingan dengan empat rumus berbeda, bukan
  ringkasan video.
- Nggak ada satu pun yang bilang "di video terbaru saya". Postingan
  berdiri sendiri.
- Klip asli Bayu (menit 06:40) dipakai, bukan direkam ulang.

---

## 13. Alur gabungan: satu minggu Rina

Begini kalau semua skill dipakai bareng dalam satu minggu.

| Hari | Yang dilakukan Rina | Skill |
| --- | --- | --- |
| Minggu malam | audit 12 postingan terakhir | `threads-audit` |
| Minggu malam | susun minggu depan dari hasil audit | `threads-plan` |
| Senin pagi | ronde engage 20 menit | `threads-balas` (mode 2) |
| Senin sore | tulis album 85 botol | `threads-album` + `threads-hook` + `threads-human` |
| Senin 19.00 | posting, lalu balas di jam pertama | `threads-balas` (mode 1) |
| Selasa | pertanyaan "tahan berapa hari?" ditanya 23 orang | `threads-balas` jadi postingan baru |
| Rabu | album endorse Rp 1,2 juta | `threads-album` |
| Kamis | polling, balas yang jawab "buat kantor" | `threads-post` + `threads-dm` |
| Jumat | album aren lawan pandan | `threads-album` |
| Sabtu | perbaiki profil, sematkan album terbaik | `threads-profil` |
| Minggu | ubah video TikTok lamanya jadi bahan minggu depan | `threads-repurpose` |

> 📌 **INGAT**: urutannya selalu **ukur, rencanakan, tulis, rapikan, posting,
> balas**. Kalau kamu cuma punya waktu untuk satu skill, pakai
> `threads-audit` dulu. Semua yang lain jadi lebih tepat setelah kamu tahu
> apa yang beneran jalan di akunmu.
