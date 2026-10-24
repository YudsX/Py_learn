# dictionary (dict) -> associative array
# indentifier ->

#list menu warung
list_makanan = ['Kopi,', 'Nasgor', 'Gorengan', 'Mieayam', 'Cake']

# Example of dict
data_dict = {
    'key1':'value1',
    'menu_warkop': list_makanan,
    'makanan1':'Nasgor',
    'harga':'10000',
}

print(data_dict['menu_warkop'])
print(data_dict['makanan1'])
print(data_dict['harga'])

# Operator Dictionary
data_dict2 = {
    "Nasgor":"Nasi Goreng",
    "Mieayam":"MIEAYAMMM",
    "Lokasi":"Ngawi barat",
    "Harga":10000
}

LENDICT = len(data_dict2) 
print(f'Panjang Dictionary ini: {LENDICT}')

# Mengecek key Exist atau tidak
KEY = 'Nasgor'    # -> ini bisa di tentukan apakah ada engga nya dalam KEY
CHECKKEY = KEY in data_dict2
print(f'Apakah {KEY} ada?: {CHECKKEY}')

# Mengakses value (Read) dengan get
print(data_dict2['Nasgor'])
print(data_dict2.get('Mieayam'))
print(data_dict2.get('Naspad', 'Naspad gaada, cek aja warkop sebelah'))     #Cek key massage dengan KEY tidak ditemukan!

# Mengupdate KEY value
data_dict2['Lokasi'] = 'Ngawi timuer'
print(data_dict2)

# Menggunakan UPDATE
data_dict2.update({'Bakso':'Bakso Khas Ngawi loh yhhh'})
print(data_dict2)
data_dict2.update({'Mieayam':{'Mie pake ayamm ^_^'}})
print(data_dict2)

# Mendelete data pada dictionary
del data_dict2['Nasgor']
print(data_dict2)

# Looping pada dict
belanjaan_market = {
    'Buah':'Apel',
    'Snacks':'Potabee',
    'Minuman':'Teh sosro',
    'Frozen food':'Sosis, Tomyam, Kanzler',
    'Barang':'Kartu TCG Pokemon'
}

# Looping First Try, hasil nya berupa key nya:
for belanjaan in belanjaan_market:
    print(belanjaan)

# operator untuk mengambil item / iterables:
keys = belanjaan_market.keys()
print(keys)

for key in belanjaan_market.keys():
    print(key)

# ini dipakai ketika Jika butuh nama kunci dan nilainya sekaligus dalam loop.
for key in belanjaan_market.keys():     # -> Memutar kunci ->>  cari value satu per satu.
    print(belanjaan_market.get(key))

# Untuk mengambil Value nya:
values = belanjaan_market.values()
print(values)

for value in belanjaan_market.values():
    print(value)

# Untuk mengambil keys + values nya 
item = belanjaan_market.items()
print(item)

for keranjang_belanjaan in belanjaan_market.items():
    print(keranjang_belanjaan)

# Ini kalo mau ambil pisah key = key, value = value
for key, value in belanjaan_market.items():
    print(f'keys = {key}, value = {value}')

# Copy pada Dictionary 
film = {
    'film action':'Avengers DOOMSDAY',
    'film horor':'THe conjuring atau sinister',
    'film comedy':'500 days summer',
    'film romance and action':'Spiderman amazing part 1 and 2'
}

# Mengcopy film dan disimpan di film for night
film_in_night = film.copy()
print(film_in_night)

# test sebuah perbedaan 
print(f'film untuk di malam hari: {film_in_night} \n')
print(f'film untuk weekend: {film} \n')

# mengganti value dengan film copy an tadi
film['film comedy'] = 'Kungfu hustle'
print(f'film untuk di malam hari change in: {film_in_night} \n')
print(f'film untuk weekend change in: {film} \n')

# Pop pada dictionary (berdasarkan key)
kick_film = film.pop('film action')
print(f"kick film action = {kick_film} \n")
print(f"hasil film keseluruhan jadi = {film} \n")

# Popitem pada dictionary (berdasarkan terakhir nya)
kick_film_terakhir = film.popitem()
print(f"kick film action = {kick_film_terakhir} \n")
print(f"hasil film keseluruhan jadi = {film} \n")

# Nested Dictionary Multi keys:
import datetime 

pengeluaran_bulan1 = {
    'Dana':'Gaji Sebulan 5jt',
    'Primer':3000000,
    'Sekunder':False,
    'Upgrade Skill': False,
    'Dana Darurat': 1000000,
    'Investment':1000000,
    'For Holiday/Hoby':False,
    'Catatan Tanggal':datetime.datetime(2027,1,2)
}

pengeluaran_bulan2 = {
    'Dana':'Gaji Sebulan 5jt',
    'Primer':3000000,
    'Sekunder':False,
    'Upgrade Skill': 500000,
    'Dana Darurat': 500000,
    'Investment':1000000,
    'For Holiday/Hoby':False,
    'Catatan Tanggal':datetime.datetime(2027,1,3)
}

pengeluaran_bulan3 = {
    'Dana':'Gaji Sebulan 5jt',
    'Primer':3000000,
    'Sekunder':1000000,
    'Upgrade Skill': False,
    'Dana Darurat': 1000000,
    'Investment':500000,
    'For Holiday/Hoby':500000,
    'Catatan Tanggal':datetime.datetime(2027,1,30)
}

rekap_bulan1_sampai_bulan3 = {
    'REKAP001':pengeluaran_bulan1,
    'REKAP002':pengeluaran_bulan2,
    'REKAP003':pengeluaran_bulan3
}

print(f"{'KEY':<8} {'Dana':^20} {'Primer':<8} {'Sekunder':^15} {'Upgrade Skill':^17}  {'Dana Darurat':^17} {'Invesment':^15} {'For Holiday/Hoby':^25} {'Catatan Tanggal':^15}")
print("-"*150)

for Hasil in rekap_bulan1_sampai_bulan3:
    KEY = Hasil

    DANA = rekap_bulan1_sampai_bulan3[KEY]['Dana']
    PRIMER  = rekap_bulan1_sampai_bulan3[KEY]['Primer']
    SEKUNDER = rekap_bulan1_sampai_bulan3[KEY]['Sekunder']
    UPGRADE = rekap_bulan1_sampai_bulan3[KEY]['Upgrade Skill']
    DANADAR = rekap_bulan1_sampai_bulan3[KEY]['Dana Darurat']
    INVESTM = rekap_bulan1_sampai_bulan3[KEY]['Investment']
    HOLIDAY = rekap_bulan1_sampai_bulan3[KEY]['For Holiday/Hoby']
    CATATAN = rekap_bulan1_sampai_bulan3[KEY]['Catatan Tanggal'].strftime("%x")

    print(f"{KEY:<8} {DANA:^20} {PRIMER:<8} {SEKUNDER:^15} {UPGRADE:^15}  {DANADAR:^17} {INVESTM:^17} {HOLIDAY:^25} {CATATAN:^15}")

