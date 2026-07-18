# ============================================================
# SISTEM INFORMASI PERPUSTAKAAN MINI
# Proyek Akhir - Algoritma dan Pemrograman
# Nama   : [ISI NAMA KAMU]
# NIM    : [ISI NIM KAMU]
# ============================================================
#
# Catatan: kode ini dikembangkan dari contoh di modul Bab 14,
# lalu ditambahkan 3 fitur yang belum ada di contoh:
#   1. Penyimpanan data ke file (persistent storage) -> data_buku.json
#   2. Batas waktu pinjam + denda keterlambatan
#   3. Menu "Lihat Riwayat Peminjaman"

import json
import os
from datetime import date, timedelta

SEPARATOR = "=" * 55
GARIS = "-" * 55

FILE_DATA = "data_buku.json"
LAMA_PINJAM_HARI = 7      # batas waktu pinjam
DENDA_PER_HARI = 1000     # rupiah per hari telat

# --- Data Global ---
katalog = {}          # dict: id_buku -> data buku
riwayat_pinjam = []    # list of dict: catatan transaksi
counter_id = 0

# ===========================
# FUNGSI UTILITAS
# ===========================

def generate_id():
    """Menghasilkan ID buku unik."""
    global counter_id
    counter_id += 1
    return f"BK-{counter_id:04d}"

def input_valid(prompt, tipe="str"):
    """Meminta input dengan validasi tipe data."""
    while True:
        nilai = input(prompt).strip()
        if not nilai:
            print("  Input tidak boleh kosong!")
            continue
        if tipe == "int":
            try:
                return int(nilai)
            except ValueError:
                print("  Masukkan angka yang valid!")
                continue
        return nilai

# ===========================
# FUNGSI FILE I/O (persistent storage)
# ===========================

def simpan_data():
    """Menyimpan katalog, riwayat, dan counter_id ke file JSON."""
    data = {
        "katalog": katalog,
        "riwayat_pinjam": riwayat_pinjam,
        "counter_id": counter_id,
    }
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def muat_data():
    """Memuat data dari file JSON jika file sudah ada."""
    global katalog, riwayat_pinjam, counter_id
    if not os.path.exists(FILE_DATA):
        return  # belum ada data tersimpan, mulai dari kosong

    with open(FILE_DATA, "r", encoding="utf-8") as f:
        data = json.load(f)

    katalog = data.get("katalog", {})
    riwayat_pinjam = data.get("riwayat_pinjam", [])
    counter_id = data.get("counter_id", 0)

# ===========================
# FUNGSI CRUD BUKU
# ===========================

def tambah_buku():
    """Menambahkan buku baru ke katalog."""
    print(f"\n{GARIS}")
    print("  TAMBAH BUKU BARU")
    print(GARIS)

    judul = input_valid("  Judul     : ")
    pengarang = input_valid("  Pengarang : ")
    tahun = input_valid("  Tahun     : ", "int")
    kategori = input_valid("  Kategori  : ")

    # Validasi tahun tidak boleh di masa depan
    if tahun > date.today().year:
        print("  Error: Tahun tidak boleh lebih dari tahun sekarang!")
        return

    id_buku = generate_id()
    katalog[id_buku] = {
        'judul': judul,
        'pengarang': pengarang,
        'tahun': tahun,
        'kategori': kategori,
        'status': 'tersedia'
    }

    print(f"\n  Buku '{judul}' berhasil ditambahkan!")
    print(f"  ID Buku: {id_buku}")
    simpan_data()

def tampilkan_semua():
    """Menampilkan seluruh buku di katalog, terurut berdasarkan judul."""
    if not katalog:
        print("\n  Katalog kosong.")
        return

    print(f"\n{SEPARATOR}")
    print(f"  KATALOG PERPUSTAKAAN ({len(katalog)} buku)")
    print(SEPARATOR)
    print(f"  {'ID':<10} {'Judul':<25} {'Pengarang':<20} {'Thn':>4} {'Status':<10}")
    print(f"  {GARIS}")

    # Urutkan berdasarkan judul (sorting)
    buku_terurut = sorted(katalog.items(),
                          key=lambda x: x[1]['judul'].lower())

    for id_buku, buku in buku_terurut:
        judul = buku['judul'][:23]
        pengarang = buku['pengarang'][:18]
        print(f"  {id_buku:<10} {judul:<25} {pengarang:<20} "
              f"{buku['tahun']:>4} {buku['status']:<10}")

def hapus_buku():
    """Menghapus buku dari katalog."""
    id_buku = input_valid("\n  Masukkan ID buku yang akan dihapus: ")

    if id_buku not in katalog:
        print(f"  Buku dengan ID '{id_buku}' tidak ditemukan.")
        return

    buku = katalog[id_buku]
    if buku['status'] == 'dipinjam':
        print(f"  Buku '{buku['judul']}' sedang dipinjam. Tidak bisa dihapus.")
        return

    konfirmasi = input(f"  Yakin hapus '{buku['judul']}'? (y/n): ").lower()
    if konfirmasi == 'y':
        del katalog[id_buku]
        print(f"  Buku '{buku['judul']}' berhasil dihapus.")
        simpan_data()
    else:
        print("  Penghapusan dibatalkan.")

