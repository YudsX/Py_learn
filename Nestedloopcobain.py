# List nilai untuk 3 siswa (Siswa 1, Siswa 2, Siswa 3)
# daftar_nilai = [
#     [80, 90, 85],  #Nilai siswa 1 
#     [70, 75, 80],  #Nilai siswa 2
#     [95, 100, 90]  #Nilai siswa 3
# ]
# #nomor urutan
# nomor_siswa = 1

# #membaca dan mencocokan siswa dan nilai nya masing-masing
# for siswa in daftar_nilai:
#     print(f"=== siswa {nomor_siswa} ===")
    
#     total_nilai_siswa = 0
#     # Agar nomor urutnya bertambah
#     nomor_siswa += 1
#     for nilai_siswa in siswa:
#         print(f"Nilai: {nilai_siswa}")
# # Menghitung total nilai
#         total_nilai_siswa += nilai_siswa

# #output
# print(f"Total nilai: {total_nilai_siswa}\n")

# Nyoba
# daftar_pesan = [
#     "Menang hadiah gratis klik disini",
#     "Halo besok kita meeting jam 9",
#     "pinjaman cepat cair tanpa jaminan"
# ]

# kata_spam = ["gratis", "pinjaman", "cair"]

# #loops luar
# for i in daftar_pesan:
#     jumlah_kata_spam = 0
#     print(f"MEMERIKSA: {i}")
#     #loop dalam 
#     for kata in kata_spam:
#         if kata in i:
#             print(f"-> Terdeteksi kata spam: {kata}")
#             jumlah_kata_spam += 1
# #di luar loop
#     if jumlah_kata_spam > 0:
#         print(f"Hasil: PESAN SPAM (ditemukan {jumlah_kata_spam} kata spam)\n")
#     else:
#         print("Hasil: PESAN HAM / AMAN\n")

#Nyoba kerjain Sendiri
#Rak buku, mencari buku Math dan ngoding
rak_buku = [
    ["Buku Filsafat", "Buku Hukum"],
    ["Buku Math", "Buku Ngoding"],
    ["Buku English", "Buku Mandarin"]
]
#Buku yang pengen gw cari
buku_dicari = ["Buku Math", "Buku Ngoding"]
#nomor urut
nomor_urutan_buku = 1
#Buku yang sering di baca
buku_sering_dibaca = 0
buku_jarang_dibaca = 0
#mencari di rak luar dulu
for rak in rak_buku:
    print()
    print(f"=== Buku Perpus area {nomor_urutan_buku} ===")
    nomor_urutan_buku += 1
    for bk in rak:
        if bk in buku_dicari:
            print(f"Buku yang mau di baca sekarang: {bk}")
            buku_sering_dibaca += 1
        else:
            print(f"Buku buat di baca nanti: {bk}")
            buku_jarang_dibaca += 1
print()
#buku yang sering di baca:
print("===== Rata-Rata buku yang ku baca di perpus hari ini =====")
print(f"Buku sering di baca: {buku_sering_dibaca}")
print(f"Buku jarang di baca: {buku_jarang_dibaca}")


