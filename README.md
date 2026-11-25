# threads-skill

12 skill Claude Code untuk menulis, meriset, dan mengaudit konten **Threads**,
dalam bahasa Indonesia. Gabungan dua paket skill Instagram yang ditulis ulang
untuk cara kerja Threads: postingan teks 500 karakter, utas, album, satu tag
topik, link yang bisa diklik, tanpa Stories.

Satu aturan berlaku di semua skill: **em dash dan en dash dilarang total.**
Tidak ada kuota. `humanize.py` menghapusnya, `lint_post.py` dan `detect.py`
menggagalkannya.

## Baru pertama kali? Baca ini dulu

- **[PANDUAN.md](PANDUAN.md)**: buku panduan santai, dari pasang sampai
  ngukur hasil. Ada ikon tips, ingat, awas, dan contekan satu halaman.
- **[CONTOH.md](CONTOH.md)**: pola perintah, 8 contoh siap salin, dan satu
  studi kasus utuh untuk tiap skill.

## Isi

| Skill | Untuk apa | Alat |
| --- | --- | --- |
| `threads-post` | satu postingan: hook, isi, satu ajakan, satu tag topik, link, polling | `lint_post.py` |
| `threads-utas` | rangkaian beberapa postingan bersambung | memakai `lint_post.py` |
| `threads-album` | album foto/video, slide bukti, video pendek, file 1080x1350 | |
| `threads-hook` | 26 rumus baris pertama, skor hook, bongkar postingan orang | `hookscore.py`, `hooks.json` |
| `threads-human` | buang jejak AI, kata klise Indonesia + Inggris, skor lima pemeriksaan | `humanize.py`, `detect.py`, `slop.json` |
| `threads-viral` | riset niche berbasis kelipatan median akun, swipe file | `swipe.py` |
| `threads-audit` | bedah postingan sendiri: kelipatan, sebaran, balasan | |
| `threads-plan` | rencana mingguan + daftar 10 akun untuk dibalas | |
| `threads-balas` | sortir dan balas kolom balasan sendiri, balas postingan orang | |
| `threads-dm` | kiriman kata kunci, pesan hangat, ajakan kolaborasi, tindak lanjut | |
| `threads-profil` | skor profil dari 100 dan tulis ulang bagian yang lemah | |
| `threads-repurpose` | ubah video, podcast, artikel, postingan platform lain jadi seminggu Threads | |

Semua script Python 3 tanpa dependensi luar.

## Pasang

### Sebagai plugin Claude Code

```bash
claude plugin marketplace add bangdirtop/threads-skill
claude plugin install threads-skill@threads-skill
```

### Atau salin langsung

```bash
git clone https://github.com/bangdirtop/threads-skill.git
cp -R threads-skill/skills/* ~/.claude/skills/
```

### Siapkan folder data

Skill menyimpan profil suara, swipe file, log, dan rencana di
`~/.claude/threads/`:

```bash
mkdir -p ~/.claude/threads
cp threads-skill/templates/voice.md ~/.claude/threads/voice.md
```

Isi `voice.md`, atau minta Claude menulisnya dari tiga postingan Threads
milikmu.

## Alur yang disarankan

1. `threads-audit` dulu kalau akunmu sudah punya 20 postingan atau lebih.
2. `threads-viral` sebulan sekali untuk swipe file niche.
3. `threads-plan` seminggu sekali.
4. Tiap slot: `threads-post`, `threads-utas`, atau `threads-album`. Semuanya
   lewat `threads-hook` untuk baris pertama dan `threads-human` sebelum
   ditunjukkan.
5. Setelah posting: `threads-balas` di jam pertama.

## Contoh script

```bash
cd skills
python3 threads-hook/hookscore.py --hook "Tidak ada yang bilang kalau 20 postingan pertamamu memang akan sepi."
python3 threads-human/humanize.py draf.txt -o bersih.txt --report
python3 threads-human/detect.py draf.txt bersih.txt
python3 threads-post/lint_post.py bersih.txt --keywords "konten AI"
python3 threads-viral/swipe.py kumpulan.tsv --out ~/.claude/threads/swipe.md
```

## Prinsip

- **Tidak ada yang diposting otomatis.** Skill menulis, user yang memposting.
- **Angka tidak pernah dikarang.** Yang belum ada ditulis `{{angka}}`.
- **Ukur dengan median akun sendiri**, bukan view mentah.
- **Baca, jangan scraping.** Tidak ada crawler, tidak ada login atas nama user.
- **Tiru rumusnya, bukan postingannya.**

Batas fitur Threads (jumlah item album, durasi video, jumlah link di profil,
lampiran teks panjang, postingan sementara) bisa berubah. Kalau ada yang
berbeda di aplikasimu, aplikasinya yang benar.

## Kredit

Struktur dan sebagian gagasan diadaptasi dari
[instagram-skills](https://github.com/sergebulaev/instagram-skills) oleh Serge
Bulaev (MIT) dan dari paket skill Instagram `ig-*`. Semua teks dan script di
repo ini ditulis ulang untuk Threads dan bahasa Indonesia.

## Lisensi

MIT. Lihat [LICENSE](LICENSE).
