# # Fungsi *args 
# def hitung_rata_rata(*nilai: int) -> float:
#     rata_rata = sum(nilai) / len(nilai)
#     return rata_rata

# hasil = hitung_rata_rata(1,2,3,4,5,6,7,8,9,10)
# print(f"Jadi rata rata nya {hasil}")

# # parameter + *args
# def sapa_kelompok(ketua, *anggota):
#     print(f"ketua Kelompok: {ketua}")
#     print(F"anggota Kelompok: {anggota}")

# sapa_kelompok("Nasgor", "MieAyam", "Sate", "Donut", "AyamGeprek")

# # parameter + *args (kasus hitung diskon belanja)
# def hitung_total_belanja(diskon: float, *harga_barang: int):
#     awal = sum(harga_barang)
#     potongan = awal * (diskon / 100)
#     total_harga_after_diskon = awal - potongan
#     return total_harga_after_diskon

# hasil = hitung_total_belanja(10, 10000, 20000, 30000, 40000, 50000)
# print(f"jadi total harga yang harus di bayar setelah diskon adalah: {hasil}")

# # Last latihan praktek *args 
# def hitung_kasir(*harga_barang: int) -> int:
#     total_jumlah = sum(harga_barang)
#     if len(harga_barang) > 3:
#         total_akhir = total_jumlah - 5000
#     else:
#         total_akhir = total_jumlah
#     return total_akhir 

# output = hitung_kasir(10000, 20000, 30000, 10000)
# print(f"jadi total akhir yang harus di bayar adalah: {output}")

# # **Kwargs
# # tanpa **Kwargs
# def warung_makan(nama, harga, lokasi):
#     print(f"YUKKK Beli {nama} harganya {harga} dan lokasi nya juga deket lgii di {lokasi}" )

# warung_makan("Nasgor", 15000, "Samping Rumah")

# # With **Kwargs tetapi memanggil key dict
# def warung_sebelah(**menu):
#     nama = menu["nama"]
#     price = menu["price"]
#     lokasi = menu["lokasi"]
#     print(f"Nah mending ini {nama} harganya murah lagi {price} lokasi nya apalagi {lokasi}")

# warung_sebelah(nama="Mieayam", price=12000, lokasi="Samping nya abang nasgor")

# # With **Kwargs tanpa key
# def warung_sebelah(**makanan):
#     print(makanan)

# warung_sebelah(nama="Sate", harga=15000, lokasi="Depan abang nasgor")

# So Last is *args + **kwargs (Sok inglis) 
def count(*args: tuple , **kwargs: dict):
    output = 0
    if kwargs['option'] == "Plus":
        for number in args:
            output += number
    elif kwargs['option'] == "multiplication":
        output = 1
        for number in args:
            output *= number
    else:
        print("Undefined")
    return output

calculation_result = count(1,2,3,4, option="Plus")
print(f"Result Calculation of Plus: {calculation_result}")

calculation_result = count(1,2,3,4, option="multiplication")
print(f"Result Calculation of Multiplication: {calculation_result}")

calculation_result = count(1,2,3,4, option="idk")

# # Latihan **Kwargs
# def buat_pesanan_warung(nama_pelanggan: str, **pesanan):
#     print(f"=== Pesanan Atas Nama: {nama_pelanggan.upper()} ===")

#     total  = 0
#     for makanan, harga in pesanan.items():
#         print(f"*{makanan} : Rp {harga}")
#         total += harga

#     print("-"*40)   
#     print(f"Total yang harus di bayar: Rp {total} ")

# buat_pesanan_warung("Cecep", Mieayam=12000, Es_Teh=4000, Kerupuk=2000)