"""
f5_filter.py - Fitur 5: Filter Tiket Berdasarkan Jenis Masalah
"""
from data_tiket import daftar_tiket, JENIS_VALID, normalisasi_pilihan, cetak_tabel


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
