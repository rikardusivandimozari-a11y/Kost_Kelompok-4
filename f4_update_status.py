"""
f4_update_status.py - Fitur 4: Update Status Tiket
"""
from data_tiket import cari_indeks_kode, daftar_tiket, ALUR_STATUS, minta_konfirmasi


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
