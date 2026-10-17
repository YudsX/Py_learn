# Lambda Function

#Contoh dari code biasa tanpa lambda
def division_floor(number):
    return number // 2

print(f"Hasil Pembagian adalah: {division_floor(10)}")

# With Lambda Function
# Output = lambda argument/parameter: Expression
division_floor = lambda number : number // 2
print(f"Hasil Pembagian With lambda: {division_floor(20)}")

# contoh dengan 2 atau lebih argument 
kuadrat = lambda number, kuadrat : number**kuadrat
print(f"Hasil kuadrat With Lambda dengan dua argument: {kuadrat(10, 2)}")

# Contoh dengan sort Lambda
# Sorting list  biasa
menu_warkop = ["Mieyam", "Sate", "Nasgor"]
menu_warkop.sort()
print(f"Sorted list = {menu_warkop}")

# Sorting kalo pakai panjang 
def panjang_menu_warkop(makanan):
    return len(makanan)

menu_warkop = ["Mieyam", "Sate", "Nasgor"]
menu_warkop.sort(key = panjang_menu_warkop)
print(f"Sorted list by kalo panjang: {menu_warkop}")

# sort pakai lambda
menu_warkop= ["Mieyam", "Sate", "Nasgor"]
menu_warkop.sort(key = lambda makanan : len(makanan))
print(f"Sorted list pake lambda: {menu_warkop}")

# Contoh filter tidak pakai lambda 
number_list = [1,2,3,4,5,6,7,8,9,14,1,31,46,5,46,42,3,41,3]
def less_five(number: list) -> int: 
    return number < 5

new_number = list(filter(less_five, number_list)) # -> menggunakan filter harus dua kondisi seperti (less_five, number_list)
print(new_number)

# memakai lambda filter
# Output = lambda argument/parameter: Expression
number_list = [1,2,3,4,5,6,7,8,9,14,1,31,46,5,46,42,3,41,3]
new_number = list(filter(lambda number : number < 5, number_list))
print(new_number)

# Kasus Genap
# Output = lambda argument/parameter: Expression
number_list = [1,2,3,4,5,6,7,8,9,14,1,31,46,5,46,42,3,41,3]
even_numbered_data = list(filter(lambda number  : (number % 2 == 0), number_list))
print(even_numbered_data) 

# Kasus Ganjil
# Output = lambda argument/parameter: Expression
number_list = [1,2,3,4,5,6,7,8,9,14,1,31,46,5,46,42,3,41,3]
odd_numbered_data = list(filter(lambda number  : (number % 2 != 0), number_list))
print(odd_numbered_data) 

# Kasus Kelipatan 3
# Output = lambda argument/parameter: Expression
number_list = [1,2,3,4,5,6,7,8,9,14,1,31,46,5,46,42,3,41,3]
data_multiples = list(filter(lambda number  : (number % 3 == 0), number_list))
print(data_multiples) 

# Anonymous Function 
# Currying  <- Haskell Curry

# Ini def biasa 
def kuad_angka(numbers, kuadrat):
    hasil = numbers**kuadrat
    return hasil

hasil_olah = kuad_angka(10, 2)
print(f"Ini hasil Function biasa: {hasil_olah}")

# Dengan Currying Teknik
def kuadrat(num):
    return lambda numbers : numbers**num

kuadrat3 = kuadrat(3)
print(f"Kuadrat 3 = {kuadrat3(4)}")

kuadrat2 = kuadrat(2)
print(f"Kuadrat 2 = {kuadrat2(2)}")
print(f"Kuadrat Bebas = {kuadrat(2)(5)}")