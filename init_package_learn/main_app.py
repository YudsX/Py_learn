import module_init  # mencari isi dari package dari module init
import os

os.system('cls')
# cara biasa tanpa import all
# ini cara 1
result_kali = module_init.matem.kali(1,2,3,5,6,7,7,8,9)
print(f"Hasil dari kali = {result_kali}")

# ini cara 2
result_plus = module_init.tambah(1,2,3,5,6,7,7,8,9)     # <- tanpa harus memanggil module
print(f"Hasil dari tambah = {result_plus}")

# cara dengan import all 
from module_init import *

# ini cara 1
result_kali = matem.kali(1,2,3,5,6,7,7,8,9)
print(f"Hasil dari kali = {result_kali}")

# ini cara 2
result_physic = physic.gaya(9, 2)
print(f"Hasil dari pisika = {result_physic}")

# ini cara chaining
import module_init

result_kali = module_init.kali(1,2,3,5,6,7,7,8,9)
print(f"Hasil dari kali = {result_kali}")

result_plus = module_init.tambah(1,2,3,5,6,7,7,8,9)
print(f"Hasil dari tambah = {result_plus}")

result_physic = module_init.gaya(9, 2)
print(f"Hasil dari pisika = {result_physic}")

# ini cara kalau mau lebih dalam
from module_init import physic

result_physic = physic.gaya(9, 2)
print(f"Hasil dari pisika = {result_physic}")

