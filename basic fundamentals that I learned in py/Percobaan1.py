# # Sentiment Analysis Evaluasi Aplikasi (Kasus NLP Dasar)
# #1. data mentah:
# skor_ulasan = [5, 1, 4, 2, 5, 3, 1, 5, 2, 4]
# Total_positif = 0
# Total_negatif = 0
# skor_terendah = skor_ulasan[0]
# skor_tertinggi = 0
# nomor = 1
# skor_ulasan.append(90)

# #2. membaca data:
# for i in skor_ulasan:
#     #Mengecek data mana yang positif dan negatif
#     if i >= 4:
#         print(f"{nomor}. Ulasan Positif")
#         Total_positif += 1 #<<<=== Menghitung total Positif dan negatif

#     else:
#         print(f"{nomor}. Ulasan Negatif")
#         Total_negatif += 1 #<<<=== Menghitung total Positif dan negatif

#     #Menghitung Skor Terendah dan tertinggi
#     if i < skor_terendah:
#         skor_terendah = i

#     if i > skor_tertinggi:
#         skor_tertinggi = i

#     nomor += 1
        
# print()

# # Total ulasan positif dan negatif 
# print("======= Total ========")
# print(f"Total Positif: {Total_positif}")
# print(f"Total Negatif: {Total_negatif}")

# print()

# # Skor terendah dan tertinggi
# print("======= Skor =========")
# print(f"Skor terendah: {skor_terendah}")
# print(f"Skor tertinggi: {skor_tertinggi}")

# print()
# print("======= Total Data ========")
# print(len(skor_ulasan))

# Selisih harga prediksi (dalam juta rupiah)
#1. data selisih
selisih_harga = [5, 25, 2, 40, 12, 50, 8]
# Menghitung Total akurat
total_akurat = 0
total_meleset = 0
#Urutan Nomor
nomor = 1
# Variabel penampung  nilai terbesar dan terkecil
selisih_terbesar = selisih_harga[0]
selisih_terkecil = selisih_harga[0]
# Penampung untuk menghitung total akumilasi selisih
total_selisih = 0

#2. Mengurutkan data selisih_harga 
for selisih in selisih_harga:
#3. Mengecek apakah harga <= 10? 
    if selisih <= 10:
#4. Mencetak Prediksi akurat dan nomor memakai dict
        print(f"{nomor}. Prediksi Akurat")
#5. Total akurat += 1 
        total_akurat += 1
#6. Jika selisih nya > 10
    else:
#7. Cetak Prediksi Meleset 
        print(f"{nomor}. Prediksi Meleset")
#8. Total Meleset += 1 
        total_meleset += 1

#9. if untuk mengecek nilai terbesar dan terkecil 
    if selisih > selisih_terbesar:
        selisih_terbesar = selisih

    if selisih < selisih_terkecil:
        total_selisih += selisih_terkecil
#10. Menghitung total selisih
    total_selisih += selisih
#11. nomor += 1 untuk mengurutkan nomor 
    nomor += 1
print()
#12. di luar loop cetak total_akurat dan total meleset 
print("==== Total Akurat dan Meleset ====")
print(f"Total Akurat: {total_akurat}")
print(f"Total Meleset: {total_meleset}")
print()
# Mencetak Selisih Terbesar dan Terkecil
print("==== Selisih Terbesar dan Terkecil ====")
print(f"Selisih Terbesar: {selisih_terbesar}")
print(f"Selisih Terkecil: {selisih_terkecil}")
print()
# Mencetak rata rata dari selisih
print("==== Rata-Rata Selisih ====")
print(total_selisih // len(selisih_harga))