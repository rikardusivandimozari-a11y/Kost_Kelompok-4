# Sistem Helpdesk / Tiket Layanan

Project Semester Algoritma dan Struktur Data, Sistem Informasi FTI Unmer Malang (Semester 3, TA 2026/2027)
Dosen Pengampu: Amadea Permana Sanusi, S.Tr.T., M.Tr.Kom

## 1. Nama & Anggota Kelompok

**Sistem:** Sistem Helpdesk / Tiket Layanan (Tema 4)
**Kelompok:** [isi nama kelompok]

| No | Nama | NIM |
|----|------|-----|
| 1 | [Rikardus Ivandi Mozary]| [25083000068] |
| 2 | [Yohanes Prasetiawan Kam] | [25083000047] |
| 3 | [Benediktus Fachrizal Juantino] | [25083000028] |
| 4 | [Adao Query Hornay Cabral] | [NIM] |
| 5 | [Frederico Agostinho Coelho] | [NIM] |

## 2. Deskripsi Sistem

Sistem ini adalah aplikasi terminal (CLI) berbasis Python untuk membantu staf helpdesk mengelola tiket laporan masalah dari pengguna. Staf dapat mencatat, menampilkan, mencari, memperbarui status, memfilter, dan menghapus tiket. Pada Tahap 1, data tiket disimpan sebagai Array of Struct (list of dict) di memori, sehingga data hilang saat program ditutup.

## 3. Cara Menjalankan

Persyaratan: Python 3.8 atau lebih baru (tanpa library eksternal).

```bash
git clone https://github.com/[README]/asd-project-helpdesk-[kelompok1].git
cd asd-project-helpdesk-[kelompok]
python main.py
```

Tips: pilih menu **7** untuk memuat data contoh saat demo.

## 4. Fitur yang Sudah Ada (Tahap 1: Array & Struct)

1. **Tambah tiket baru**: validasi kode unik dan tidak kosong, nama dan deskripsi tidak kosong, jenis masalah (Hardware/Software/Jaringan/Lainnya) dan prioritas (Rendah/Sedang/Tinggi) tidak case sensitive. Status awal otomatis "Menunggu".
2. **Tampilkan semua tiket**: tabel dengan penanda visual prioritas dan status, plus ringkasan jumlah per status.
3. **Cari tiket**: berdasarkan kode (exact match) atau nama pelapor (partial match, tidak case sensitive).
4. **Update status tiket**: alur satu arah Menunggu, Diproses, Selesai, dengan konfirmasi y/n.
5. **Filter tiket** berdasarkan jenis masalah.
6. **Hapus tiket**: hanya untuk status Selesai, dengan konfirmasi y/n.

## 5. Pembagian Tugas

| Anggota | Tugas |
|---------|-------|
| [Rikardus Ivandi Mozary] (Ketua) | Setup repository GitHub, struktur project, menu utama `main.py`, integrasi antar modul |
| [Yohanes Prasetiawan Kam] | Fitur 1 (Tambah tiket) beserta seluruh validasinya |
| [Benediktus Fachrizal Juantino] | Fitur 2 (Tampilkan semua tiket) dan Fitur 3 (Cari tiket) |
| [Adao Query Hornay Cabral] | Fitur 4 (Update status tiket) dan Fitur 5 (Filter tiket) |
| [Frederico Agostinho Coelho] | Fitur 6 (Hapus tiket), pengujian seluruh fitur, dan dokumentasi README |

## Struktur Folder

```
├── main.py     # Entry point dan menu utama
├── tiket.py    # Data tiket (Array of Struct) dan 6 fitur Tahap 1
└── README.md
```
