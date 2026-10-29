# Pertemuan 11 - Dictionary/Map

**Nama:** Muhammad Fatih Ammar  
**NIM:** 2225250135  
**Kelas:** 3E  
**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Pendidikan Matematika FKIP Untirta  
**Tahun Ajaran:** 2026/2027 Ganjil

## 1. Tujuan

Mempelajari penggunaan dictionary dalam Python untuk menyimpan data dalam bentuk pasangan key-value, mengakses dan memodifikasi data, melakukan iterasi, serta mengintegrasikan dictionary dengan list dan fungsi.

## 2. Materi yang Dipelajari

- Membuat dictionary dan pasangan key-value.
- Mengakses data menggunakan key.
- Menggunakan `get()` untuk akses yang lebih aman.
- Menambah, mengubah, dan menghapus data.
- Menelusuri dictionary menggunakan `keys()`, `values()`, dan `items()`.
- Menggunakan dictionary bersarang.
- Mengolah data menggunakan fungsi Python.
- Menguji program dan mengelola kode melalui Git dan GitHub.

## 3. Struktur Proyek

```text
pertemuan-11-dictionary-2225250135/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## 4. Program Praktik

Program utama berada pada `praktik/data_mahasiswa.py` dan menggunakan NIM sebagai key utama untuk menyimpan data mahasiswa.

Setiap mahasiswa memiliki atribut:
- Nama
- Kelas
- Nilai

Program memiliki fitur pencarian mahasiswa, penanganan NIM yang tidak ditemukan, penambahan data mahasiswa, pembaruan nilai, penampilan rekap menggunakan `items()`, dan perhitungan rata-rata nilai.

## 5. Cara Menjalankan

Pastikan Python 3 telah terpasang dan terminal berada di folder utama proyek.

Jalankan setiap latihan menggunakan perintah berikut:

```bash
python latihan/01_dasar_dictionary.py
python latihan/02_akses_get.py
python latihan/03_manipulasi_dictionary.py
python latihan/04_iterasi_dictionary.py
python latihan/05_dictionary_bersarang.py
python latihan/06_fungsi_dictionary.py
```

Untuk menjalankan program praktik:

```bash
python praktik/data_mahasiswa.py
```

## 6. Test Case

| Pengujian | Hasil yang Diharapkan |
|---|---|
| Pencarian NIM A003 | Data Citra ditampilkan |
| Pencarian NIM A999 | Pesan data tidak ditemukan |
| Pembaruan nilai A002 | Nilai Budi menjadi 82 |
| Penambahan NIM A006 | Data Fajar tersimpan |
| Rekap data mahasiswa | Seluruh NIM dan atribut ditampilkan |
| Perhitungan rata-rata | Rata-rata nilai ditampilkan dengan dua angka desimal |

Status pengujian akhir diisi berdasarkan hasil eksekusi program di VS Code.

## 7. Refleksi

Melalui praktikum ini, saya mempelajari bahwa dictionary memudahkan pencarian data berdasarkan key tanpa harus mengetahui posisi indeks seperti pada list. Penggunaan `get()` membantu menangani key yang tidak tersedia, sedangkan `items()` memudahkan penelusuran key dan value secara bersamaan. Dictionary bersarang juga dapat digunakan untuk menyimpan data mahasiswa dengan beberapa atribut secara terstruktur.

## 8. Kesimpulan

Dictionary merupakan struktur data Python yang berguna untuk mengelola data berbentuk pasangan key-value. Dengan menggabungkan dictionary, perulangan, dan fungsi, program dapat melakukan pencarian, penambahan, pembaruan, serta rekap data secara lebih terstruktur.

## 9. Referensi

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 11, Dictionary/Map dan Pasangan Key-Value, Untirta, Tahun Ajaran 2026/2027 Ganjil.
- Python Software Foundation, Python Documentation: Data Structures — Dictionaries.
