# Sistem Informasi Perpustakaan Mini

## Deskripsi
Aplikasi konsol Python untuk mengelola perpustakaan mini. Dikembangkan
sebagai Proyek Akhir mata kuliah Algoritma dan Pemrograman, Program Studi
Informatika, Universitas Al Azhar Indonesia.

## Latar Belakang Masalah
Perpustakaan kecil (misalnya di kampus, sekolah, atau komunitas) sering
masih mencatat peminjaman buku secara manual di buku catatan. Ini membuat
pencarian buku lambat, riwayat peminjaman sulit dilacak, dan tidak ada
mekanisme untuk mengingatkan keterlambatan pengembalian. Aplikasi ini
menyediakan solusi digital sederhana berbasis konsol.

## Fitur
1. Tambah buku baru ke katalog
2. Tampilkan seluruh buku (terurut berdasarkan judul)
3. Cari buku berdasarkan judul / pengarang / kategori
4. Pinjam buku (otomatis mencatat batas waktu pengembalian, 7 hari)
5. Kembalikan buku (otomatis menghitung denda jika terlambat)
6. Hapus buku dari katalog
7. Statistik perpustakaan (total buku, status, buku per kategori)
8. Lihat riwayat seluruh transaksi peminjaman/pengembalian
9. **Data tersimpan otomatis ke file** `data_buku.json`, sehingga data
   tidak hilang saat program ditutup dan dimuat ulang saat program dibuka
   kembali

## Cara Menjalankan
1. Pastikan Python 3 terpasang
2. Jalankan lewat terminal:
   ```
   python3 main.py
   ```
   Atau upload `main.py` ke Google Colab dan jalankan `!python main.py`
   (catatan: input interaktif di Colab kadang perlu disesuaikan)

## Struktur Data
| Data | Struktur | Alasan |
|------|----------|--------|
| Katalog buku | `dict` (key = id_buku) | Akses cepat O(1) berdasarkan ID |
| Riwayat transaksi | `list` of `dict` | Perlu urutan kronologis dan iterasi |
| Data 1 buku | `dict` | Menyimpan judul, pengarang, tahun, kategori, status |

## Algoritma yang Digunakan
- **Linear search** — untuk mencari buku berdasarkan keyword (fungsi `cari_buku`)
- **Sorting** (`sorted()` / `.sort()`) — untuk menampilkan katalog dan hasil
  pencarian terurut berdasarkan judul, serta statistik kategori terbanyak
- **Perhitungan tanggal** (modul `datetime`) — untuk menentukan jatuh tempo
  dan menghitung denda keterlambatan

## Struktur File Proyek
```
perpustakaan-mini/
├── main.py            # Program utama
├── data_buku.json     # Data tersimpan (dibuat otomatis saat program jalan)
└── README.md          # Dokumentasi ini
```

## Keterbatasan / Pengembangan Selanjutnya
- Belum ada sistem login/multi-user untuk petugas perpustakaan
- Belum ada validasi jika beberapa peminjam mengembalikan di hari yang sama
  dengan urutan transaksi yang kompleks
- Denda saat ini dihitung flat per hari, belum ada batas maksimum denda

## Identitas
- Nama: [ISI NAMA KAMU]
- NIM: [ISI NIM KAMU]
- Mata Kuliah: Algoritma dan Pemrograman (3 SKS)
- Dosen: Tri Aji Nugroho, S.T., M.T.
- Semester: Genap 2025/2026
