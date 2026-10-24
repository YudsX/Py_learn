# Soal Latihan 1: Hitung Diskon Belanja
def hitung_diskon(harga_total, persen_diskon):
    '''Fungsi untuk menghitung Harga total dan persen diskon'''
    potongan_harga = harga_total * persen_diskon // 100
    hasil = harga_total - potongan_harga
    return hasil 

#Memanggil fungsi nya:
harga_akhir = hitung_diskon(100000, 20)
print(harga_akhir)

# Soal Latihan 2: Cek kelulusan Nilai
def cek_kelulusan(nama, nilai):
    if nilai >= 70:
        print(f"{nama} Dinyatakan LULUS!")
    else:
        print(f"{nama} Dinyatakan TIDAK LULUS!")
    return 
    
cek_kelulusan('Yd', 80)
print(cek_kelulusan)

cek_kelulusan('Rachell', 69)
print(cek_kelulusan)

# Soal 3: Hitung Rata-Rata & Kelulusan Kelas
def analisis_kelas(daftar_nilai):
    '''Perbaikan Taro lulus = 0'''
    lulus = 0
    for i in daftar_nilai:
        if i >= 70:
            lulus += 1 # Menambah hitungan jika nilainya >= 70

    return f"Dari {len(daftar_nilai)} siswa, ada {lulus} siswa yang LULUS!"

# List daftar nilai 
daftar_nilai = [90, 80, 100, 70, 60, 30, 40]

# Memanggil hasil 
hasil = analisis_kelas(daftar_nilai)
print(hasil)

# Soal latihan 4: Improve soal 3 yang salah
def filter_username(pendaftar: list) -> list:
    username_valid = []
    for i in pendaftar:
        if len(i) >= 5 and len(i) <= 12:
            username_valid.append(i)
    return username_valid    

# List pendaftar 
pendaftar = ["Yudi", "Wira", "Asep123", "RezaKecap11122222", "AtmaKnalpot", "BayuNgawi", "FarhanKebabAsliNgajukLOhyahhh"]

# Memanggil Hasil filter
hasil_filter = filter_username(pendaftar)
print(hasil_filter)

# Soal Latihan: *args 
def hitung_total(*harga):
    # *harga disini akan di ubah menjadi tuple, yang isinya semua input yang dimasukan
    total = sum(harga)
    return f"Jadi TOTAL: {total}"

print(hitung_total(10000, 20000))
print(hitung_total(900000, 1000000))

# Soal Latihan: **kwargs 
def cek_biodata(**biodata):
    # data disini berubah menjadi Dictionary
    for kunci, data in biodata.items():
        print(f"{kunci.capitalize()}: {data}")
    return

# Memanggil fungsi dengan input berlabel:
cek_biodata(nama = "Yudi", Jurusan = "Informatics Engineering", kota = "Sukabumi")

# Soal Latihan: Func dengan Dictionary 
def format_biodata_Belanjaan(**data):
    for kunci, nilai in data.items():
        print(f'{kunci.capitalize()}: {nilai}')

format_biodata_Belanjaan(product = "Mie Indomie", price = 7500, send = "Kalimantan Kopdes", total_kemasan = 10000)

# -----------------------------------------------------------------------------------------------------------------------------
''' Type hints pada function '''
# bentuk standar fungsi yang udah kita pelajari
'''
   Studi kasus:
def fungsi(parameter):
    hasil = parameter ** 2
    print(hasil) 

fungsi(10)
fungsi("Nasgor")  # ---> gabisa
fungsi(True)
'''

# Penggunaan Type Hints 
def pangkat_lima(argument:int) -> int:
    '''FUNGSI DENGAN HINTS '''
    out = 5 ** argument
    return out

HASIL = pangkat_lima("Mie ayam") # -> jadi kita tahu argumentnya type apa dan tahu yang di inginkan oleh fungsi yang kita buat
print(HASIL)

# Type hints ini agar rapih secara dokumentasi

# Hints Tanpa return
import string
import os
def display(argument: string) -> string:
    print(argument)

display("Nasgor")
hasil = os.system("clear") # so at least si os system ini akan me return sebuah nilai ke (hasil)
print(hasil)