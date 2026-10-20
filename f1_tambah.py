"""
f1_tambah.py - Fitur 1: Tambah Tiket Baru
"""
from data_tiket import daftar_tiket, JENIS_VALID, PRIORITAS_VALID, cari_indeks_kode, normalisasi_pilihan


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
