# __main__ adalah top level code environment

# __name__ == "__main__"  # ini akan terjadi ketika, program file utama 

# __name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

# __name__ pada program file eksternal 
import function

# Contoh penggunaan __main__

# Deklarasi 
def function_kali(a: int, b: int)-> int:
    return a * b

# Fungsi  utama
if __name__ == "__main__":
    angka1 = 10
    angka2 = 2
    hasil = function_kali(angka1, angka2)
    print(f"ini hasil dari perkalianya: {hasil}")

# Import Package
import package_add