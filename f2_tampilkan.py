"""
f2_tampilkan.py - Fitur 2: Tampilkan Semua Tiket
"""
from data_tiket import daftar_tiket, cetak_tabel


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
