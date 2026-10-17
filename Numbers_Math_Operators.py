# type() digunakan untuk mengetahui jenis dari isi sebuah variabel
int_positif = 56
int_negatif = -4

print(type(int_positif)) # <class 'int'>
print(type(int_negatif)) # <class 'int'>

# contoh dari penjumlahan dengan operatos +
int_positif1 = 56
int_positif2 = 12

hasil = int_positif1 + int_positif2
print('Hasil penjumlahan:', hasil) # Hasil penjumlahan: 68

# Contoh dari pengurangan -
int_positif1 = 56
int_positif2 = 12

hasil = int_positif1 - int_positif2
print('Hasil pengurangan:', hasil) # Hasil pengurangan: 44

# Contoh dari perkalian *
int_positif1 = 56
int_positif2 = 12

hasil = int_positif1 * int_positif2
print('Hasil perkalian:', hasil) # Hasil perkalian: 672

# Contoh dari pembagian atau division /
# disini hasil nya akan berupa float atau desimal... 
int_positif1 = 56
int_positif2 = 12

hasil = int_positif1 / int_positif2
print('Hasil pembagian:', hasil) # Hasil pembagian:  4.666666666666667

# Ini adalah bilangan float atau desimal 
float1 = -12.0
float2 = 4.9

print(type(float1)) # <class 'float'>
print(type(float2)) # <class 'float'>

# Contoh penjumlahan dengan bilangan float, jika bil positif + dengan float.
float_1 = 5.4
float_2 = 12.0

Hasil_float = float_1 + float_2
print('Hasil Float:', Hasil_float) # Hasil Float: 17.4

# Contoh pengurangan dengan bilangan float, jika bil positif - dengan float. 
float_1 = 5.4
float_2 = 12.0

Hasil_float = float_1 - float_2
print('Hasil Float:', Hasil_float) # Hasil Float: -6.6

# Contoh perkalian dengan bilangan float, jika bil positif * dengan float. 
float_1 = 5.4
float_2 = 12.0

Hasil_float = float_1 * float_2
print('Hasil Float:', Hasil_float) # Hasil Float: 64.80000000000001

# Contoh pembagian dengan bilangan float, jika bil positif / dengan float. 
float_1 = 5.4
float_2 = 12.0

Hasil_float = float_1 / float_2
print('Hasil Float:', Hasil_float) # Hasil Float: 0.45

# Jika disini mau menambahkan bilangan bulat dan float, hasilnya secara otomatis dikonversi jadi float:
bil_int = 56
bil_float = 5.4

positif_float = bil_int + bil_float

print(positif_float) # 61.4
print(type(positif_float)) # <class 'float'>

# Operator modulo () mengembalikan sisa ketika nilai di sebelah kiri dibagi dengan nilai di sebelah kanan:%
# misal :
int1 = 56
int2 = 12

ini_float1 = 5.4
ini_float2 = 12.0

int_hasil = int1 % int2
floats_hasil = ini_float2 % ini_float1
print('Hasil dari int Modulo:', int_hasil) # Hasil dari int Modulo: 8
print('Hasil dari float Modulo:', floats_hasil) # Hasil dari float Modulo: 1.1999999999999993

# floor division // sama seperti pembagian sebelum nya, namun floor division hasil nya akan berupa bilangan bulat.
int1 = 56
int2 = 12

ini_float1 = 5.4
ini_float2 = 12.0

int_hasil = int1 // int2
floats_hasil = ini_float2 // ini_float1
print('Hasil dari int Modulo Floor Division:', int_hasil) # Hasil dari int Floor Division: 4
print('Hasil dari float Floor Division:', floats_hasil) # Hasil dari float Floor Divison: 2.0

# round(): Membulatkan angka dengan jumlah angka desimal yang ditentukan. Secara default fungsi ini membulatkan ke bilangan bulat terdekat, dan mengembalikan angka bulat tanpa angka desimal:
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3

# abs(): mengembalikan nilai mutlak dari sebuah angka
num = -15

absolute_value = abs(num)
print(absolute_value) # 15

# pow(): menaikkan sebuah angka ke pangkat angka lain atau melakukan eksponensiasi modular.

# pow(base, exp, mod)
# base: Angka dasar.
# exp: Pangkat / eksponen.
# mod (opsional): Angka pembagi untuk mengambil sisa hasil bagi (modulus). Jika diisi, Python akan menghitung (base ** exp) % mod dengan cara yang lebih efisien.

result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3