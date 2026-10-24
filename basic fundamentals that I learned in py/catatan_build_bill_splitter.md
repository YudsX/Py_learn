# Catatan Project: Build Bill Splitter (freeCodeCamp Python)

**Nama File:** `Build_Bill_Splitter.py`  
**Tanggal:** 14 Agustus 2026  
**Platform:** freeCodeCamp Python Certification  

---

## 📌 Ringkasan Project
Project ini berfokus pada perhitungan matematika sederhana dalam program pembagi tagihan (Bill Splitter), meliputi akumulasi nilai (*augmented assignment*), perhitungan persentase tip, pembagian biaya per orang, serta pembulatan angka desimal.

---

## 🛠️ Konsep Python yang Dipelajari & Digunakan

### 1. Augmented Assignment Operator (`+=`)
Operator `+=` digunakan untuk menambahkan nilai ke dalam variabel yang sudah ada (*running total*) secara lebih efisien.
```python
running_total = 0
running_total += appetizers + main_courses + desserts + drinks
# Sama dengan: running_total = running_total + (appetizers + main_courses + desserts + drinks)
```

---

### 2. Aritmatika & Perhitungan Tip
* **Perhitungan Tip (25%):** Mengalikan total tagihan dengan desimal `0.25`.
  ```python
  tip = running_total * 0.25
  ```
* **Menambahkan Tip ke Total Tagihan:**
  ```python
  running_total += tip
  ```
* **Pembagian Tagihan:** Membagi total tagihan akhir dengan jumlah orang (`num_of_friends`).
  ```python
  final_bill = running_total / num_of_friends
  ```

---

### 3. Pembulatan Desimal (`round()`)
Fungsi `round(val, ndigits)` digunakan untuk membulatkan angka desimal ke jumlah digit tertentu di belakang koma (cocok untuk format mata uang).
```python
each_pays = round(final_bill, 2)  # Membulatkan hingga 2 digit di belakang koma
```

---

### 4. Formatted String (`f-string`)
Memformat teks hasil akhir agar siap ditampilkan ke pengguna secara rapi.
```python
print(f"Each person pays: {each_pays}")
```

---

## 🚀 Kode Lengkap (`Build_Bill_Splitter.py`)
```python
num_of_friends = 4  # Asumsi jumlah teman

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Hitung total awal
running_total = 0
running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Hitung tip (25%)
tip = running_total * 0.25
print('Tip amount:', tip)

# Tambahkan tip ke total tagihan
running_total += tip
print('Total with tip:', running_total)

# Bagi tagihan per orang
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Pembulatan 2 digit desimal
each_pays = round(final_bill, 2)
print(f"Each person pays: {each_pays}")
```
