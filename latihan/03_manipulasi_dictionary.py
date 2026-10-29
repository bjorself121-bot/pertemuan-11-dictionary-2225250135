
# Latihan 3: Manipulasi Dictionary

data = {
    "nama": "Ammar",
    "nilai": 90
}

# Menambahkan data kelas
data["kelas"] = "A"

# Mengubah nilai mahasiswa
data["nilai"] = 90

print("Setelah ditambah dan diubah:")
print(data)

# Menghapus data kelas
data.pop("kelas")

print("Setelah kelas dihapus:")
print(data)
