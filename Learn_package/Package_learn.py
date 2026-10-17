import time    # <- import time disini aku mencoba untuk mengukur kecepatan antara pake _pycache_ dan antara tidak

t_start = time.time()     # <- untuk memulai waktu
import contoh_package.contoh_file

hasil_tambah = contoh_package.contoh_file.tambah(1,2,3,4,5)
print(f"Ini hasil tambah = {hasil_tambah}")

hasil_kali = contoh_package.contoh_file.kali(1,2,3,4,5)
print(f"Ini hasil kali = {hasil_kali}")

hasil_pangkat = contoh_package.contoh_file.pangkat(1,2,3,4,5)
print(f"ini hasil pangkat = {hasil_pangkat}")

# This DSA(recursion problem solv)
hasil_rekursi = contoh_package.contoh_file.factorial(5)
print(f"ini hasil dari rekursi pada struktur data = {hasil_rekursi}")
t_end = time.time()     # <- untuk mengakhiri pengukuran hasil waktu eksekusi program

print(f"waktu eksekusi program adalah: {t_end - t_start }")     #<-- Output hasil dari pengukuran waktu cepat atau lambat nya program di eksekusi

# ini contoh 2 latihan import package
import contoh_package.contoh2_file_latihan

final = contoh_package.contoh2_file_latihan.cek_angka(5)
print(f" Hasil ganjil-genap = {final}")

final = contoh_package.contoh2_file_latihan.konversi_suhu(5)
print(f" Hasil setelah di konversi = {final}")

final = contoh_package.contoh2_file_latihan.count(10, 10, "*")
print(f" Hasil dari perkalian sederhana perkalian = {final}")

# IMPORT FROM
from contoh_package.contoh2_file_latihan import count
ini_count = count(10, 2, "*")
print(f"Ini hasil dari import from division =  {ini_count}")