# ===========================
# FUNGSI PENCARIAN (linear search)
# ===========================

def cari_buku():
    """Mencari buku berdasarkan keyword (judul/pengarang/kategori)."""
    print(f"\n{GARIS}")
    print("  CARI BUKU")
    print(f"  Kriteria: 1=Judul, 2=Pengarang, 3=Kategori")
    print(GARIS)

    pilihan = input("  Pilih kriteria (1-3): ").strip()
    kriteria_map = {"1": "judul", "2": "pengarang", "3": "kategori"}

    if pilihan not in kriteria_map:
        print("  Kriteria tidak valid!")
        return

    kriteria = kriteria_map[pilihan]
    keyword = input(f"  Masukkan keyword ({kriteria}): ").strip().lower()

    # Linear search: cek setiap buku satu per satu
    hasil = []
    for id_buku, buku in katalog.items():
        if keyword in buku[kriteria].lower():
            hasil.append((id_buku, buku))

    if not hasil:
        print(f"\n  Tidak ditemukan buku dengan {kriteria} '{keyword}'.")
        return

    # Urutkan hasil berdasarkan judul
    hasil.sort(key=lambda x: x[1]['judul'].lower())

    print(f"\n  Ditemukan {len(hasil)} buku:")
    print(f"  {'ID':<10} {'Judul':<25} {'Pengarang':<20} {'Status':<10}")
    print(f"  {GARIS}")
    for id_buku, buku in hasil:
        print(f"  {id_buku:<10} {buku['judul'][:23]:<25} "
              f"{buku['pengarang'][:18]:<20} {buku['status']:<10}")

# ===========================
# FUNGSI PEMINJAMAN (dengan batas waktu & denda)
# ===========================

def pinjam_buku():
    """Memproses peminjaman buku, mencatat tanggal pinjam & jatuh tempo."""
    id_buku = input_valid("\n  Masukkan ID buku yang akan dipinjam: ")

    if id_buku not in katalog:
        print(f"  Buku dengan ID '{id_buku}' tidak ditemukan.")
        return

    buku = katalog[id_buku]

    if buku['status'] == 'dipinjam':
        print(f"  Buku '{buku['judul']}' sedang dipinjam orang lain.")
        return

    nama_peminjam = input_valid("  Nama peminjam: ")

    tanggal_pinjam = date.today()
    jatuh_tempo = tanggal_pinjam + timedelta(days=LAMA_PINJAM_HARI)

    buku['status'] = 'dipinjam'
    buku['peminjam'] = nama_peminjam
    buku['tanggal_pinjam'] = tanggal_pinjam.isoformat()
    buku['jatuh_tempo'] = jatuh_tempo.isoformat()

    riwayat_pinjam.append({
        'id_buku': id_buku,
        'judul': buku['judul'],
        'peminjam': nama_peminjam,
        'aksi': 'pinjam',
        'tanggal': tanggal_pinjam.isoformat()
    })

    print(f"\n  Buku '{buku['judul']}' berhasil dipinjam oleh {nama_peminjam}.")
    print(f"  Batas kembali: {jatuh_tempo.isoformat()} "
          f"({LAMA_PINJAM_HARI} hari dari sekarang)")
    simpan_data()

def kembalikan_buku():
    """Memproses pengembalian buku dan menghitung denda jika telat."""
    id_buku = input_valid("\n  Masukkan ID buku yang akan dikembalikan: ")

    if id_buku not in katalog:
        print(f"  Buku dengan ID '{id_buku}' tidak ditemukan.")
        return

    buku = katalog[id_buku]

    if buku['status'] != 'dipinjam':
        print(f"  Buku '{buku['judul']}' tidak sedang dipinjam.")
        return

    peminjam = buku.get('peminjam', 'Unknown')
    tanggal_pinjam_str = buku.get('tanggal_pinjam', '-')
    jatuh_tempo_str = buku.get('jatuh_tempo')

    # Tampilkan info pinjaman
    print(f"\n  Peminjam      : {peminjam}")
    print(f"  Tanggal pinjam: {tanggal_pinjam_str}")
    print(f"  Jatuh tempo   : {jatuh_tempo_str or '-'}")

    # Input tanggal pengembalian
    while True:
        masukan = input(
            f"\n  Tanggal pengembalian (YYYY-MM-DD)]: "
        ).strip()
        if not masukan:
            tanggal_kembali = date.today()
            break
        try:
            tanggal_kembali = date.fromisoformat(masukan)
            break
        except ValueError:
            print("  Format tanggal tidak valid! Gunakan format YYYY-MM-DD (contoh: 2026-07-17).")

    denda = 0
    if jatuh_tempo_str:
        jatuh_tempo = date.fromisoformat(jatuh_tempo_str)
        if tanggal_kembali > jatuh_tempo:
            telat = (tanggal_kembali - jatuh_tempo).days
            denda = telat * DENDA_PER_HARI
            print(f"\n  Terlambat {telat} hari. Denda: Rp{denda:,}")
        else:
            print("\n  Dikembalikan tepat waktu, tidak ada denda.")

    buku['status'] = 'tersedia'
    buku.pop('peminjam', None)
    buku.pop('tanggal_pinjam', None)
    buku.pop('jatuh_tempo', None)

    riwayat_pinjam.append({
        'id_buku': id_buku,
        'judul': buku['judul'],
        'peminjam': peminjam,
        'aksi': 'kembali',
        'tanggal': tanggal_kembali.isoformat(),
        'denda': denda
    })

    print(f"  Buku '{buku['judul']}' berhasil dikembalikan oleh {peminjam}.")
    print(f"  Tanggal pengembalian: {tanggal_kembali.isoformat()}")
    simpan_data()

