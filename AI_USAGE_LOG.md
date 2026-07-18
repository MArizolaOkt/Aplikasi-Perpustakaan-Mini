# AI Usage Log — Proyek Akhir

> PENTING: Template ini hanya kerangka. Isi SEMUA bagian bertanda [...]
> dengan interaksi ASLI kamu bersama AI (prompt yang benar-benar kamu
> ketik, jawaban yang benar-benar AI berikan). Jangan mengarang interaksi
> yang tidak pernah terjadi — bagian ini dinilai juga dari kejujuran
> (komponen Etika & Integritas, 5%), bukan cuma kelengkapan.

## Identitas
- Nama: Muhammad Arizola Oktramadiputra
- NIM: 0102519017
- Proyek: Sistem Informasi Perpustakaan Mini
- Tanggal mulai: 10 Juli 2026
- Tanggal selesai: 14 Juli 2026

## Ringkasan
- AI yang digunakan: Claude (Antigravity IDE)
- Persentase kode AI: 85%
- Persentase kode sendiri: 15%
- Jumlah interaksi: [ISI JUMLAH]

## Detail Interaksi

### Interaksi 1
- **Prompt:**
  ```
  1. Nama aplikasi:
     Sistem Informasi Perpustakaan Mini

  2. Bentuk aplikasi:
     Aplikasi Command Line Interface (CLI) berbasis Python.

  3. Tujuan utama:
     Mengelola katalog buku perpustakaan sederhana, termasuk pencatatan
     peminjaman, pengembalian, denda keterlambatan, statistik, dan riwayat transaksi.

  4. Pengguna aplikasi:
     Petugas atau admin perpustakaan.

  5. Fitur utama:
     - Menambah buku baru ke katalog.
     - Menampilkan semua buku, diurutkan berdasarkan judul.
     - Mencari buku berdasarkan judul, pengarang, atau kategori.
     - Meminjamkan buku kepada peminjam.
     - Mengembalikan buku dan menghitung denda keterlambatan.
     - Menghapus buku yang tersedia.
     - Menampilkan statistik perpustakaan.
     - Menampilkan riwayat peminjaman dan pengembalian.
     - Menyimpan dan memuat data dari file JSON.

  6. Data yang disimpan:
     Data buku:
     - ID buku, misalnya BK-0001
     - Judul
     - Pengarang
     - Tahun terbit
     - Kategori
     - Status: tersedia atau dipinjam
     - Nama peminjam, jika sedang dipinjam
     - Tanggal pinjam, jika sedang dipinjam
     - Tanggal jatuh tempo, jika sedang dipinjam

     Data riwayat transaksi:
     - ID buku
     - Judul buku
     - Nama peminjam
     - Aksi: pinjam atau kembali
     - Tanggal transaksi
     - Denda, khusus saat pengembalian terlambat

  7. Aturan bisnis:
     - Setiap buku menerima ID unik otomatis dengan format BK-XXXX.
     - Tahun terbit tidak boleh lebih besar dari tahun sekarang.
     - Buku hanya dapat dipinjam jika statusnya tersedia.
     - Durasi peminjaman maksimal 7 hari.
     - Denda keterlambatan adalah Rp1.000 per hari.
     - Buku hanya dapat dikembalikan jika statusnya dipinjam.
     - Buku yang sedang dipinjam tidak boleh dihapus.
     - Data disimpan dalam file data_buku.json saat ada perubahan dan saat keluar.
     - Buku ditampilkan serta hasil pencarian diurutkan berdasarkan judul.

  8. Bentuk output yang diinginkan:
     Program Python interaktif melalui terminal dengan menu:
     1. Tambah Buku Baru
     2. Tampilkan Semua Buku
     3. Cari Buku
     4. Pinjam Buku
     5. Kembalikan Buku
     6. Hapus Buku
     7. Statistik
     8. Lihat Riwayat Peminjaman
     9. Keluar

  9. Edge case yang harus ditangani:
     - Pengguna memasukkan pilihan menu selain 1–9.
     - Input wajib seperti judul, pengarang, kategori, atau nama peminjam kosong.
     - Input tahun bukan angka.
     - Tahun terbit lebih besar dari tahun saat ini.
     - ID buku tidak ditemukan saat dipinjam, dikembalikan, atau dihapus.
     - Buku yang sudah dipinjam dicoba untuk dipinjam kembali.
     - Buku tersedia dicoba untuk dikembalikan.
     - Buku yang masih dipinjam dicoba untuk dihapus.
     - Hasil pencarian tidak ditemukan.
     - Katalog masih kosong saat ingin melihat data atau statistik.
     - Riwayat transaksi masih kosong.
     - Pengembalian tepat waktu: denda Rp0.
     - Pengembalian terlambat: denda dihitung berdasarkan jumlah hari terlambat.
     - File data_buku.json belum ada: aplikasi memulai dengan katalog kosong.

  10. Batasan tambahan:
      - Menggunakan Python.
      - Tanpa database; penyimpanan menggunakan JSON.
      - Data disimpan secara lokal pada folder aplikasi.
      - Antarmuka berupa terminal, bukan website atau GUI.
      - Menggunakan struktur data dictionary untuk katalog dan list untuk riwayat transaksi.
    
  11. Masukan AI Usage Log dan README.MD yang proper

- **Respons AI:** Oke, aku bikinkan kerangka kerjanya. Untuk kode, aku ambil contoh dari modul lalu tambahin fitur yang belum ada di contoh (supaya jelas beda dan bukan copy-paste) — 
yaitu penyimpanan file (persistent storage berbentuk JSON) , plus fitur denda keterlambatan dan riwayat peminjaman. 
README dan AI Usage Log aku siapkan juga.
versi modifikasi dengan fitur tambahan (file I/O, denda, riwayat)Done Sekarang aku tes dulu supaya kamu yakin programnya jalan tanpa error:Menguji program dengan simulasi input menuMenguji 
program dengan simulasi input menuProgram berjalan lancar tanpa error, dan file data_buku.json berhasil dibuat (persistent storage-nya kerja).

- **Yang digunakan:**  seluruh perubahan kode digunakan, kecuali bagian teks prompt input yang menampilkan tanggal hari ini secara dinamis — bagian itu dihapus secara manual oleh pengguna agar lebih ringkas.
- **Modifikasi:** Mengubah baris interface dari `*` menjadi `=`, menambahkan spacing ` ` di beberapa bagian agar lebih rapi.
- **Pelajaran:** AI bisa membaca konteks dari spec yang diberikan

### Interaksi 2
- **Prompt:** "Pada fitur pengembalian buku, tambahkan tanggal pengembalian buku."
- **Respons AI:** AI membaca kode fungsi `kembalikan_buku()` di `main.py` dan menemukan bahwa tanggal pengembalian sebelumnya selalu otomatis menggunakan `date.today()`. AI kemudian memodifikasi fungsi tersebut dengan menambahkan:
  1. Tampilan info pinjaman (nama peminjam, tanggal pinjam, jatuh tempo) sebelum proses pengembalian.
  2. Input tanggal pengembalian manual dengan format `YYYY-MM-DD`, dengan opsi menekan Enter untuk menggunakan tanggal hari ini.
  3. Validasi format tanggal — jika format salah, program meminta input ulang.
  4. Perhitungan denda berdasarkan tanggal yang dimasukkan pengguna (bukan selalu `date.today()`).
  5. Konfirmasi tanggal pengembalian ditampilkan di akhir proses.
- **Yang digunakan:** Hampir seluruh perubahan kode digunakan, kecuali bagian teks prompt input yang menampilkan tanggal hari ini secara dinamis — bagian itu dihapus secara manual oleh pengguna agar lebih ringkas.
- **Modifikasi:** Mengubah baris prompt input dari `f"\n  Tanggal pengembalian (YYYY-MM-DD) [Enter = hari ini ({date.today().isoformat()})]: "` menjadi `f"\n  Tanggal pengembalian (YYYY-MM-DD)]: "` agar tampilannya lebih sederhana.
- **Pelajaran:** AI bisa membaca konteks kode yang sudah ada dan memodifikasi hanya bagian yang diperlukan tanpa mengubah logika lain. Saya juga belajar cara validasi input tanggal menggunakan `date.fromisoformat()` dan blok `try/except`.

<!-- Tambahkan interaksi 3, 4, dst sesuai jumlah interaksi kamu yang sebenarnya -->

## Refleksi
AI sangat membantu dalam membangun kerangka awal program secara cepat dan lengkap — mulai dari struktur menu, fungsi CRUD buku, hingga tiga fitur tambahan (penyimpanan JSON, sistem denda, dan riwayat peminjaman) yang saya minta berdasarkan spesifikasi yang saya susun sendiri. Bagian yang saya kerjakan/desain sendiri adalah menentukan aturan bisnis (batas pinjam 7 hari, denda Rp1.000/hari, format ID BK-XXXX), menyusun edge case yang harus ditangani, serta melakukan penyesuaian kecil pada tampilan (mengganti separator, merapikan spasi, menyederhanakan teks prompt input tanggal). Saya juga secara aktif meminta revisi pada fitur pengembalian buku agar tanggal bisa diinput manual, bukan hanya otomatis memakai tanggal hari ini.
