# Function Global and Local Scope
makanan_global = "Nasgor" # <- Ini variabel global 

# Akses variabel global ke dalam fungsi
def fungsi():
    '''Menampilkan variabel global'''
    print(f"Aku mau beli {makanan_global} nanti!")

fungsi()

# Akses variabel global ke loops
for i in range(1,6):
    print(f"Qeueu {i} - {makanan_global}")

# Akses variabel global ke booleans
if True:
    print(f"Aku Nak {makanan_global}!")

## Contoh 1: Variabel Local Scope
def fungsi2():
    makanan_local = "Mieayam" # <- Varibel Local Scope

fungsi()
# print(makanan_local) # -> tidak bisa di akses

# Contoh 2: merubah variabel global
numbers = 1000000000
eat = "Satay"
float = 7.8

def change(new_numbers, new_eats, new_float):
    '''Fungsi Mengakses ke Global'''
    global numbers # <- Fungsi Global untuk mendapat akses merubah value variabel dari numbers
    global eat
    global float

    numbers = new_numbers 
    eat = new_eats
    float = new_float

print(f"Before {numbers} - {eat} - {float}")
change(1, "Bumbu sate Khas Kebumen", 10)
print(f"After {numbers} - {eat} - {float}")

# Contoh 3: Perulangan (for/while) & Kondisi (if) ga perlu memakai 'global' untuk mengakses variabel global 
numberst =  0 # <- Variabel global

for i in range(1, 6): # <- for loop BISA langsung membaca & MENGUBAH variabel global
    numberst += 1 
    numberst_dummy = 0 # <- mengakses global 

print(f"Number Loops: {numberst}") # Output nya akan 5
print(f"Number dummy Loops: {numberst_dummy}")

if True: 
    numberst = 10
    numbers_dummy = 1

print(f"Number if booleans: {numberst}")
print(f"Number dummy if booleans: {numbers_dummy}")