"""
data_tiket.py - Data bersama dan fungsi bantu (dipakai semua fitur)

Seluruh tiket disimpan dalam sebuah list (array) yang berisi dict (struct).
Data hanya ada di memori, hilang saat program ditutup (sesuai ketentuan Tahap 1).
"""

# ---------------------------------------------------------------------------
JENIS_VALID = ["Hardware", "Software", "Jaringan", "Lainnya"]
PRIORITAS_VALID = ["Rendah", "Sedang", "Tinggi"]
ALUR_STATUS = {"Menunggu": "Diproses", "Diproses": "Selesai"}

# Array of Struct: list of dict
daftar_tiket = []


def cari_indeks_kode(kode):
    """Kembalikan indeks tiket dengan kode persis sama (tidak peduli huruf besar/kecil),
    atau -1 jika tidak ada."""
    for i in range(len(daftar_tiket)):
        if daftar_tiket[i]["kode_tiket"].lower() == kode.lower():
            return i
    return -1


def normalisasi_pilihan(teks, pilihan_valid):
    """Cocokkan teks dengan daftar pilihan tanpa peduli huruf besar/kecil.
    Mengembalikan nilai dengan format konsisten (huruf kapital di awal) atau None."""
    for pilihan in pilihan_valid:
        if teks.strip().lower() == pilihan.lower():
            return pilihan
    return None


def minta_konfirmasi(pertanyaan):
    """Minta konfirmasi y/n. Mengembalikan True jika 'y'."""
    while True:
        jawab = input(pertanyaan + " (y/n): ").strip().lower()
        if jawab in ("y", "n"):
            return jawab == "y"
        print("Masukkan 'y' atau 'n'.")


def tanda_prioritas(prioritas):
    return "[" + prioritas.upper() + "]"


def tanda_status(status):
    return "[" + status.upper() + "]"


def cetak_tabel(data):
    """Cetak tabel tiket: No, Kode, Nama Pelapor, Jenis Masalah, Prioritas, Status."""
    garis = "-" * 82
    print(garis)
    print(f"{'No':<4}{'Kode':<10}{'Nama Pelapor':<24}{'Jenis Masalah':<15}"
          f"{'Prioritas':<12}{'Status':<12}")
    print(garis)
    for no, t in enumerate(data, start=1):
        print(f"{no:<4}{t['kode_tiket'][:9]:<10}{t['nama_pelapor'][:23]:<24}"
              f"{t['jenis_masalah']:<15}{tanda_prioritas(t['prioritas']):<12}"
              f"{tanda_status(t['status']):<12}")
    print(garis)


def cetak_detail(t):
    """Cetak seluruh atribut satu tiket (termasuk deskripsi)."""
    print("=" * 50)
    print(f"Kode Tiket    : {t['kode_tiket']}")
    print(f"Nama Pelapor  : {t['nama_pelapor']}")
    print(f"Jenis Masalah : {t['jenis_masalah']}")
    print(f"Deskripsi     : {t['deskripsi']}")
    print(f"Prioritas     : {tanda_prioritas(t['prioritas'])}")
    print(f"Status        : {tanda_status(t['status'])}")
    print("=" * 50)


def muat_data_contoh():
    contoh = [
        ("TKT001", "Andi Wijaya", "Hardware", "Laptop tidak bisa menyala", "Tinggi", "Menunggu"),
        ("TKT002", "Andi Saputra", "Jaringan", "Wi-Fi ruang dosen putus", "Sedang", "Diproses"),
        ("TKT003", "Siti Rahma", "Software", "Aplikasi akademik tidak bisa dibuka", "Rendah", "Selesai"),
        ("TKT004", "Budi Santoso", "Lainnya", "Akun email terkunci", "Sedang", "Menunggu"),
    ]
    ditambah = 0
    for kode, nama, jenis, desk, prio, status in contoh:
        if cari_indeks_kode(kode) == -1:
            daftar_tiket.append({
                "kode_tiket": kode, "nama_pelapor": nama, "jenis_masalah": jenis,
                "deskripsi": desk, "prioritas": prio, "status": status,
            })
            ditambah += 1
    print(f"{ditambah} data contoh dimuat.")
