# Data harga, umur, Waktu, tempat duduk type
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# Pemeriksaan Kategori Usia: 
# Memutuskan kategori umur yang bisa memesan ticket 
if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')


# Logika Perhitungan Diskon & Presedensi Operator Logika: 
# Syarat nya
is_member = True
is_weekend = False

# Perhitungan untuk discount
discount = 0

# Memutuskan discount pada pembeli berdasarkan syarat nya
if is_member and age >= 21 or is_weekend:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Perhitungan Biaya Tambahan (Extra Charges):
extra_charges = 0

# Memutuskan di kenakan biaya tambahan
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Logika Pemesanan Tiket Kompleks & Biaya Layanan:
# Menghitung total akhir harga yang harus di bayar semua nya  
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price = base_price + extra_charges + service_charges - discount
    print('Final price of ticket:', final_price)
else:
    print('Ticket booking failed due to restrictions')

