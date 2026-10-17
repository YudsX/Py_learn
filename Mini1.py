#warna = ["kuning", "hijau", "merah"]
#print(warna[2])

#nama = input("masukan nama: ")
#print("halo,", nama)

#perulangan dengan while 
#angka = 1

#while angka <= 10:
    #print(angka)
    #angka += 1

#angka = 1

#while angka <= 5:

    #if angka == 3:
        #angka += 1
        #continue

    #print(angka)
    #angka += 1

#data = 0 

#while data <= 10:
    #ata += 1

    #if data == 3:
        #continue
    #print(data)
   
#else: 
    #print("data yang tidak tersedia di skip!")

#Dummy bab Python list 
#buah = ["apel", "jeruk"]
#buah.append("mangga")
#print(buah)

#angka = [10, 20]
#angka.append(30)
#angka[0] = 100

#print(angka)

#ai = ["Python"]

#ai.append("AI")
#ai.append("Machine Learning")

#print(ai)

#kota = ["Jakarta", "Bandung"]

#kota.append("Surabaya")
#kota[1] = "Yogyakarta"

#print(kota)

#buah = ["Apel", "Jeruk", "Mangga"]

#hasil = buah.pop()

#print(hasil)
#print(buah)


#PERBANDINGAN ANTARA FOR LOOPS DAN WHILE LOOPS
#buah = ["Apel", "Jeruk", "Mangga"]

#for kotak_buah in buah:
    #print(kotak_buah)

#buah = ["Apel", "Jeruk", "Pisang"]
##i = 0  # Harus bikin variabel penanda manual

#while i < len(buah):
    #print(buah[i])
    #i += 1  # Harus nambahin hitungan manual. Kalau lupa, bakal loop selamanya!

#LIST BERDASARKAN MENGGUNAKAN NOMOR
#buah = ["Apel", "Jeruk", "Mangga"]

#for kotak_buah in buah:
    #f kotak_buah == "Apel":
        #print("1.", kotak_buah)

    #if kotak_buah == "Jeruk":
        #print("2.", kotak_buah)

    #if kotak_buah == "Mangga":
        #print("3.", kotak_buah)

# Perkalian 1 sampai 3
#for baris in range(1, 4):  # Angka pertama
    #for kolom in range(1, 4):  # Angka kedua
        #hasil = baris * kolom
        #print(f"{baris} x {kolom} = {hasil}")

    #print("----------------")  # Pemisah antar kelompok perkalian

#LIST SORTED 
angka = [10, 3, 7, 1, 9]

hasil = sorted(angka, reverse=True)

print(hasil)
print("----------")

#LIST SORT
buah = [10, 3, 7, 1, 9]

buah.sort(reverse=True)
print(buah)