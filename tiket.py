"""
main.py - Entry point Sistem Helpdesk / Tiket Layanan (CLI)
Jalankan dengan: python main.py
"""
from data_tiket import muat_data_contoh # type: ignore
from f1_tambah import tambah_tiket # type: ignore
from f2_tampilkan import tampilkan_semua_tiket # type: ignore
from f3_cari import cari_tiket # type: ignore
from f4_update_status import update_status_tiket # type: ignore
from f5_filter import filter_tiket
from f6_hapus import hapus_tiket


def tampilkan_menu():
    print("\n" + "=" * 42)
    print("   SISTEM HELPDESK / TIKET LAYANAN")
    print("=" * 42)
    print("1. Tambah tiket baru")
    print("2. Tampilkan semua tiket")
    print("3. Cari tiket")
    print("4. Update status tiket")
    print("5. Filter tiket berdasarkan jenis masalah")
    print("6. Hapus tiket")
    print("7. Muat data contoh (untuk demo)")
    print("0. Keluar")
    print("=" * 42)


def main():
    menu = {
        "1": tambah_tiket,
        "2": tampilkan_semua_tiket,
        "3": cari_tiket,
        "4": update_status_tiket,
        "5": filter_tiket,
        "6": hapus_tiket,
        "7": muat_data_contoh,
    }

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Terima kasih. Data tiket tidak disimpan permanen. Sampai jumpa!")
            break
        elif pilihan in menu:
            menu[pilihan]()
        else:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan.")
"""
tiket.py - Modul data tiket (Tahap 1: Array & Struct)

Seluruh tiket disimpan dalam sebuah list (array) yang berisi dict (struct).
Data hanya ada di memori, hilang saat program ditutup (sesuai ketentuan Tahap 1).
"""


# Konstanta

JENIS_VALID = ["Hardware", "Software", "Jaringan", "Lainnya"]
PRIORITAS_VALID = ["Rendah", "Sedang", "Tinggi"]
ALUR_STATUS = {"Menunggu": "Diproses", "Diproses": "Selesai"}

# Array of Struct: list of dict
daftar_tiket = []



# Fungsi bantu

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



# Fitur 1: Tambah Tiket Baru

def tambah_tiket():
    print("\n--- TAMBAH TIKET BARU ---")
    kode = input("Kode tiket      : ").strip()
    if kode == "":
        print("Gagal: kode tiket tidak boleh kosong.")
        return
    if cari_indeks_kode(kode) != -1:
        print(f"Gagal: kode tiket '{kode}' sudah digunakan.")
        return

    nama = input("Nama pelapor    : ").strip()
    if nama == "":
        print("Gagal: nama pelapor tidak boleh kosong.")
        return

    jenis_input = input(f"Jenis masalah ({'/'.join(JENIS_VALID)}): ")
    jenis = normalisasi_pilihan(jenis_input, JENIS_VALID)
    if jenis is None:
        print(f"Gagal: jenis masalah harus salah satu dari: {', '.join(JENIS_VALID)}.")
        return

    deskripsi = input("Deskripsi masalah: ").strip()
    if deskripsi == "":
        print("Gagal: deskripsi tidak boleh kosong.")
        return

    prioritas_input = input(f"Prioritas ({'/'.join(PRIORITAS_VALID)}): ")
    prioritas = normalisasi_pilihan(prioritas_input, PRIORITAS_VALID)
    if prioritas is None:
        print(f"Gagal: prioritas harus salah satu dari: {', '.join(PRIORITAS_VALID)}.")
        return

    tiket = {
        "kode_tiket": kode,
        "nama_pelapor": nama,
        "jenis_masalah": jenis,
        "deskripsi": deskripsi,
        "prioritas": prioritas,
        "status": "Menunggu",  # nilai awal selalu Menunggu
    }
    daftar_tiket.append(tiket)
    print(f"Tiket {kode} dari {nama} berhasil dicatat.")



# Fitur 2: Tampilkan Semua Tiket

def tampilkan_semua_tiket():
    print("\n--- DAFTAR SEMUA TIKET ---")
    if len(daftar_tiket) == 0:
        print("Belum ada tiket dalam sistem.")
        return

    cetak_tabel(daftar_tiket)

    menunggu = diproses = selesai = 0
    for t in daftar_tiket:
        if t["status"] == "Menunggu":
            menunggu += 1
        elif t["status"] == "Diproses":
            diproses += 1
        elif t["status"] == "Selesai":
            selesai += 1
    print(f"Total tiket: {len(daftar_tiket)} | Menunggu: {menunggu} | "
          f"Diproses: {diproses} | Selesai: {selesai}")



# Fitur 3: Cari Tiket

