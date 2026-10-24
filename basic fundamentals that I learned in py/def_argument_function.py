# def fungsi(argument = nilai defaultnya):
# contoh 1
def warung_makan(makanan = "Nasgor"): # <-- argument = nilai 
    print(f'WOiiiii {makanan}')

warung_makan("Mieayam") # <-- berfungsi untuk mengganti inputan/nilai
warung_makan() 

# contoh 2 argument 
# 2 input argument 
def makanan(warung_makan1 = "Sate", warung_makan2 = "Padang"):
    print(f"Yang enak mana ya? {warung_makan1} atau {warung_makan2}?")

makanan("Mieayam", "Nasgor") # <-- berfungsi untuk mengganti inputan/nilai
makanan()

# Contoh 3 
def hitung_pangkat(angka, pangkat = 2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(5, 3)) 

hasil = hitung_pangkat(angka = 4, pangkat = 3) # <-- merubah pangkat
print(hasil)

# hasil = hitung_pangkat(angka = 4, 3) # <-- akan error, depan nya harus ada variabel
# print(hasil)

hasil = hitung_pangkat(pangkat = 4, angka = 3) # <-- di balik inputanya
print(hasil)

# contoh 4
def liburan(kota1 = 'Bandung', kota2 = 'Jakarta', kota3 = 'Bali', kota4 = 'Tokyo'):
    hasil = kota1 + " " + kota2 + " " + kota3 + " " + kota4
    return hasil

print(liburan())
print(liburan(kota3 = 'Yogyakarta')) # <-- berfungsi untuk mengganti inputan/nilai

# NOTE: # def fungsi(argument = nilai defaultnya) ini bergunak jika kita punya argument yang banya..
# Semisal mau akses input kota2 =jakarta, kita pengen ubah jadi sukabumi
# itu tidak bisa memakai print(liburan("Sukabumi")) YANG  ADA MALAH BANDUNG KE GANTI
# jadi pake print(liburan(kota2 = Sukabumi)) nah ini baru ke gnti secara mau di akses nya