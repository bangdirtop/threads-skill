# threads-skill Buat yang Nggak Mau Ribet

### Buku panduan santai untuk 12 skill Claude yang bantu kamu nulis, ngukur, dan ngatur konten Threads

---

## Daftar Isi

- [Pengantar](#pengantar)
- **Bagian 1: Kenalan Dulu**
  - [Bab 1. Skill Itu Apa, Sih?](#bab-1-skill-itu-apa-sih)
  - [Bab 2. Pasang dalam 5 Menit](#bab-2-pasang-dalam-5-menit)
  - [Bab 3. Ajari Claude Cara Kamu Ngomong](#bab-3-ajari-claude-cara-kamu-ngomong)
- **Bagian 2: Nulis Postingan yang Dibaca Orang**
  - [Bab 4. Baris Pertama Adalah Segalanya (threads-hook)](#bab-4-baris-pertama-adalah-segalanya-threads-hook)
  - [Bab 5. Satu Postingan, 500 Karakter (threads-post)](#bab-5-satu-postingan-500-karakter-threads-post)
  - [Bab 6. Kalau Nggak Muat: Utas (threads-utas)](#bab-6-kalau-nggak-muat-utas-threads-utas)
  - [Bab 7. Bukti Pakai Gambar: Album (threads-album)](#bab-7-bukti-pakai-gambar-album-threads-album)
  - [Bab 8. Biar Nggak Kayak Tulisan Robot (threads-human)](#bab-8-biar-nggak-kayak-tulisan-robot-threads-human)
- **Bagian 3: Ngukur, Bukan Nebak**
  - [Bab 9. Bedah Akun Sendiri (threads-audit)](#bab-9-bedah-akun-sendiri-threads-audit)
  - [Bab 10. Intip yang Lagi Jalan (threads-viral)](#bab-10-intip-yang-lagi-jalan-threads-viral)
  - [Bab 11. Rencana Seminggu (threads-plan)](#bab-11-rencana-seminggu-threads-plan)
- **Bagian 4: Ngobrol Sama Manusia**
  - [Bab 12. Balas-balasan (threads-balas)](#bab-12-balas-balasan-threads-balas)
  - [Bab 13. DM yang Dibalas (threads-dm)](#bab-13-dm-yang-dibalas-threads-dm)
  - [Bab 14. Profil yang Bikin Orang Follow (threads-profil)](#bab-14-profil-yang-bikin-orang-follow-threads-profil)
  - [Bab 15. Satu Konten Jadi Seminggu (threads-repurpose)](#bab-15-satu-konten-jadi-seminggu-threads-repurpose)
- **Bagian 5: Serba Sepuluh**
  - [Bab 16. 10 Kesalahan yang Paling Sering](#bab-16-10-kesalahan-yang-paling-sering)
  - [Bab 17. 10 Perintah Siap Salin](#bab-17-10-perintah-siap-salin)
- **Lampiran**
  - [A. Kamus Istilah](#lampiran-a-kamus-istilah)
  - [B. 26 Rumus Hook dalam Satu Tabel](#lampiran-b-26-rumus-hook-dalam-satu-tabel)
  - [C. Kalau Ada yang Error](#lampiran-c-kalau-ada-yang-error)
  - [D. Contekan Satu Halaman](#lampiran-d-contekan-satu-halaman)

---

## Pengantar

### Tentang buku ini

Kamu punya akun Threads. Kamu pakai Claude. Kamu pengin postinganmu dibaca
lebih banyak orang, tanpa harus jadi ahli algoritma dan tanpa harus nulis
kayak robot.

Buku ini menjelaskan cara pakai **threads-skill**, kumpulan 12 skill yang
bikin Claude bisa jadi copywriter, analis, dan perencana konten Threads kamu.
Nggak perlu dibaca urut. Lompat aja ke bab yang kamu butuhkan.

Mau langsung lihat contoh? Buku pendampingnya, [CONTOH.md](CONTOH.md),
berisi pola perintah, 8 contoh siap salin, dan satu studi kasus utuh untuk
tiap skill.

### Asumsi saya tentang kamu

Saya anggap kamu:

- Punya akun Threads, dan pernah posting paling tidak beberapa kali.
- Sudah pasang Claude Code (di terminal atau di aplikasi desktop Claude).
- Bisa salin-tempel perintah. Itu saja. Nggak perlu bisa coding.

Kalau kamu belum pernah posting sama sekali, nggak apa-apa. Bagian 2 tetap
jalan. Bagian 3 (ngukur) baru berguna setelah kamu punya sekitar 20 postingan.

### Ikon di buku ini

> 💡 **TIPS**: jalan pintas atau trik yang bikin kerjaan lebih cepat.

> 📌 **INGAT**: hal penting yang bakal kepakai terus. Kalau cuma mau
> ingat satu hal dari sebuah bab, ingat yang ini.

> ⚠️ **AWAS**: hal yang bisa bikin postinganmu jelek, akunmu dibatasi,
> atau kamu malu di depan umum.

> 🤓 **TEKNIS**: penjelasan di balik layar. Boleh dilewati.

### Mulai dari mana?

| Kalau kamu... | Mulai dari |
| --- | --- |
| Belum pasang apa-apa | Bab 2 |
| Mau langsung nulis postingan hari ini | Bab 5 |
| Postinganmu sepi dan nggak tahu kenapa | Bab 9 |
| Bingung mau posting apa minggu ini | Bab 11 |
| Cuma mau contekan | Lampiran D |

---

# Bagian 1: Kenalan Dulu

## Bab 1. Skill Itu Apa, Sih?

**Di bab ini:**
- Apa bedanya Claude biasa dan Claude yang pakai skill
- 12 skill dalam satu tabel
- Aturan main yang berlaku di semua skill

### Claude biasa vs Claude pakai skill

Claude biasa itu pintar, tapi umum. Kalau kamu minta "bikinin postingan
Threads soal jualan online", hasilnya bisa saja rapi, tapi rasanya kayak
iklan bank.

Skill itu **buku resep** yang dibaca Claude sebelum kerja. Isinya aturan,
langkah, dan alat ukur. Jadi Claude nggak cuma nulis, tapi juga:

- milih rumus pembuka yang terbukti,
- ngasih skor ke baris pertama,
- buang kata-kata yang bikin tulisan kerasa AI,
- ngecek batas 500 karakter,
- dan nolak ngarang angka.

### 12 skill dalam satu tabel

| Skill | Gampangnya | Pakai saat |
| --- | --- | --- |
| `threads-hook` | tukang bikin kalimat pembuka | butuh baris pertama yang bikin orang berhenti |
| `threads-post` | penulis postingan tunggal | mau posting satu teks, dengan atau tanpa 1 gambar |
| `threads-utas` | penulis rangkaian postingan | idenya kepanjangan buat 500 karakter |
| `threads-album` | perancang album | punya bukti visual: screenshot, sebelum/sesudah |
| `threads-human` | penghapus jejak robot | sebelum apa pun diposting |
| `threads-audit` | dokter akun | mau tahu postingan mana yang beneran jalan |
| `threads-viral` | mata-mata niche | mau tahu apa yang lagi jalan di akun lain |
| `threads-plan` | perencana mingguan | bingung mau posting apa minggu ini |
| `threads-balas` | penjaga kolom balasan | banyak balasan masuk, atau mau balas postingan orang |
| `threads-dm` | penulis pesan pribadi | mau DM orang tanpa terkesan spam |
| `threads-profil` | penata profil | orang mampir tapi nggak follow |
| `threads-repurpose` | tukang daur ulang | punya video, podcast, atau artikel panjang |

### Aturan main yang berlaku di semua skill

1. **Nggak ada yang diposting otomatis.** Skill cuma nulis. Kamu yang
   posting.
2. **Angka nggak pernah dikarang.** Kalau Claude butuh angka yang belum
   kamu kasih, dia nulis `{{angka}}` dan nanya.
3. **Em dash dilarang total.** Tanda pisah panjang itu salah satu ciri
   tulisan AI yang paling gampang dikenali. Di sini, satu pun nggak boleh.
4. **Ukur pakai akun sendiri.** Aturan umum cuma tebakan awal. Data akunmu
   yang menang.
5. **Tiru rumusnya, bukan postingannya.** Bentuk boleh diambil, kalimat
   orang jangan.

> 📌 **INGAT**: kalau cuma ingat satu aturan, ingat nomor 2. Satu angka
> palsu yang ketahuan di kolom balasan bisa ngabisin kepercayaan yang
> dibangun berbulan-bulan.

---

## Bab 2. Pasang dalam 5 Menit

**Di bab ini:**
- Dua cara pasang
- Bikin folder data
- Cek apakah sudah jalan

### Cara 1: sebagai plugin (disarankan)

Buka terminal, jalankan dua perintah ini satu per satu:

```bash
claude plugin marketplace add bangdirtop/threads-skill
```

```bash
claude plugin install threads-skill@threads-skill
```

Tutup lalu buka lagi Claude Code. Selesai.

> 💡 **TIPS**: kalau nanti ada versi baru, perbarui dengan:
> `claude plugin marketplace update threads-skill` lalu
> `claude plugin update threads-skill@threads-skill`.

### Cara 2: salin langsung

Kalau cara 1 gagal, salin folder skill-nya ke folder skill Claude:

```bash
git clone https://github.com/bangdirtop/threads-skill.git
```

```bash
cp -R threads-skill/skills/* ~/.claude/skills/
```

### Bikin folder data

Skill menyimpan catatan kamu (gaya bicara, rencana, hasil riset, log
postingan) di satu folder:

```bash
mkdir -p ~/.claude/threads
```

```bash
cp threads-skill/templates/voice.md ~/.claude/threads/voice.md
```

Isi folder ini nanti kira-kira begini:

| File | Isinya | Ditulis oleh |
| --- | --- | --- |
| `voice.md` | cara kamu ngomong | kamu, atau Claude dari contoh postinganmu |
| `plan.md` | rencana minggu ini | `threads-plan` |
| `swipe.md` | rumus yang lagi jalan di niche | `threads-viral` |
| `log.md` | catatan postingan yang sudah ditulis | `threads-post`, `threads-utas` |
| `audit/` | hasil bedah akun | `threads-audit` |

### Cek sudah jalan atau belum

Di Claude, ketik:

```
/threads-skill:threads-hook
```

Kalau Claude merespons dengan cara kerja skill hook, berarti terpasang.

> 🤓 **TEKNIS**: kalau dipasang sebagai plugin, nama skill diawali
> `threads-skill:`. Kalau disalin langsung (cara 2), cukup `/threads-hook`.
> Kamu juga bisa nggak pakai garis miring sama sekali. Cukup bilang
> "bikinin hook buat..." dan Claude biasanya milih skill yang cocok sendiri.

---

## Bab 3. Ajari Claude Cara Kamu Ngomong

**Di bab ini:**
- Kenapa `voice.md` penting banget
- Cara paling gampang ngisinya

### Kenapa penting

Postingan yang bagus tapi nggak kedengeran kayak kamu itu sama aja nggak
bisa dipakai. Follower kamu kenal cara kamu ngomong. Kalau tiba-tiba kamu
nulis "Mari kita selami bersama", mereka langsung curiga.

`voice.md` adalah catatan cara kamu ngomong: pakai "saya", "aku", atau
"gue", suka huruf kecil semua atau nggak, emoji berapa, kata apa yang kamu
benci, dan angka apa saja yang boleh dipakai.

### Cara paling gampang

Jangan isi manual. Kirim tiga postingan Threads kamu yang paling "kamu
banget" ke Claude, lalu bilang:

```
Tulis voice.md saya dari tiga postingan ini.
```

Claude akan mengisi file itu. Kamu tinggal baca dan koreksi.

> 📌 **INGAT**: bagian **"Bukti yang boleh dipakai"** di `voice.md` itu
> yang paling sering kepakai. Isi dengan angka dan cerita nyata yang kamu
> rela taruh nama kamu di atasnya. Kalau kosong, setiap draf bakal penuh
> `{{angka}}`.

> ⚠️ **AWAS**: jangan taruh password, nomor rekening, atau data pribadi
> pelanggan di `voice.md`. File ini dibaca setiap kali Claude nulis.

---

# Bagian 2: Nulis Postingan yang Dibaca Orang

## Bab 4. Baris Pertama Adalah Segalanya (threads-hook)

**Di bab ini:**
- Kenapa baris pertama menentukan nasib postingan
- 26 rumus pembuka
- Cara ngasih skor ke hook

### Kenapa baris pertama

Orang di Threads menggulir cepat. Mereka baca satu baris, lalu memutuskan:
berhenti atau lanjut. Baris pertama itu satu-satunya kesempatanmu.

Baris pertama yang lemah biasanya:
- dibuka sapaan ("Halo warga Threads"),
- dibuka basa-basi ("Di utas ini aku mau share"),
- nggak ada angka, nama, atau hal konkret,
- isi pentingnya baru muncul di ujung kalimat.

### 26 rumus pembuka

Skill ini punya 26 rumus. Contoh tiga yang paling sering kepakai:

| No | Rumus | Pola | Contoh |
| --- | --- | --- | --- |
| 3 | Tidak Ada yang Bilang | Tidak ada yang bilang kalau {kenyataan pahit}. | Tidak ada yang bilang kalau 20 postingan pertamamu memang akan sepi. |
| 5 | Waktu Dipangkas | Dulu {pekerjaan} butuh {lama}. Sekarang {singkat}. | Dulu bikin satu video butuh 2 hari. Sekarang 40 menit. |
| 6 | Bukti Angka | Saya {melakukan hal} selama {N hari}. Ini angka aslinya. | Saya posting album 8 hari berturut-turut. Ini angka aslinya. |

Daftar lengkapnya ada di [Lampiran B](#lampiran-b-26-rumus-hook-dalam-satu-tabel).

### Cara pakai

Bilang ke Claude:

```
/threads-skill:threads-hook bikinin 3 hook buat postingan soal
saya berhenti pasang iklan dan omzet tetap naik 18% bulan ini
```

Claude akan menulis tiga kandidat dari tiga rumus berbeda, lalu ngasih skor.

```
HOOK (diurutkan)
   85  KUAT   Iklan saya matikan bulan ini. Omzet malah naik 18%.
   55  OKE    Berhenti bakar uang di iklan. Ini yang saya lakukan.
             tidak ada angka, nama, atau durasi
   32  LEMAH  Akhirnya saya sadar sesuatu soal iklan.
             tidak ada angka, nama, atau durasi; tidak ada yang dipertaruhkan
```

Perhatikan catatan di bawah tiap hook. Itu petunjuk cara benerinnya: hook
nomor dua cukup ditambah angka.

| Skor | Label | Artinya |
| --- | --- | --- |
| 70 ke atas | KUAT | layak dipakai |
| 50 sampai 69 | OKE | bisa, tapi coba cari yang lebih tajam |
| di bawah 50 | LEMAH | jangan dipoles, ganti rumus atau tambah bahan |

> 💡 **TIPS**: ada postingan orang yang rame dan kamu penasaran kenapa?
> Tempel teksnya, lalu bilang "bongkar postingan ini". Claude akan bilang
> rumus apa yang dipakai, kenapa jalan, dan ngasih templat kosong buat
> kamu isi dengan ceritamu sendiri.

> ⚠️ **AWAS**: skor ini menyaring hook yang jelek, bukan meramal mana yang
> bakal viral. Di antara dua hook yang sama-sama KUAT, data akunmu sendiri
> (Bab 9) yang lebih jujur.

---

## Bab 5. Satu Postingan, 500 Karakter (threads-post)

**Di bab ini:**
- Bentuk postingan yang jalan
- Pilih tujuan dulu, baru nulis
- Aturan khusus Threads

### Bentuknya

```
Baris 1     klaim, angka, atau pertanyaan nyata
Isi         1 sampai 4 kalimat pendek, satu baris kosong di antaranya
Ajakan      SATU: repost, simpan, balas, atau klik
Tag topik   SATU, di akhir (atau tidak sama sekali)
```

Batasnya 500 karakter. Lebih dari itu, pindah ke utas (Bab 6) atau album
(Bab 7).

### Pilih tujuan dulu

| Kamu mau orang... | Bentuk yang cocok |
| --- | --- |
| nyebarin (repost, share) | opini tajam, angka yang mengejutkan |
| nyimpen | cara, template, daftar pendek |
| bales | pertanyaan nyata, pengalaman yang bisa dibandingkan |
| follow | bukti dengan angka, cerita gagal yang jujur |
| klik link | tenggat nyata, hal baru |

> 📌 **INGAT**: balasan banyak belum tentu menyebar. Postingan "kalian tim
> A atau B?" bisa rame banget di kolom balasan, tapi nggak ada yang
> repost. Kalau mau dilihat orang baru, kejar repost dan share, bukan
> jumlah komentar.

### Aturan khusus Threads

- **Satu tag topik per postingan.** Bukan dinding tagar kayak di Instagram.
- **Link bisa diklik.** Nggak perlu bilang "link di bio".
- **Polling** boleh, maksimal 4 pilihan, berlaku 24 jam.
- **Gambar membantu.** Satu screenshot bukti lebih meyakinkan daripada
  kalimat "percaya deh".

### Cara pakai

```
/threads-skill:threads-post tulis postingan soal jualan kopi literan saya
yang naik dari 20 ke 85 botol sehari setelah botolnya saya kasih tanggal
produksi tulisan tangan. Tujuannya biar disimpan.
```

Claude akan: pilih tujuan, bikin 3 hook dan skornya, tulis postingan,
bersihkan pakai `threads-human`, cek pakai linter, lalu kasih hasil:

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

Postingan lengkapnya ada di [CONTOH.md](CONTOH.md#2-threads-post).

Tinggal salin, tempel di Threads, posting.

> 💡 **TIPS**: mau ngecek postingan yang kamu tulis sendiri? Simpan ke file
> `draf.txt`, lalu bilang "cek draf ini pakai lint_post". Linter akan
> bilang GAGAL (wajib dibetulkan), AWAS (kamu putuskan), atau SIAP.

---

## Bab 6. Kalau Nggak Muat: Utas (threads-utas)

**Di bab ini:**
- Kapan pakai utas, kapan bukan
- Aturan postingan pertama

### Kapan utas

| Isi | Pakai |
| --- | --- |
| langkah-langkah, cerita beberapa babak, argumen panjang | utas |
| bukti visual (screenshot, grafik, sebelum/sesudah) | album (Bab 7) |
| satu klaim | satu postingan (Bab 5) |

### Bentuknya

```
1          HOOK      bernilai walaupun orang berhenti di sini
2          TARUHAN   kenapa ini penting buat pembaca
3 sampai N-1  ISI    satu gagasan per postingan
N          PENUTUP   ringkasan + satu ajakan + link (kalau ada)
```

Panjang ideal 4 sampai 8 postingan.

> 📌 **INGAT**: kebanyakan orang cuma baca postingan pertama. Tes
> sederhananya: kalau orang berhenti di postingan 1, apakah mereka tetap
> dapat sesuatu? Kalau nggak, tulis ulang.

> ⚠️ **AWAS**: "Utas di bawah 👇" bukan hook. Itu petunjuk arah.

> 🤓 **TEKNIS**: linter bisa ngecek utas sekaligus. Pisahkan tiap postingan
> dengan baris berisi `---` saja. Linter akan ngecek batas 500 karakter per
> postingan dan ngingetin kalau ada link di postingan pertama.

---

## Bab 7. Bukti Pakai Gambar: Album (threads-album)

**Di bab ini:**
- Kenapa album sering jadi format paling menyebar
- Susunan slide
- Video di Threads

### Kenapa album

Teks bikin orang berhenti. Gambar bikin orang percaya. Untuk akun yang
jualan keahlian, album berisi bukti nyata (screenshot insight, hasil kerja,
sebelum dan sesudah) sering jadi format yang paling jauh menyebar.

### Susunan slide

```
Teks       pengantar, aturan Bab 5 berlaku penuh
Slide 1    SAMPUL: janji dalam 6 kata, huruf besar
Slide 2    BUKTI TERKUAT (taruh di depan!)
Slide 3..  satu hal per slide, maksimal 25 kata
Slide N-1  RINGKASAN: semuanya dalam satu slide
Slide N    AJAKAN: satu saja
```

Ideal 4 sampai 10 slide. Ukuran gambar 1080x1350.

> 💡 **TIPS**: screenshot asli lebih kuat daripada desain ulang yang cantik.
> Orang percaya sama yang kelihatan "mentah".

> 💡 **TIPS**: kasih nomor di tiap slide (3/8). Orang lebih mau menggeser
> sampai habis kalau tahu ujungnya di mana.

> ⚠️ **AWAS**: sensor data pribadi orang lain di screenshot. Nama
> pelanggan, nomor HP, alamat.

### Video

Video di Threads jalan otomatis tanpa suara. Jadi:
- frame pertama harus bergerak dan ada teks besar,
- teks terbakar di video untuk yang diucapkan,
- 15 sampai 45 detik, satu ide per video.

### Cara pakai

```
/threads-skill:threads-album bikinin album dari screenshot
omzet 3 bulan terakhir ini, tujuannya biar orang nyimpen
```

Claude akan kasih **teks slide dulu** sebagai daftar. Kamu baca, koreksi,
baru setelah kamu setuju gambarnya dibikin.

---

## Bab 8. Biar Nggak Kayak Tulisan Robot (threads-human)

**Di bab ini:**
- Ciri tulisan AI yang paling gampang ketahuan
- Apa yang dibetulkan otomatis, apa yang harus kamu tulis ulang
- Cara baca skornya

### Ciri tulisan AI

| Ciri | Contoh |
| --- | --- |
| Em dash | "AI bukan alat (tanda pisah panjang) tapi partner" |
| Kata klise | di era digital ini, krusial, signifikan, komprehensif, menyelami |
| "Bukan sekadar X, tapi Y" | "Ini bukan sekadar alat, tapi partner" |
| Tanya jawab sendiri | "Hasilnya? Luar biasa." |
| Tumpukan pendek | "Cepat. Murah. Efektif." |
| Pengumuman kejujuran | "Jujur aja ya...", "Real talk:" |
| Pancingan refleks | "Jangan lupa follow!", "Repost kalau setuju!" |

### Yang dibetulkan otomatis

- Em dash dan en dash, semuanya, tanpa kecuali
- Karakter tak terlihat (iya, ada karakter yang nggak kelihatan di layar
  tapi ikut tersalin dari hasil AI)
- Kata-kata klise, diganti kata biasa atau dihapus

### Yang harus ditulis ulang

Pola kalimat (baris 3 sampai 7 di tabel atas) cuma **ditandai**. Claude atau
kamu yang menulis ulang, karena ngubah bentuk kalimat butuh rasa.

### Skornya

Lima pemeriksaan, masing-masing 0 sampai 100:

| Cek | Pertanyaannya |
| --- | --- |
| VARIASI | panjang kalimatnya beda-beda atau seragam kayak mesin? |
| KONKRET | ada angka, nama, tanggal? |
| SLOP | banyak kata klise? |
| JEJAK | ada em dash atau karakter aneh? |
| SUARA | kedengeran kayak orang ngomong, atau kayak rilis pers? |

**LOLOS** kalau skor 70 ke atas dan nggak ada satu pemeriksaan pun di bawah
55. **Satu em dash = GAGAL**, berapa pun skornya.

### Cara pakai

```
/threads-skill:threads-human rapikan ini biar nggak kayak AI:
[tempel teksnya]
```

> 📌 **INGAT**: skill lain sudah otomatis memanggil `threads-human` sebelum
> nunjukin hasil. Kamu baru perlu manggil manual untuk teks yang kamu tulis
> sendiri atau dari tempat lain.

> ⚠️ **AWAS**: skor ini dihitung di komputermu sendiri. Ini bukan GPTZero
> atau detektor AI lainnya, dan nggak bisa menjamin lolos dari detektor
> mana pun. Yang dijaga di sini adalah pembaca manusia.

---

# Bagian 3: Ngukur, Bukan Nebak

## Bab 9. Bedah Akun Sendiri (threads-audit)

**Di bab ini:**
- Kenapa jumlah view itu angka paling menipu
- Tiga angka yang benar-benar penting
- Cara baca hasil audit

### Kenapa view menipu

Akun dengan 500 ribu follower yang dapat 100 ribu view itu lagi sepi. Akun
dengan 3 ribu follower yang dapat 100 ribu view itu nemu sesuatu. View
mentah kebanyakan cuma menggambarkan seberapa besar akunmu, bukan seberapa
bagus postingannya.

### Tiga angka yang penting

| Angka | Cara hitung | Artinya |
| --- | --- | --- |
| **Kelipatan** | view postingan dibagi median view akun | 1x = hari biasa, 3x ke atas = hit |
| **Sebaran** | (repost + quote + share) per 1.000 view | orang mau naruh namanya di postingan itu. Sinyal terkuat |
| **Balasan** | balasan per 1.000 view | memancing obrolan, tapi belum tentu menyebar |

> 🤓 **TEKNIS**: median itu angka tengah. Kalau view 10 postinganmu
> diurutkan, median adalah angka di tengah-tengahnya. Dipakai karena satu
> postingan viral nggak bikin median ikut melonjak, beda dengan rata-rata.

### Cara pakai

Kasih datanya dengan salah satu cara:
- screenshot insight per postingan,
- daftar postingan plus view-nya,
- atau minta Claude narik sendiri kalau kamu punya konektor seperti Repliz.

```
/threads-skill:threads-audit akun @namaakun
```

### Cara baca hasilnya

```
5 TERATAS (kelipatan)
  12,4x  album bukti      14.300 view  sebaran 7,2/1k
5 TERBAWAH
   0,4x  luar niche          460 view  sebaran 0,0/1k

STOP: postingan luar niche.
PERBANYAK: album bukti dengan angka.
```

Baca dua baris terakhir dulu. Itu kesimpulannya.

> 📌 **INGAT**: postingan yang dapat view tapi nggak dapat follower bukan
> postingan gagal. Itu tanda **profilmu** yang perlu dibetulkan (Bab 14).
> Postingan yang nggak dapat view itu masalah **baris pertama** (Bab 4).

> ⚠️ **AWAS**: dengan 6 postingan, belum ada pola. Dengan 30, mulai
> kelihatan. Kalau Claude bilang "belum cukup data", itu bukan malas, itu
> jujur.

> 💡 **TIPS**: jam posting hampir nggak pernah jadi penyebab. Audit
> ngeceknya paling akhir. Kalau kamu masih sibuk ngatur jam padahal baris
> pertamamu lemah, kamu lagi memoles hal yang salah.

---

## Bab 10. Intip yang Lagi Jalan (threads-viral)

**Di bab ini:**
- Cara milih akun yang pantas dicontek rumusnya
- Swipe file itu apa

### Pilih akunnya

6 sampai 12 akun, ukurannya paling jauh 10 kali akunmu:
- **4 langsung**: niche sama, sedikit di depanmu.
- **4 tetangga**: niche beda, penontonnya sama.
- **2 sampai 4 besar**: cuma buat lihat format.

### Swipe file

Swipe file adalah catatan postingan orang yang jalan, diurutkan pakai
kelipatan (bukan view), lengkap dengan nama rumusnya. Disimpan di
`~/.claude/threads/swipe.md`, lalu dibaca otomatis oleh `threads-post` dan
`threads-plan`.

### Cara pakai

```
/threads-skill:threads-viral riset niche jualan online pakai AI,
ini akun yang mau saya pantau: @akun1 @akun2 @akun3
```

> ⚠️ **AWAS**: jangan pernah kasih password Threads atau Instagram ke
> siapa pun, termasuk ke Claude. Skill ini membaca dengan kecepatan
> manusia, bukan nyedot data massal. Scraping massal melanggar aturan Meta
> dan bisa bikin akun dibatasi.

> 📌 **INGAT**: tiru rumusnya, bukan postingannya. Hasil akhir skill ini
> adalah baris pertama versi **kamu**, dengan cerita dan angka kamu.

---

## Bab 11. Rencana Seminggu (threads-plan)

**Di bab ini:**
- Campuran tipe postingan dalam seminggu
- Ronde engage 20 menit

### Campurannya

| Tipe | Berapa kali | Isinya |
| --- | --- | --- |
| Bukti | 1 sampai 2 | kejadian nyata dengan angka |
| Ajar | 1 sampai 2 | satu hal yang bisa dipakai hari ini |
| Opini | 1 | sikap yang bikin sebagian orang nggak setuju |
| Cerita | 1 per dua minggu | adegan dengan harga yang dibayar |
| Tawaran | 1 per dua minggu | yang kamu jual, terang-terangan |
| Obrolan | 1 | polling atau pertanyaan nyata |

Kalau audit (Bab 9) bilang satu format jauh lebih jalan di akunmu, rencana
akan dibangun di sekitar format itu.

### Ronde engage

20 menit sehari, **sebelum** posting. Daftar 10 akun:
- 5 akun besar yang penontonnya kamu incar,
- 3 akun seukuran kamu,
- 2 calon pembeli (balas berminggu-minggu sebelum DM, dan jangan pernah
  jualan di balasan).

### Cara pakai

```
/threads-skill:threads-plan susun minggu depan. Minggu ini saya
baru selesai bikin template katalog dan dapat 2 klien baru.
```

> 💡 **TIPS**: ceritakan apa yang **benar-benar terjadi** minggu ini.
> Postingan yang bagus lahir dari kejadian, bukan dari topik. "AI" itu
> topik. "Bot saya salah balas 40 orang" itu postingan.

Setelah rencana jadi, bilang "tulis Senin" dan Claude langsung bikin
drafnya.

---

# Bagian 4: Ngobrol Sama Manusia

## Bab 12. Balas-balasan (threads-balas)

**Di bab ini:**
- Sortir balasan sebelum menjawab
- Cara balas postingan orang biar nggak kayak bot

### Mode 1: kolom balasan postingan sendiri

Tempel balasan yang masuk. Claude akan menyortirnya dulu:

| Kelompok | Dapat apa |
| --- | --- |
| KATA KUNCI | barang yang dijanjikan |
| CALON PEMBELI | jawaban lengkap di depan umum, lalu satu tawaran bantuan |
| ISI | balasan paling panjang |
| PERTANYAAN | dijadikan postingan baru |
| DUKUNGAN | like, dan 3 sampai 8 kata |
| KEBISINGAN | nggak dibalas |

> 💡 **TIPS**: kalau satu pertanyaan juga ditanyakan banyak orang, jangan
> cuma dibalas. Jadikan postingan baru yang mengutip pertanyaan itu. Hook-nya
> sudah ditulis oleh penonton kamu sendiri.

> ⚠️ **AWAS**: pembenci jangan dibalas. Balasan itu jangkauan, dan itu yang
> mereka cari.

### Mode 2: balas postingan orang lain

Tempel postingan orangnya. Claude ngasih dua pilihan balasan dari dua jenis
yang berbeda, plus saran mana yang dikirim.

Jangan pernah dibuka dengan: "Mantap", "Setuju banget", "Daging", "Keren".
Dan jangan pernah jualan di balasan orang.

---

## Bab 13. DM yang Dibalas (threads-dm)

**Di bab ini:**
- Tiga jenis DM yang layak dikirim
- Aturan dua tindak lanjut

### Tiga jenis DM

1. **Balasan untuk tangan yang terangkat**: mereka ngetik kata kunci,
   jawab polling, atau bertanya. Mereka yang mulai.
2. **Pendekatan hangat**: orang yang postingannya sudah kamu balas
   berminggu-minggu.
3. **Ajakan kolaborasi**: usulan spesifik ke akun spesifik.

Sisanya DM dingin ke orang asing, hasilnya paling rendah untuk waktu yang sama.

### Kiriman kata kunci

Kirim barangnya **di pesan pertama**, tanpa syarat. Baru tanya di akhir.

```
{nama}, ini dia: {link-nya}.

{satu baris cara pakai}

{satu pertanyaan yang bisa dijawab 4 kata}
```

### Tindak lanjut

Dua kali saja: hari ke-4 (bawa hal baru) dan hari ke-10 (pamit). Lalu
berhenti.

> ⚠️ **AWAS**: jangan pakai alat yang ngirim DM otomatis ke orang yang nggak
> berinteraksi. Itu melanggar aturan Meta dan cara tercepat bikin akun
> dibatasi.

---

## Bab 14. Profil yang Bikin Orang Follow (threads-profil)

**Di bab ini:**
- Profil itu layar keputusan 3 detik
- Urutan perbaikan

### 3 detik

Orang mampir ke profilmu dari satu postingan. Mereka cuma bertanya: "Ada
lagi yang kayak tadi? Ini buat saya nggak?" Profilmu harus menjawab itu
dalam 3 detik.

### Urutan perbaikan

Claude memberi skor dari 100, lalu membetulkan dari yang paling banyak
kehilangan poin. Biasanya urutannya:

1. **Postingan disematkan**: pilih postingan terbaik dari hasil audit.
2. **Nama**: `Nama, kata yang dicari orang`. Contoh: "Rina, Konten AI".
3. **Bio baris pertama**: buat siapa dan apa yang berubah buat mereka.
4. **Link**: satu tujuan yang cocok dengan janji di bio.
5. **Lima postingan teratas**: harus satu niche.

```
/threads-skill:threads-profil cek profil saya [tempel screenshot]
```

> 💡 **TIPS**: kebanyakan profil dapat 30 sampai 50 di putaran pertama.
> Jangan kecil hati. Itu normal.

---

## Bab 15. Satu Konten Jadi Seminggu (threads-repurpose)

**Di bab ini:**
- Ekstrak, jangan ringkas
- Buang sisa platform asal

### Ekstrak, jangan ringkas

Dari satu video, podcast, atau artikel panjang, Claude mengambil:
klaim, angka, cerita, cara kerja, kesalahan, dan kalimat yang layak dikutip.
Tiap temuan jadi satu postingan yang berdiri sendiri.

### Buang sisa platform asal

Hapus "link di bio", "klik subscribe", "seperti di video saya", dan dinding
tagar. Postingan hasil daur ulang nggak boleh ngaku hasil daur ulang.

```
/threads-skill:threads-repurpose ubah transkrip video YouTube ini
jadi postingan Threads seminggu: [tempel transkrip]
```

> 📌 **INGAT**: kalau temuan kurang dari empat, sumbernya tipis. Claude
> akan bilang. Lebih baik dua postingan bagus daripada lima yang hambar.

---

# Bagian 5: Serba Sepuluh

## Bab 16. 10 Kesalahan yang Paling Sering

1. **Buka dengan sapaan.** "Halo warga!" makan baris pertama tanpa isi.
   Kalau tetap mau pakai sapaan, pastikan angka atau klaimnya muncul di
   baris pertama atau kedua.
2. **Ngejar komentar, lupa sebaran.** Rame di kolom balasan belum tentu
   menyebar ke luar.
3. **Posting di luar niche.** Lucu buat kamu, sepi buat algoritma.
4. **Angka bulat dan kabur.** "Omzet naik banyak" kalah sama "omzet naik
   18% dalam 3 minggu".
5. **Dua ide dalam satu postingan.** Itu dua postingan.
6. **Banyak tag topik.** Threads pakai satu.
7. **Teks tanpa bukti untuk klaim besar.** Kalau ada screenshot, pakai album.
8. **Ngatur jam sebelum ngatur hook.** Jam hampir nggak pernah jadi penyebab.
9. **Langsung pakai hasil AI tanpa dirapikan.** Em dash dan kata klise
   langsung ketahuan.
10. **Pakai bot balasan tanpa diuji.** Balasan yang salah nggak bisa
    ditarik setelah terkirim.

---

## Bab 17. 10 Perintah Siap Salin

Ganti bagian `[...]` dengan punyamu.

```
1.  Tulis voice.md saya dari tiga postingan ini: [tempel 3 postingan]
2.  /threads-skill:threads-audit akun @[namaakun]
3.  /threads-skill:threads-plan susun minggu depan. Minggu ini [kejadian nyata]
4.  Tulis Senin
5.  /threads-skill:threads-hook bikinin 3 hook soal [ide + angka]
6.  /threads-skill:threads-post tulis postingan soal [kejadian + angka]
7.  /threads-skill:threads-album bikinin album dari [screenshot/bukti]
8.  /threads-skill:threads-human rapikan ini: [teks]
9.  /threads-skill:threads-balas urus balasan ini: [tempel balasan]
10. Bongkar postingan ini, ambil rumusnya: [tempel postingan orang]
```

---

# Lampiran

## Lampiran A. Kamus Istilah

| Istilah | Artinya |
| --- | --- |
| **Hook** | baris pertama yang bikin orang berhenti menggulir |
| **Utas** | beberapa postingan yang bersambung |
| **Album** | postingan dengan beberapa foto atau video yang digeser |
| **Tag topik** | label topik di Threads, satu per postingan |
| **Median** | angka tengah setelah semua angka diurutkan |
| **Kelipatan** | view postingan dibagi median view akun |
| **Sebaran** | repost + quote + share per 1.000 view |
| **Niche** | topik sempit yang jadi ciri akunmu |
| **Swipe file** | catatan rumus yang terbukti jalan di niche |
| **Slop** | kata dan pola klise khas tulisan AI |
| **Em dash** | tanda pisah panjang. Dilarang di sini |
| **Linter** | alat pengecek otomatis sebelum posting |
| **Engage** | membalas dan berinteraksi di postingan orang lain |

## Lampiran B. 26 Rumus Hook dalam Satu Tabel

| No | Nama | Pola singkat | Tujuan |
| --- | --- | --- | --- |
| 1 | Pengakuan Biaya | {angka} habis gara-gara {kesalahan} | repost, balasan |
| 2 | Perintah Larangan | Berhenti {kebiasaan}. Lakukan {alternatif} | repost |
| 3 | Tidak Ada yang Bilang | Tidak ada yang bilang kalau {kenyataan} | repost, balasan |
| 4 | Pengganti Murah | {hal ini} menggantikan {hal mahal} | simpan, repost |
| 5 | Waktu Dipangkas | Dulu {lama}. Sekarang {singkat} | simpan, repost |
| 6 | Bukti Angka | Saya {lakukan} {N hari}. Ini angka aslinya | repost, follow |
| 7 | Salah Cara | Kamu salah {hal}, dan itu bukan salahmu | balasan, simpan |
| 8 | Bocoran Orang Dalam | {N tahun} saya di {bidang}. Ini yang tak pernah diucapkan | repost, follow |
| 9 | Ambil Saja | Ambil {template} ini | simpan |
| 10 | Kalau Kamu Begini | Kalau kamu {situasi}, ini beresin | simpan, balasan |
| 11 | Daftar dengan Favorit | {N} {hal}. Nomor {k} paling jarang dipakai | simpan |
| 12 | Keberatan | "{keberatan}". Oke. Ini versi yang tetap jalan | balasan |
| 13 | Sebelum dan Sesudah | {lama}. {baru}. {pengungkit} | simpan, repost |
| 14 | Panggilan Kelompok | {kelompok}, ini yang kalian lewatkan | balasan, repost |
| 15 | Catatan Gagal | {N} percobaan pertama gagal. Ini yang berubah | balasan, follow |
| 16 | Pertanyaan Apa Adanya | "{pertanyaan asli}". Masuk tiap minggu | balasan, simpan |
| 17 | Adu Langsung | {A} lawan {B}. Hasilnya jauh | balasan, repost |
| 18 | Langsung Praktik | {mulai di tengah aksi}. Lihat hasilnya | repost |
| 19 | Tenggat | {hal} berubah tanggal {tanggal} | simpan, klik |
| 20 | Izin | Kamu tidak butuh {hal yang katanya wajib} | repost, balasan |
| 21 | Mulai di Tengah Kalimat | ...dan saat itu {belokan} | balasan |
| 22 | Pepatah Dibalik | {pepatah terkenal, dibalik} | repost, balasan |
| 23 | Statistik | {N}% {kelompok} {fakta} | repost |
| 24 | Pengungkapan | Ini {hal} yang baru | repost, klik |
| 25 | Hasil Orang Lain | Ada satu {orang} yang {hasil} dalam {waktu} | follow, klik |
| 26 | Paling | {paling ...} adalah {jawaban} | repost, balasan |

Versi lengkap (contoh dan cara rusaknya) ada di
`skills/threads-hook/hooks.json`.

## Lampiran C. Kalau Ada yang Error

| Masalah | Coba ini |
| --- | --- |
| Skill nggak muncul setelah dipasang | tutup dan buka lagi Claude Code |
| `/threads-hook` nggak dikenal | kalau pasang sebagai plugin, pakai `/threads-skill:threads-hook` |
| `python3: command not found` | pasang Python 3 dari python.org, lalu ulangi |
| Draf penuh `{{angka}}` | isi bagian "Bukti yang boleh dipakai" di `voice.md`, atau kasih angkanya langsung |
| Linter bilang AWAS soal ajakan | baca kalimat yang disebut. Kalau memang cuma satu ajakan, abaikan |
| Humanizer GAGAL padahal kelihatan bersih | biasanya ada em dash atau karakter tak terlihat. Jalankan `humanize.py` dulu |
| Audit bilang "belum cukup data" | posting dulu sampai sekitar 20 postingan |

## Lampiran D. Contekan Satu Halaman

```
SEBELUM NULIS
  voice.md sudah diisi?            ~/.claude/threads/voice.md
  rencana minggu ini ada?          /threads-skill:threads-plan

BARIS PERTAMA
  angka/klaim di depan, tanpa sapaan basa-basi
  skor hook 70 ke atas             /threads-skill:threads-hook

BADAN POSTINGAN
  maksimal 500 karakter
  satu ide, satu ajakan, satu tag topik
  bukti visual? pakai album
  kepanjangan? pakai utas

SEBELUM POSTING
  nol em dash
  humanizer LOLOS                  /threads-skill:threads-human
  linter SIAP                      lint_post.py
  angka asli semua, nggak ada {{...}} tersisa

SETELAH POSTING
  balas di jam pertama             /threads-skill:threads-balas
  seminggu sekali: audit           /threads-skill:threads-audit
  sebulan sekali: riset niche      /threads-skill:threads-viral

YANG DIUKUR
  kelipatan  = view / median akun
  sebaran    = (repost + quote + share) per 1.000 view
  sebaran > balasan > suka > view
```

---

*Selamat posting. Ingat: baris pertama dulu, sisanya belakangan.*
