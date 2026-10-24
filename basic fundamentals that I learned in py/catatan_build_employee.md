# Catatan Project: Build Employee (freeCodeCamp Python)

**Nama File:** `BuildEmployee.py`  
**Tanggal:** 12 Agustus 2026  
**Platform:** freeCodeCamp Python Certification  

---

## 📌 Ringkasan Project
Project ini berfokus pada manipulasi data teks (String) dan angka di Python, meliputi penggabungan string, konversi tipe data, f-string formatting, serta teknik *slicing* & *indexing* string.

---

## 🛠️ Konsep Python yang Dipelajari & Digunakan

### 1. Penggabungan String (String Concatenation)
Menggabungkan dua atau lebih variabel string menggunakan operator `+` atau `+=`.
```python
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name  # Result: 'John Doe'

address = '123 Main Street'
address += ', Apartment 4B'               # Result: '123 Main Street, Apartment 4B'
```

---

### 2. Konversi Tipe Data (Type Casting)
Mengubah tipe data angka (`int`) menjadi string (`str`) menggunakan fungsi `str()` agar dapat digabungkan dengan string lain tanpa menghasilkan error `TypeError`.
```python
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
```

---

### 3. Formatted String (f-String)
Cara modern, rapi, dan efisien untuk memformat string tanpa perlu konversi manual dengan `str()`.
```python
position = 'Data Analyst'
salary = 75000

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
# Output: Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
```

---

### 4. Pemotongan & Indeks String (String Slicing & Indexing)
Mengambil bagian/karakter spesifik dari string menggunakan indeks `[start:end]` atau indeks negatif `[-n:]`.

Contoh kode identitas karyawan: `employee_code = 'DEV-2026-JD-001'`

* **Mengambil Departemen:**
  ```python
  department = employee_code[0:3]  # Output: 'DEV'
  ```
* **Mengambil Tahun:**
  ```python
  year_code = employee_code[4:8]   # Output: '2026'
  ```
* **Mengambil Inisial Nama:**
  ```python
  initials = employee_code[9:11]   # Output: 'JD'
  ```
* **Mengambil 3 Karakter Terakhir (Indeks Negatif):**
  ```python
  last_three = employee_code[-3:]  # Output: '001'
  ```

---

## 🚀 Kode Lengkap (`BuildEmployee.py`)
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three = employee_code[-3:]
print(last_three)