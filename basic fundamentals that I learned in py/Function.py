# Learn Function on Freecodecamp
def nama_function(parameter): #def disini digunakan untuk membuat function, parameter tempat untuk menerima data ketika function di panggil
    proses # proses di sini seperti mesin yang akan memproses data nya
    return hasil  # return digunakan untuk mengembalikan hasil dari function
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#contoh Menjumlahkan 2 angka: Analogikan ini seperti dapur

def calculate_sum(a, b): # Resep Dapur. aku memberi tahu koki (fungsi) bahwa dia butuh 2 bahan dasar, yaitu a dan b.
    return a + b # Makanan Jadi yang Diserahkan. Koki memasak (menjumlahkan a + b), lalu membungkus hasilnya untuk diserahkan kembali kepada pemesan.

my_sum  = calculate_sum(3, 1) 
print(my_sum) # Memamerkan / Memakan Makanan. menampilkan isi piring tersebut ke layar.
# my_sum adalah Kotak/Piring Pengampung. aku menyiapkan piring bernama my_sum untuk menampung makanan (angka 4) yang dikembalikan oleh koki.
# calculate_sum(3, 1) adalah Proses Memesan. aku mengirim bahan 3 dan 1 ke dapur. Koki memasaknya (3 + 1 = 4).
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# return VS print()
# Tanpa return (Hanya print di dalam fungsi): Koki memasak makanan, lalu memakannya sendiri di dapur. aku di meja luar tidak mendapat apa-apa (variabel my_sum akan bernilai kosong/None).

# Menggunakan return: Koki tidak memakannya, tapi mengirimkan masakan itu ke meja Anda, sehingga hasilnya bisa disimpan di variabel my_sum untuk dipakai lagi nanti.

# singkatnya:
# 👨‍🍳 KOKI / membuat resep
def calculate_sum(a, b):
    
    # 🔥 PROSES MEMASAK
    return a + b


# 👤 PELANGGAN MEMESAN
# "Saya pesan 3 + 1"
my_sum = calculate_sum(3, 1)


# 🧑 PELANGGAN MENERIMA HASIL
# my_sum sekarang berisi 4

# 👀 MELIHAT HASIL
print(my_sum)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Function Scope 
# Scope = wilayah/tempat di mana sebuah variabel bisa diakses.
# contoh:
def masak():
    bahan = 'Tepung'
    print(bahan)
masak()

# 🌍 LUAR FUNCTION
#    │
#    │  bahan ❌ tidak dikenal
#    │
#    └── 👨‍🍳 masak()
#           │
#           └── bahan = "Tepung" ✅

# LEGB adalah urutan python mencari variabel
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

 #Contoh local:
def masak():           
    bahan = "ayam"      #Local, bahan disini 
    print(bahan) 
masak()
# Local = variabel yang berada di dalam function yang sedang dijalankan.

 #Contoh Enclosing
def dapur():            
    bahan = "ayam"      #bahan di temukan disini, di dapur()
    def masak():          
        print(bahan)    #Local tidak ada, bahan tidak ada di dalam masak()
    masak()
dapur()                 
# Makanya disebut Enclosing: scope function yang membungkus function lain.

 #Contoh Global
bahan = "ayam" #bahan terdapat di luar function 

def masak():
    print(bahan)
masak()
# Global adalah variabel yang dibuat di luar semua function.

 #Contoh Built-in
def masak():
    bahan = "ayam" 
    print(bahan)    #Built-in terletak disini
# Kalau tidak ditemukan di Local, Enclosing, atau Global, Python mencari Built-in.
# Contoh built-lainnya:
len()
sum()
max()
min()
print()
type()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Analogi Di Dapur, python mencari bahan bernama "garam"

# L — Local
# ↓
# 👨‍🍳 Meja koki sekarang
# "Apakah ada garam?"
#        ↓ tidak ada

# E — Enclosing
# ↓
# 🍳 Dapur yang membungkusnya
# "Apakah ada garam?"
#        ↓ tidak ada

# G — Global
# ↓
# 🏪 Gudang restoran
# "Apakah ada garam?"
#        ↓ tidak ada

# B — Built-in
# ↓
# 🏭 Peralatan/bahan bawaan Python

# Contoh lengkap: 
nama = "Global"

def dapur():
    nama = "Enclosing"
    def masak():
        nama = "Local"
        print(nama)
    masak()
dapur()