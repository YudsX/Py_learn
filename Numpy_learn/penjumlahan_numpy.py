import numpy as np

vector_one = np.array ([1,2,3]) 
print(vector_one)
vector_two = np.ones (2)
print(vector_two)

# Setiap membuat array biasakan untuk mengecek 3 ini: shape, ndim, size
print(f" ini shape vector one: {vector_one.shape}") 
print(f" ini shape vector two: {vector_two.shape}")
print(f" ini ndim vector one: {vector_one.ndim}")
print(f" ini ndim vector two: {vector_two.ndim}")
print(f" ini size vector one: {vector_one.size}")
print(f" ini size vector two: {vector_two.size}")

# penjumlahan dalam Numpy (+)
total = vector_one + vector_one ** 2
print(f" ini vector hasil penjumlahan: {total}")