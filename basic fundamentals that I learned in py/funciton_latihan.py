# def nama_fungsi(parameter):
#     badan fungsi

# Contoh String
def warung(makanan):
    print(f"Woiii {makanan}")

warung("Nasgor")
warung("Mieayam")
warung("Sate")

# Contoh Penjumlahan
def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(8, 1)
tambah(999999999, 1)

#Contoh list
def warung_makan(makan):
    for makanan in makan:
        print(f"Aku mau makan ini: {makanan}")

list_menu = ["Mieayam", "Nasgor", "Sate", "Padang"]
warung_makan(list_menu)

# return 
# Kembalian dalam Python function
# Rumus nya seperti:
# def fungsi(parameter/input):
    # badan fungsi
    # return output
# y = f(x) ---> hasil dari f(x) akan di kembalikan ke y 
# Contoh:
def bilangan(angka):
    output_angka = angka // 2
    return output_angka

y = bilangan(90) #<-- bisa mengeluarkan kaya gini
print(y)

print(bilangan(30)) #<-- atau bisa kaya gini

z = 2 ** bilangan(10) #<-- atau terakhir bisa kaya gini
print(z)
print()

# bisa nambahin input/parameter lebih dari 1:
def hitung_luas(luas_a, luas_b):
    total_luas = luas_a * luas_b
    return total_luas 
    
hasil_luas = hitung_luas(9, 7)
print(hasil_luas)
print()

# Contoh langsung return dan multi input/parameter
def kali(num1, num2):
    return num1 * num2

y = kali(10, 2)
print(y)
print()

# fungsi dengan return banyak sekaligus
def operasi_matematika(bil_1, bil_2):
    kali = bil_1 * bil_2
    division = bil_1 / bil_2
    tambah = bil_1 + bil_2
    kurang = bil_1 - bil_2
    floordivision = bil_1 // bil_2
    pangkat = bil_1 ** bil_2

    return kali,division,tambah,kurang,floordivision,pangkat

y,u,d,h,a,s = operasi_matematika(10, 5)
print(f"Hasil dari kali: {y}")
print(f"Hasil dari division: {u}")
print(f"Hasil dari tambah: {d}")
print(f"Hasil dari kurang: {h}")
print(f"Hasil dari floor division: {a}")
print(f"Hasil dari pangkat: {s}")

# y = f(x)
# Mencari angka terbesar menggunakan func, return, loops
def cari_angka_terbesar(angka: int) -> int:
    terbesar = angka[0]

    for i in angka:
        if i > terbesar:
            terbesar = i 

    return terbesar

list_num = [10, 30, 40, 70, 1, 2, 100]
hasil = cari_angka_terbesar(list_num)
print(hasil)
print(cari_angka_terbesar ([10, 90, 1000000, 20, 900000, 90000000000000]))
print(cari_angka_terbesar([1, 3, 6, 7, 5, 3, 2]))
# print()

# Latihan di Freecodecamp
def apply_discount(price: int, discount: float) -> int:
    if type(price) != int and type(price) != float:
        return 'The price should be a number' 
    if type(discount) != int and type(discount) != float:
        return 'The discount should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    final_price = price - (price *(discount / 100))
    
    return final_price
        
y = apply_discount(100, 20)
print(y)
print(apply_discount(50, 0))
print(apply_discount(100, 0))

