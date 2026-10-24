# # Module ngitung_ngitung dengan import

# def plus(*args):
#     hasil = 0
#     for i in args:
#         hasil += i
    
#     return hasil 

# def kali(*args):
#     hasil = 1
#     for i in args:
#         hasil *= i
    
#     return hasil

# def kuadrat(i: int):
#     return lambda numbers : numbers ** i

# Example first def in my brain
# fun merujuk ke makan(-> makanan: type hints of (Nasgor))

import string
def makan(makanan: str, name: str):
    print(f"aku nak makan {makanan} di tempat makan pak {name}")

makan("Nasgor", "Mas Rusdi")

# Example of args*
def menu(*tempat_makan):
    return tempat_makan

list = ["Mieayam", "Nasgor", "Sate", "Soto"]
print(list)

# Example of Kwargs**
def menu(**tempat_makan2: str):
    return tempat_makan2

list_dic = menu(tempat= "Warung King Nasir", makan= "Sate")
print(list_dic)

# # Example of *args and **Kwargs
# def menu_dan_pelanggan(*pelanggan: tuple, **list_menu: dict):
#     print("=== List pendataan menu yang ada dan pelanggan")
#     nomor = 0

#     for 
#         for pelanggan