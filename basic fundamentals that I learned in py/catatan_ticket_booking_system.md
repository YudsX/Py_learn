# Catatan Project: Ticket Pricing & Eligibility System (freeCodeCamp Python)

**Tanggal:** 15 Agustus 2026  
**Platform:** freeCodeCamp Python Certification  
**Topik Utama:** Pengondisian Majemuk (*Conditional Logic* `if-elif-else`), Operator Logika (`and`, `or`, `not`), & Hirarki Evaluasi

---

## 📌 Ringkasan Project
Project ini mensimulasikan logika sistem pemesanan tiket bioskop/acara. Sistem akan mengevaluasi:
1. Kelayakan usia pembeli (*eligibility*).
2. Perhitungan diskon berdasarkan status keanggotaan dan hari (*membership & weekend discount*).
3. Penambahan biaya (*extra charges*) berdasarkan waktu tayang atau hari.
4. Penentuan biaya layanan (*service charges*) berdasarkan tipe tempat duduk (`Gold`, `Premium`, dll).
5. Kalkulasi total harga akhir (`final_price`).

---

## 📖 Penjelasan Kode Per Baris (Line-by-Line Review)

### 1. Inisialisasi Variabel Utama
```python
# Data harga dasar, umur, waktu tayang, dan tipe tempat duduk
base_price = 15       # Harga dasar tiket sebesar $15
age = 21              # Umur pengguna (21 tahun)
seat_type = 'Gold'    # Tipe tempat duduk yang dipilih ('Gold')
show_time = 'Evening' # Waktu penayangan ('Evening')
```
* **Penjelasan:** Menyiapkan data awal yang akan diperiksa oleh kondisi-kondisi di bawahnya.

---

### 2. Pemeriksaan Kategori Usia
```python
# Memutuskan kategori umur yang bisa memesan tiket
if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')
```
* **Baris `if age > 17:`** Mengecek apakah umur di atas 17 tahun. Karena `age = 21`, hasilnya `True`, maka mencetak *'User is eligible to book a ticket'*.
* **Baris `if age >= 21:`** Mengecek apakah umur 21 tahun atau lebih untuk pertunjukan malam. Karena `21 >= 21` adalah `True`, maka mencetak *'User is eligible for Evening shows'*.

---

### 3. Logika Perhitungan Diskon & Presedensi Operator Logika
```python
# Syarat kondisi
is_member = True
is_weekend = False

# Inisialisasi diskon awal
discount = 0

# Memutuskan diskon pada pembeli berdasarkan syarat
if is_member and age >= 21 or is_weekend:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)
```
* **⚠️ Evaluasi Penting (`and` vs `or`):**
  Dalam Python, operator `and` dievaluasi **sebelum** `or` (*operator precedence*).
  * Ekspresi `is_member and age >= 21 or is_weekend` dibaca sebagai:  
    `(is_member and age >= 21) or is_weekend`
  * Sub-kondisi `(True and True)` bernilai `True`.
  * Karena `True or False` bernilai `True`, blok `if` dieksekusi. Diskon diatur menjadi `3`.

---

### 4. Perhitungan Biaya Tambahan (Extra Charges)
```python
# Inisialisasi biaya tambahan awal
extra_charges = 0

# Memutuskan apakah dikenakan biaya tambahan
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)
```
* **Penjelasan:** Operator `or` hanya memerlukan **satu** syarat bernilai `True`.
* Karena `show_time == 'Evening'` bernilai `True` (meskipun `is_weekend` bernilai `False`), kondisi bernilai `True`. `extra_charges` menjadi `2`.

---

### 5. Logika Pemesanan Tiket Kompleks & Biaya Layanan
```python
# Menhitung total akhir harga yang harus dibayar
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
```

* **Evaluasi Kondisi Utama:**
  `age >= 21` bernilai `True`. Karena ada operator `or` di awal (`age >= 21 or ...`), seluruh ekspresi utama langsung bernilai `True` (teknik *Short-circuit Evaluation*). Maka pemesanan tiket berhasil (*satisfied*).
* **Pengondisian Bertingkat (`if-elif-else`):**
  Sistem mengecek `seat_type`. Karena `seat_type == 'Gold'`, blok `elif` terpilih sehingga `service_charges = 3`.
* **Kalkulasi Harga Akhir:**  
  `final_price = 15 (base) + 2 (extra) + 3 (service) - 3 (discount) = 17`.

---

## 🛠️ Konsep Penting yang Dipelajari

1. **Short-circuit Evaluation:**
   Pada operator `or`, jika kondisi pertama sudah `True`, Python tidak akan mengecek kondisi setelahnya karena hasilnya sudah pasti `True`.
2. **Operator Precedence (Urutan Eksekusi):**
   Urutan prioritas operator logika dari tertinggi ke terendah adalah: `not` $ightarrow$ `and` $ightarrow$ `or`. Gunakan tanda kurung `()` jika ingin mengubah urutan evaluasi.
3. **Pengondisian Bersarang (*Nested Conditions*):**
   Memasukkan struktur `if-elif-else` di dalam blok `if` lain untuk perhitungan khusus seperti `service_charges`.

---

## 🚀 Kode Lengkap Terstruktur
```python
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = True
is_weekend = False
discount = 0

if (is_member and age >= 21) or is_weekend:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or (age >= 18 and (show_time != 'Evening' or is_member)):
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
```
