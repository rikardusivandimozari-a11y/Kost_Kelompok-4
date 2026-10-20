"""
f3_cari.py - Fitur 3: Cari Tiket
"""
from data_tiket import daftar_tiket, cari_indeks_kode, cetak_tabel, cetak_detail


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
