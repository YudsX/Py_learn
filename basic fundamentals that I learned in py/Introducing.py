# #Type data dalam Python
# data0 = 10
# print(type(data0))

# data1 = "Nasgor"
# print(type(data1))

# data2 = 8.50
# print(type(data2))

# data3 = True
# print(type(data3))

# data4 = {"name": 'Rize', 'age': 25}
# print(type(data4))

# data5 = (10, "Nasgor", 9.0)
# print(type(data5))

# data6 = ["Yudha", "Rize", "Nasgor"]
# print(type(data6))

# data7 = None
# print(type(data7))

# #Split() digunakan jika ingin memisah kan sesuatu di dalam str
# nama = "Yudha ELiza Rize"

# split_nama = nama.split()
# print(split_nama)

# #Join() kebalikan dari split, untuk menghubungkan str 
# nama = ["Aku Rize dan Eliza"]

# join_nama = ''.join(nama)
# print(join_nama)

# #startswith() untuk menemukan data depan apakah benar atau tidak, kalo benar True, kalo salah False
# link = "https:///09w447t52987t548925t184598743"
# print(link.startswith(("https")))

# #endswith() Kebalikan dari startswith, yaitu menemukan data yang belakang benar atau tidak
# file = "spidermanPic.png"
# print(file.endswith("png"))

# find() dan index()
#keduanya di gunakan ketika ingin mencari posisi (index)
# nama = "Yudha"
# ini_find = nama.find("Y")
# ini_Index = nama.index("Y")

# print(ini_find)
# print(ini_Index)

#Yang terjadi jika tidak di temukan 

# nama = "Wira"
# this_find = nama.find("L")
# this_index = nama.index("L")

# print(this_find)
# print(this_index)

#Hasil nya find akan menghasilkan -1, dan index akan error..

# count() adalah menghitung berapa kali jumlah suatu elemen, karakter, 
# atau kata muncul dalam sekumpulan data (lis, tuple, string, database)

# contoh = "My Nasgor kesayangan and My World Eliza"

# #Menghitungg berapa kali kata "My" Muncul:
# hitung_kalimat = contoh.count("My")
# print(hitung_kalimat)

# capitalize() digunakan ketika ingin mengubahh huruf pertama dari sebuah teks(string)
# menjadi huruf besar(kapital), dan mengubah seluruh huruf sisanya menjadi kecil

# makanan = "nasgor"
# ubah_jadiCapitalize = makanan.capitalize()
# print(ubah_jadiCapitalize)

# isupper dan islower digunakan untuk memeriksa status huruf kapital(besar) atau kecil dalam string 
# benda = "laptop"
# ini_isupper = benda.isupper()
# ini_islower = benda.islower()

# print(ini_isupper) #akan menghasilkan false karena huruf bukan kapital
# print(ini_islower) #akan menghasilkan True karena huruf adalah kecil 

# title() digunakan ketikan ingin mengubah huruf kecil dalam string menjadi kapital per kata...
# my_dream = "found my eliza"

# ubah_title = my_dream.title()
# print(ubah_title)