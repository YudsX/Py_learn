'''Modul matematika'''

def tambah(*args):
    hasil = 0
    for data in args:
        hasil += data
    return hasil

def kali(*args):
    hasil = 1
    for data in args:
        hasil *= data
    return hasil

def pangkat(*args):
    hasil = 2
    for data in args:
        hasil **= data
    return hasil

# This Recursion faktorial !5
def factorial(numbers: int):
    # Base case (if condition) n is -1 or 0
    if numbers == 0 or numbers == 1:
        return 1
    # recursive: n multiplied by factorial of (n - 1)
    else:
        return numbers * factorial(numbers - 1)