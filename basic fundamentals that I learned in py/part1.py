# # 1. Minta input dari user (misal: kalimat/kata favorit mereka)
# kata_kalimat = input("masukan kata favorit mu ^_^ : ")
# hitung = 0
# # 2. Buat 'for loop' yang berjalan sebanyak 5 kali (pakai range)
# #    Di DALAM loop: cetak variabel kata tersebut ke layar

# for fav in range(5):
#     hitung += 1
#     print(f"Perulangan ke-{hitung}: {kata_kalimat}")

# print("=== Daftar Belanjaan Kopdes ===")
# # 1. Memasukan nama barang 3 bebas
# daftar_belanjaan = []

# # 2. barang langsung otomatis masuk ke dalam list
# for x in range(3):
#     label = input("Nama Barang: ")
#     daftar_belanjaan.append(label)

# print()
# # 3. nampilin isi dari daftar belanjaan nya
# print("--- Daftar Belanjaan kamu ---")
# hitung = 0
# for data in daftar_belanjaan:
#     hitung += 1
#     print(f"{hitung}.{data}")

#KASIR TOKO KOPI
# print("=== Toko Kopi selamet === ")
# print()
# harga_kopi = int(input("Masukan harga Kopi: "))
# jumlah_cangkir = int(input("Jumlah cangkir: "))
# print()
# print("=== Total yang harus di bayar === ")
# print()
# total = harga_kopi * jumlah_cangkir

# if total > 50000:
#     print("Selamat Anda dapat diskon!!")
#     total = total - 10000 

# else:
#     print("Tidak ada potongan, total tetap utuh")
# print()
# print(total)

# #Menentukan siswa remed atau tidak berdasarkan nilai nya
# #masukan input dari user nilai
# nilai_siswa = int(input("Masukan nilai siswa: "))

# #menentukan remed atau tidak berdasarkan nilainya
# if nilai_siswa >= 90:
#     print("Kamu lulus dengan nilai A!!")

# elif nilai_siswa >= 70:
#     print("Kamu lulus!!")

# else:
#     print("Maaf lu remed")

#Kasir Serba ada

# print("=== Kasir Serba diskon meriah!! ===")

# #menampung total barang jumlah
# total_belanja = 0

# for total in range(3):
#     harga = int(input("Masukan Harga Barang: "))
#     total_belanja = total_belanja + harga

# if  total_belanja > 100000:
#     total_belanja = total_belanja - 15000
#     print()
#     print("Dapat Diskon!")

# else:
#     print("Tidak Dapat Diskon Maaf")

# print()
# print("--- TOTAL YANG HARUS DI BAYAR ---")
# print(total_belanja)

# def sapa_user(nama, peran):
#     print(f"Halo {nama}, selamat bertugas sebagai {peran}!")

# # Cara Panggil:
# user1 = sapa_user("Budi", "Kasir")
# user2 = sapa_user("Alex", "Ojol")
# user3 = sapa_user("Gilang", "Kang Paket")
# # Output: Halo Budi, selamat bertugas sebagai Kasir!

# 1. Mendefinisikan Fungsi Hitung Belanja
# def proses_transaksi(jumlah_barang):
#     total_belanja = 0

#     # Looping input harga barang
#     for i in range(jumlah_barang):
#         harga = int(input(f"Masukkan harga barang ke-{i+1}: "))
#         total_belanja += harga

#     # Logika Cek Diskon
#     if total_belanja > 100000:
#         diskon = 15000
#         total_akhir = total_belanja - diskon
#         print("\n🎉 Selamat! Anda mendapatkan diskon Rp 15.000")
#     else:
#         total_akhir = total_belanja
#         print("\nBelanjaan belum mencapai Rp 100.000 untuk dapat diskon.")

#     return total_akhir

# # ==========================================
# # 2. Program Utama (Main Program)
# # ==========================================
# print("=== SISTEM KASIR TOKO KOPI SELAMET ===")

# # Memanggil fungsi untuk Pelanggan 1
# total_bayar_pembeli1 = proses_transaksi(3)
# total_bayar_pembeli2 = proses_transaksi(3)
# total_bayar_pembeli3 = proses_transaksi(3)

# print("--------------------------------------")
# print(f"TOTAL AKHIR HARUS DIBAYAR: Rp {total_bayar}")
# print("--------------------------------------")

#inputan Panjang dan lebar nya:
# def hitung_luas(panjang, lebar):
#     luas = panjang * lebar
#     return luas

# hasil = hitung_luas(10, 5)

# print("--- Hasil Luas!!! ---")
# print(hasil)

# def cek_lulus(nilai):
#     if nilai >= 70:
#          return "Lulus!, selamatt"
#     else:
#         return "remidi"

# status = cek_lulus(60)
# print("=== Kamu di nyatakan! ===")
# print(status)

# def hitung_total_belanja():
#     total = 0

#     for x in range(3):
#         harga = int(input("Masukan harga barang: "))
#         total = total + harga

#     return total

# total_bayar = hitung_total_belanja()
# print(total_bayar)

# def hitung_total_nilai():
#     total_nilai = 0 

#     for i in range(3):
#         nilai = int(input("Masukan Nilai rata rata: "))
#         total_nilai += nilai

#     return total_nilai

# hasil = hitung_total_nilai()
# print(hasil)

