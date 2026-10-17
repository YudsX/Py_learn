# # 1. Fungsi Pengecek
# def cek_tebakan(tebakan, rahasia):
#     if tebakan == rahasia:
#         return "Tepat sekali! 🎉"
#     elif tebakan > rahasia:
#         return "Terlalu tinggi! 📈"
#     else:
#         return "Terlalu rendah! 📉"

# # 2. Program Utama (TANPA random!)
# angka_rahasia = 15  # <--- Kita tentuin sendiri angkanya di sini
# sudah_benar = False

# print("=== GAME TEBAK ANGKA ===")

# # Loop akan terus jalan SELAMA 'sudah_benar' masih False
# while not sudah_benar:
#     input_pemain = int(input("Masukkan tebakanmu (1-20): "))
    
#     # Panggil fungsi pengecek
#     hasil = cek_tebakan(input_pemain, angka_rahasia)
#     print(hasil)
#     print("----------------------------")
    
#     # Kalau hasil fungsinya bilang tepat, berhentikan loop!
#     if hasil == "Tepat sekali! 🎉":
#         sudah_benar = True

# print("Selamat! Kamu berhasil menebaknya!")
