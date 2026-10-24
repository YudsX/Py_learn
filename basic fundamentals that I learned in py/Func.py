# 1. Kita buat fungsi yang menerima SATU bahan saja, yaitu jenis pembelinya
def cek_tempat_makan(kategori_pembeli):
    if kategori_pembeli == "padang":
        return "tempat makan orang padang"
    else:
        return "resto nya untuk orang luar"

# 2. Kita buat variabel penentu pilihan (misal kita isi "padang")
pilihan_user = "padang"

# 3. Logika IF untuk mengecek pilihan
if pilihan_user == "padang":
    print(cek_tempat_makan("padang"))
else:
    print(cek_tempat_makan("luar"))

#LIST OF NUMBERS
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

