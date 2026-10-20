"""
f6_hapus.py - Fitur 6: Hapus Tiket
"""
from data_tiket import daftar_tiket, cari_indeks_kode, minta_konfirmasi


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
