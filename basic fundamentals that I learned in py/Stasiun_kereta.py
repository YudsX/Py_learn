# # ---- Memesan ticket kereta ----
# # Tujuan saya ke stasiun ke sukabumi naik kereta dari bandung, (berangkat dari stasiun bandung)
# # ---------------------------------
# # STASIUN 
# stasiun_bandung = True

# # HARGA TICKET
# ticket_stasiun_bandung = 30000

# # JADWAL HARI KEBERANGKATAN 
# hari_senin = True
# hari_selasa = False
# hari_rabu = False
# hari_kamis = True
# hari_jumat = True

# # jika hari senin dan ticket >= 30000 dan stasiun bandung
# if hari_senin and ticket_stasiun_bandung >= 30000 and stasiun_bandung:
#     print("kereta Bandung hari ini siap berangkat!")
# else:
#     print("Tidak sesuai dengan jadwal keberangkatan, harga ticket dan stasiun... Silahkan untuk cek kembali!!")

# Soal 1: Cek ketersediaan hari keberangkatan, Rute dari Sukabumi-Bandung
hari = "Sabtu"

if hari == "Sabtu":
    print("Kereta Sukabumi-Bandung tersedia hari ini.")
else:
    print("Tidak ada kereta pada Jadwal hari ini")

# Soal 2: Cek Saldo E-Money untuk ticket
# Harga ticket kereta adalah 45.000
saldo = 50000
harga_ticket = 45000

if saldo >= harga_ticket:
    saldo -= harga_ticket
    sisa_saldo = saldo
    print(f'Pembelian Ticket kereta Sukabumi-Bandung berhasil! Sisa akhir dari saldo anda: {sisa_saldo}')
else:
    print('Pembelian gagal! Saldo anda tidak mencukupi!')

# Soal 3: Penentuan Jenis diskon ticket berdasarkan kategori pembeli
kategori1 = 'Pelajar'
kategori1_harga= (45000)

kategori2 = 'Umum'
kategori2_harga = 45000

# diskon untuk kategori pelajar 
diskon = 15000

if kategori1 and kategori1_harga:
    kategori1_harga -= diskon
    harga_akhir = kategori1_harga
    print(f'Kategori pelajar mendapatkan diskon sebesar 10.000, harga yang perlu di bayar: {harga_akhir}')
elif kategori2 and kategori2_harga:
    print(f"kategori umum harga yang perlu di bayar: {kategori2_harga}")
else:
    print('Pembelian Gagal! silahkan coba lagi!!')