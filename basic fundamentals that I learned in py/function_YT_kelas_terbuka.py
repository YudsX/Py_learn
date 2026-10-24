# # #latihan fungsi/function
# import os
# # program menghitung luas dan keliling persegi panjang
# os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input('Masukan Angka Lebar: '))
# PANJANG = int(input('Masukan Angka Panjang: '))

# # Program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2*(PANJANG * LEBAR)

# # Tampilakan hasilnya
# print()
# print(f"Hasil dari perhitungan Luas = {LUAS}")
# print(f"Hasil dari perhitungan Panjang = {PANJANG}")

import os 

# #Bagian Header function 1
def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def pilihan_menu(): # Opsi milih buat user
    user_input = input("Mau Hitung apa? (Luas/Keliling): ")
    pilihan_user_input = user_input.lower()
    return pilihan_user_input

def input_user(): # Mengambil input user
    lebar = int(input('Masukan Angka Lebar: '))
    panjang = int(input('Masukan Angka Panjang: '))
    return lebar, panjang 

def hitung_luas(lebar, panjang): # Menghitung luas 
    return lebar * panjang

def hitung_keliling(lebar, panjang): # Menghitung Keliling 
    return 2*(lebar + panjang)

def display(message, value): # Menampilkan Hasil
    print(f"hasil dari hitungan {message} adalah {value}")

# Program Utamanya
while True:
    header()      
    # # Pr Hitung luas atau keliling nya (opsi)
    opsi = pilihan_menu()
    if opsi == 'luas':
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR, PANJANG)
        display("Luas", LUAS)
    elif opsi == 'keliling':
        LEBAR, PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display("Keliling", KELILING)  
    else:
        print("PILIH SALAH SATU WOIII!!!")

    is_done = input("Mau lanjut Kaga? (Gas lanjut / Engga): ").lower()
    if is_done == 'engga':
        break

print("\n Program Selesai! Hatur Nuhunn ^_^")