def lihat_riwayat():
    """Menampilkan seluruh riwayat transaksi peminjaman/pengembalian."""
    if not riwayat_pinjam:
        print("\n  Belum ada riwayat transaksi.")
        return

    print(f"\n{SEPARATOR}")
    print(f"  RIWAYAT PEMINJAMAN ({len(riwayat_pinjam)} transaksi)")
    print(SEPARATOR)

    for i, t in enumerate(riwayat_pinjam, start=1):
        info_denda = f" | Denda: Rp{t['denda']:,}" if t.get('denda') else ""
        print(f"  {i}. [{t['tanggal']}] {t['aksi'].upper():<8} "
              f"'{t['judul']}' oleh {t['peminjam']}{info_denda}")

# ===========================
# FUNGSI STATISTIK
# ===========================

def tampilkan_statistik():
    """Menampilkan statistik perpustakaan."""
    total = len(katalog)
    if total == 0:
        print("\n  Katalog kosong - belum ada statistik.")
        return

    tersedia = sum(1 for b in katalog.values() if b['status'] == 'tersedia')
    dipinjam = sum(1 for b in katalog.values() if b['status'] == 'dipinjam')
    total_denda = sum(t.get('denda', 0) for t in riwayat_pinjam)

    # Hitung jumlah buku per kategori
    kategori_count = {}
    for buku in katalog.values():
        kat = buku['kategori']
        kategori_count[kat] = kategori_count.get(kat, 0) + 1

    print(f"\n{SEPARATOR}")
    print("  STATISTIK PERPUSTAKAAN")
    print(SEPARATOR)
    print(f"  Total buku       : {total}")
    print(f"  Tersedia         : {tersedia}")
    print(f"  Dipinjam         : {dipinjam}")
    print(f"  Total transaksi  : {len(riwayat_pinjam)}")
    print(f"  Total denda      : Rp{total_denda:,}")
    print(f"\n  Buku per Kategori:")

    # Urutkan kategori dari yang jumlahnya terbanyak (sorting)
    for kat, jumlah in sorted(kategori_count.items(),
                               key=lambda x: x[1], reverse=True):
        bar = "#" * jumlah
        print(f"    {kat:<15} : {bar} ({jumlah})")

# ===========================
# FUNGSI MENU UTAMA
# ===========================

def tampilkan_header():
    """Menampilkan header program."""
    print(f"\n{SEPARATOR}")
    print("     SISTEM INFORMASI PERPUSTAKAAN MINI")
    print("     Algoritma dan Pemrograman - Proyek Akhir")
    print(SEPARATOR)

def tampilkan_menu():
    """Menampilkan menu utama."""
    print("\n  +================ MENU ==================+")
    print("  |  1. Tambah Buku Baru                    |")
    print("  |  2. Tampilkan Semua Buku                |")
    print("  |  3. Cari Buku                           |")
    print("  |  4. Pinjam Buku                          |")
    print("  |  5. Kembalikan Buku                      |")
    print("  |  6. Hapus Buku                           |")
    print("  |  7. Statistik                            |")
    print("  |  8. Lihat Riwayat Peminjaman             |")
    print("  |  9. Keluar                               |")
    print("  +==========================================+")

def main():
    """Fungsi utama program: memuat data, menjalankan loop menu."""
    tampilkan_header()
    muat_data()

    if katalog:
        print(f"\n  Data berhasil dimuat dari '{FILE_DATA}' "
              f"({len(katalog)} buku).")
    else:
        print("\n  Belum ada data tersimpan. Mulai dari katalog kosong.")

    aksi = {
        "1": tambah_buku,
        "2": tampilkan_semua,
        "3": cari_buku,
        "4": pinjam_buku,
        "5": kembalikan_buku,
        "6": hapus_buku,
        "7": tampilkan_statistik,
        "8": lihat_riwayat,
    }

    while True:
        tampilkan_menu()
        pilihan = input("\n  Pilih menu (1-9): ").strip()

        if pilihan == "9":
            simpan_data()
            print(f"\n  Data tersimpan di '{FILE_DATA}'.")
            print(f"  Terima kasih telah menggunakan sistem ini.\n")
            break

        if pilihan in aksi:
            aksi[pilihan]()
        else:
            print("  Pilihan tidak valid! Silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    main()
