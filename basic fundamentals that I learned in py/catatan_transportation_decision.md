# Catatan Project: Transportation Decision System (freeCodeCamp Python)

**Tanggal:** 16 Agustus 2026  
**Platform:** freeCodeCamp Python Certification  
**Topik Utama:** Percabangan `if-elif-else`, Operator Logika (`and`, `not`), Nilai *Falsy*, & Alur Evaluasi Kondisi

---

## 📌 Ringkasan Project
Project ini mensimulasikan sistem pengambilan keputusan moda transportasi berdasarkan beberapa faktor:
1. Jarak tempuh (`distance_mi`).
2. Kondisi cuaca (`is_raining`).
3. Ketersediaan kendaraan/aplikasi (`has_bike`, `has_car`, `has_ride_share_app`).

Sistem akan mengevaluasi kondisi secara berurutan (*top-to-bottom*) dan hanya mengeksekusi **blok pertama** yang bernilai `True`.

---

## 📖 Penjelasan Kode Per Baris (Line-by-Line Review)

### 1. Inisialisasi Variabel Utama
```python
distance_mi = 5             # Jarak tempuh (5 mil)
is_raining = False          # Status hujan (False = tidak hujan)
has_bike = True             # Memiliki sepeda (True)
has_car = True              # Memiliki mobil (True)
has_ride_share_app = True   # Memiliki aplikasi ride share (True)
```
* **Penjelasan:** Menyiapkan parameter kondisi awal perjalanan.

---

### 2. Alur Evaluasi Percabangan (`if-elif`)

```python
# 15. Pengecekan nilai Falsy
if not distance_mi:
    print(False)
```
* **Review:** `distance_mi = 5`. Nilai `5` bersifat *truthy*, sehingga `not 5` bernilai `False`. Lanjut ke `elif` berikutnya.

```python
# 16. Jarak <= 1 DAN tidak hujan
elif distance_mi <= 1 and not is_raining:
    print(True)
```
* **Review:** `5 <= 1` bernilai `False`. Karena operator `and` membutuhkan kedua kondisi `True`, blok ini dilewati.

```python
# 17. Jarak <= 1 DAN hujan
elif distance_mi <= 1 and is_raining:
    print(False)
```
* **Review:** `5 <= 1` bernilai `False`. Blok ini dilewati.

```python
# 18. Jarak <= 6, hujan, DAN tidak ada sepeda
elif distance_mi <= 6 and is_raining and not has_bike:
    print(False)
```
* **Review:** `is_raining` bernilai `False`. Karena ada `is_raining` pada operator `and`, blok ini bernilai `False` dan dilewati.

```python
# 19. Jarak <= 6, tidak hujan, DAN tidak ada sepeda
elif distance_mi <= 6 and not is_raining and not has_bike:
    print(False)
```
* **Review:** `not has_bike` bernilai `False` (karena `has_bike = True`). Blok ini bernilai `False` dan dilewati.

```python
# 20. Jarak <= 6, ada sepeda, DAN tidak hujan
elif distance_mi <= 6 and has_bike and not is_raining:
    print(True)
```
* **Review (KONDISI TERPENUHI!):**
  * `distance_mi <= 6` $ightarrow$ `5 <= 6` (`True`)
  * `has_bike` $ightarrow$ `True`
  * `not is_raining` $ightarrow$ `not False` (`True`)
  * **Hasil:** `True and True and True` $ightarrow$ **`True`**.
  * **Output:** Mencetak `True`. Karena sudah menemukan kondisi yang `True`, Python **menghentikan** pengecekan `elif` selanjutnya.

```python
# 21-23. Kondisi Jarak > 6 (Dilewati/Terkunci)
elif distance_mi > 6 and has_ride_share_app:
    print(True)

elif distance_mi > 6 and has_car:
    print(True)

elif distance_mi > 6 and not has_car and not has_ride_share_app:
    print(False)
```
* **Review:** Kondisi 21, 22, dan 23 tidak pernah dievaluasi karena kondisi nomor 20 sudah terpenuhi terlebih dahulu.

---

## 🛠️ Konsep Penting yang Dipelajari

1. **Short-Circuit & Exclusive Execution (`if-elif`):**
   Pada rantai `if-elif-else`, begitu **satu** kondisi bernilai `True`, blok tersebut akan dieksekusi dan seluruh `elif` di bawahnya **diabaikan/dilewati**.
2. **Evaluasi Nilai Falsy/Truthy:**
   Dalam Python, angka `0`, `None`, `""` (string kosong), `[]` (list kosong) dianggap *falsy* (`False`). Angka selain `0` (seperti `5`) dianggap *truthy* (`True`).
3. **Operator `not`:**
   Membalikkan nilai boolean (`not False` menjadi `True`, `not True` menjadi `False`).

---

## 🚀 Kode Lengkap Terstruktur (`Transportation_Decision.py`)
```python
distance_mi = 5
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

# 15. distance_mi nilainya falsy (0 / None)
if not distance_mi:
    print(False)

# 16. Jarak <= 1 DAN tidak hujan
elif distance_mi <= 1 and not is_raining:
    print(True)

# 17. Jarak <= 1 DAN hujan
elif distance_mi <= 1 and is_raining:
    print(False)

# 18. Jarak antara 1 dan 6, DAN hujan tanpa sepeda
elif distance_mi <= 6 and is_raining and not has_bike:
    print(False)

# 19. Jarak antara 1 dan 6, DAN tidak hujan tanpa sepeda
elif distance_mi <= 6 and not is_raining and not has_bike:
    print(False)

# 20. Jarak antara 1 dan 6, ada sepeda DAN tidak hujan
elif distance_mi <= 6 and has_bike and not is_raining:
    print(True)

# 21. Jarak > 6 DAN ada aplikasi ride share
elif distance_mi > 6 and has_ride_share_app:
    print(True)

# 22. Jarak > 6 DAN ada mobil
elif distance_mi > 6 and has_car:
    print(True)

# 23. Jarak > 6 tapi TIDAK ada mobil DAN TIDAK ada aplikasi ride share
elif distance_mi > 6 and not has_car and not has_ride_share_app:
    print(False)
```
