# ini contoh 2 latihan import package

# Fungsi menentukan antara genap dan ganjil (is_even)
def cek_angka(angka: int):
    if angka % 2 == 0:
        return f"{angka} adalah Genap!"
    else:
        return f"{angka} adalah Ganjil!"

# Konversi suhu (Celcius ke Fahrenheit)
def konversi_suhu(celcius):
    return (celcius * 9 / 5) + 32

# Kalkulator sederhana 
def count(number1: int , number2: int , operator):
    if operator == "+":
        return number1 + number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    elif operator == "//":
        return number1 // number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "INVALID!"