def cari_tiket():
    print("\n--- CARI TIKET ---")
    print("1. Cari berdasarkan kode tiket")
    print("2. Cari berdasarkan nama pelapor")
    mode = input("Pilih mode (1/2): ").strip()
    if mode not in ("1", "2"):
        print("Pilihan mode tidak valid.")
        return

    kata_kunci = input("Kata kunci: ").strip()
    if kata_kunci == "":
        print("Gagal: kata kunci tidak boleh kosong.")
        return

    if mode == "1":
        # Exact match, hanya 1 hasil
        idx = cari_indeks_kode(kata_kunci)
        if idx == -1:
            print(f"Tiket dengan kode '{kata_kunci}' tidak ditemukan.")
        else:
            cetak_detail(daftar_tiket[idx])
    else:
        # Partial match, tidak case sensitive, bisa banyak hasil
        hasil = []
        for t in daftar_tiket:
            if kata_kunci.lower() in t["nama_pelapor"].lower():
                hasil.append(t)
        if len(hasil) == 0:
            print(f"Tiket dengan nama pelapor '{kata_kunci}' tidak ditemukan.")
        else:
            print(f"Ditemukan {len(hasil)} tiket dengan nama pelapor mengandung '{kata_kunci}':")
            cetak_tabel(hasil)



# Fitur 4: Update Status Tiket

def update_status_tiket():
    print("\n--- UPDATE STATUS TIKET ---")
    kode = input("Kode tiket: ").strip()
    idx = cari_indeks_kode(kode)
    if idx == -1:
        print(f"Tiket dengan kode '{kode}' tidak ditemukan.")
        return

    tiket = daftar_tiket[idx]
    if tiket["status"] == "Selesai":
        print(f"Tiket {tiket['kode_tiket']} sudah berstatus Selesai dan tidak dapat diperbarui lagi.")
        return

    status_lama = tiket["status"]
    status_baru = ALUR_STATUS[status_lama]
    print(f"Kode tiket      : {tiket['kode_tiket']}")
    print(f"Nama pelapor    : {tiket['nama_pelapor']}")
    print(f"Status saat ini : {status_lama}")
    print(f"Status berikutnya: {status_baru}")

    if minta_konfirmasi("Lanjutkan perubahan status?"):
        tiket["status"] = status_baru
        print(f"Status tiket {tiket['kode_tiket']} berhasil diperbarui: "
              f"{status_lama} menjadi {status_baru}.")
    else:
        print("Perubahan status dibatalkan.")



# Fitur 5: Filter Tiket Berdasarkan Jenis Masalah

def filter_tiket():
    print("\n--- FILTER TIKET BERDASARKAN JENIS MASALAH ---")
    jenis_input = input(f"Jenis masalah ({'/'.join(JENIS_VALID)}): ")
    jenis = normalisasi_pilihan(jenis_input, JENIS_VALID)
    if jenis is None:
        print(f"Gagal: jenis masalah harus salah satu dari: {', '.join(JENIS_VALID)}.")
        return

    hasil = []
    for t in daftar_tiket:
        if t["jenis_masalah"] == jenis:
            hasil.append(t)

    if len(hasil) == 0:
        print(f"Tidak ada tiket dengan jenis masalah '{jenis}' dalam sistem.")
    else:
        print(f"Menampilkan tiket jenis masalah: {jenis} ({len(hasil)} tiket ditemukan).")
        cetak_tabel(hasil)



# Fitur 6: Hapus Tiket

def hapus_tiket():
    print("\n--- HAPUS TIKET ---")
    kode = input("Kode tiket: ").strip()
    idx = cari_indeks_kode(kode)
    if idx == -1:
        print(f"Tiket dengan kode '{kode}' tidak ditemukan.")
        return

    tiket = daftar_tiket[idx]
    # Cek status SEBELUM menampilkan konfirmasi
    if tiket["status"] != "Selesai":
        print(f"Tiket {tiket['kode_tiket']} tidak dapat dihapus karena masih berstatus "
              f"{tiket['status']}. Selesaikan penanganan tiket terlebih dahulu sebelum menghapusnya.")
        return

    print(f"Kode tiket    : {tiket['kode_tiket']}")
    print(f"Nama pelapor  : {tiket['nama_pelapor']}")
    print(f"Jenis masalah : {tiket['jenis_masalah']}")
    print(f"Prioritas     : {tiket['prioritas']}")
    print(f"Status        : {tiket['status']}")

    if minta_konfirmasi("Yakin ingin menghapus tiket ini?"):
        daftar_tiket.pop(idx)
        print(f"Tiket {tiket['kode_tiket']} dari {tiket['nama_pelapor']} "
              f"berhasil dihapus dari sistem.")
    else:
        print("Penghapusan dibatalkan.")



# Tambahan: data contoh untuk demo/pengujian (bukan fitur wajib)

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
3