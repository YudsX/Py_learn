# Latihan ini dict + def + if + loops
import datetime
import os
import string
import random 

# Template Pengeluaran
Pengeluaran_Template = {
    'Bulan':'Gaji Sebulan 5jt',
    'Primer':3000000,
    'Sekunder':False,
    'Upgrade Skill': False,
    'Dana Darurat': 1000000,
    'Investment':1000000,
    'For Holiday/Hoby':False,
    'Catatan Tanggal':datetime.datetime(2027,1,2)
}

# Header
def header():
    os.system('cls') # -> supaya tidak perlu lagi clear di run
    print(f"{'INFO REKAP PENGELUARAN':^20}")
    print(f"{'SELAMA SEBULAN!!':^20}")
    print("-"*20)

def random_key():
    return ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
        
# input masukan
def input_data():
    input_pengeluaran = dict.fromkeys(Pengeluaran_Template.keys())

# Ambil input pengeluaran 
    input_pengeluaran['Bulan'] = input(f"Bulan ke berapa? : ")
    input_pengeluaran['Primer'] = int(input(f"Masukan Nominal spend Primer selama sebulan: "))
    input_pengeluaran['Sekunder'] = int(input(f"Masukan Nominal spend sekunder selama sebulan: "))   
    input_pengeluaran['Upgrade Skill'] = int(input(f"Masukan Nominal spend untuk UpSkill selama sebulan: "))
    input_pengeluaran['Dana Darurat'] = int(input(f"Masukan Nominal spend Dana Darurat selama sebulan: "))
    input_pengeluaran['Investment'] = int(input(f"Masukan Nominal spend Investment selama sebulan: "))
    input_pengeluaran['For Holiday/Hoby'] = int(input(f"Masukan Nominal spend healing selama sebulan: "))

# Ambil input tanggal 
    CATATAN_TAHUN = int(input(f"Masukan Tahun / YYYY: "))
    CATATAN_BULAN = int(input(f"Masukan Bulan (1-12): "))
    CATATAN_TANGGAL = int(input(f"Masukan Tanggal (1-31): "))

# Simpan ke datetime
    input_pengeluaran['Catatan Tanggal'] = datetime.datetime(CATATAN_TAHUN, CATATAN_BULAN, CATATAN_TANGGAL)

# KEMBALIKAN HASIL NYA
    return input_pengeluaran 

# Total Pengeluaran 
def hitung_total(primer, sekunder, upgrade, danadar, investm, holiday):
    return primer + sekunder + upgrade + danadar + investm + holiday 
                     
# Rekap tabel
def tampilkan_rekap(rekap_dict):
# Header Tabel Judul
    print()
    print()
    print(f"\n{'KEY':<8} {'Bulan?':^20} {'Primer':<8} {'Sekunder':^13} {'Upgrade Skill':^15}  {'Dana Darurat':^13} {'Invesment':^13} {'For Holiday/Hoby':^22} {'Catatan Tanggal':^15} {'Total':^15}")
    print("-"*150)

    for KEY, val in rekap_dict.items():
        BULAN = val['Bulan']
        PRIMER  =  val['Primer']
        SEKUNDER = val['Sekunder']
        UPGRADE =  val['Upgrade Skill']
        DANADAR =  val['Dana Darurat']
        INVESTM =  val['Investment']
        HOLIDAY =  val['For Holiday/Hoby']
        CATATAN =  val['Catatan Tanggal'].strftime("%x")
        TOTAL = hitung_total(PRIMER, SEKUNDER, UPGRADE, DANADAR, INVESTM, HOLIDAY)
# Header Tabel isi 
        print(f"{KEY:<8} {BULAN:^20} {PRIMER:<8} {SEKUNDER:^13} {UPGRADE:^15} {DANADAR:^13} {INVESTM:^13} {HOLIDAY:^22} {CATATAN:^15} {TOTAL:^15}")

# --- PROGRAM UTAMA ---
rekap_bulan1_sampai_bulan3 = {}

while True:
    header()
    input_pengeluaran = input_data()
    KEY = random_key()
    rekap_bulan1_sampai_bulan3.update({KEY:input_pengeluaran})
    tampilkan_rekap(rekap_bulan1_sampai_bulan3)
    print("\n")
    is_done = input("Sudah Kah? pilih >>> (y/n): ")
    if is_done == "y":
        break

print()
print("\n Arigatou Udah ngisi ^_^")