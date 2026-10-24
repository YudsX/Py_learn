from collections import Counter

list_daftar_nama = ["Ucup", "dimas", "asep", "rusdi", "rusdi", "anton"]

# contoh tanpa memakai counter
count = 0
for i in list_daftar_nama:
    if i == "rusdi":
        count += 1

print(f"hasil muncul nya nama yang lebih: {count}")

# memakai counter
hasil_count = Counter(list_daftar_nama)
print(f"Hasil menggunakan counter: {hasil_count}")      # <- hasil berupa dictionary

print(f"Hasil menggunakan counter tanpa dict untuk mencari jumlah rusdi: {hasil_count['rusdi']}")