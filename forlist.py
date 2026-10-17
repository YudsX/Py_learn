#AI Confidence Checker 

#1. Inisialisasi variabel awal (Persiapan)
data = [45, 88, 76, 91, 59, 99, 65] #<----- data ai accuracynya
nomor_urut = 1 #<---- nomor urut setiap data
jumlah_Accep = 0  #<---- jumlah dari accept
jumlah_Reject = 0 #<---- jumlah dari reject
data_highest = 0 #<---- Menghitung data mana yang nilai nya paling besar
data_lowest = data[0]
data.append(20)

#2. Proses pengolahan data (Looping)
for hitung_jumlah in data: #<---- for akan membaca setiap data yang ada di list (data)

    # Cek kategori accepted / Rejected
    if hitung_jumlah >= 88: #<---- if akan mengecek apakah nilai data lebih besar sama dengan 88
        print(f"{nomor_urut}. Prediction accepted") #<---- Output
        jumlah_Accep += 1 # <----- jika data nya masuk accept, maka accept nambah 1
    else:
        print(f"{nomor_urut}. Prediction Rejected") #<---- Output
        jumlah_Reject += 1 # <----- jika data nya masuk reject, maka reject nambah 1

    # Cek nilai tertinggi dan terendah
    if hitung_jumlah > data_highest: # <---- untuk mengecek setiap data yang paling besar, itu yang mana
            data_highest = hitung_jumlah # <---- setelah di cek, data di masukan ke data_highest

    if hitung_jumlah < data_lowest:
         data_lowest = hitung_jumlah


    # Update nomor urut di bagian paling akhir loop
    nomor_urut += 1 # <---- mengurutkan nomor yang ada di dalam (dict if)

# 3. Laporan Hasil (Output)
total_Prediction = len(data) #menghitung total jumlah data ada berapa
print()
print("Jumlah data Total ada:")
print(total_Prediction)
print()

print("==== Jumlah Accepted and Rejected ==== ")
print(f"Total Accepted: {jumlah_Accep}") #menghitung total accept dan reject
print(f"Total Rejected: {jumlah_Reject}")
print()

print("=== Highest & Lowest ===")
print(f"Highest Confindence: {data_highest}") #menampikan data terbesar
print(f"Lowest Confindence: {data_lowest}")