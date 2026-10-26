import numpy as np

list_biasa1 = [1,2,3]
vector_1 = np.array([1,2,3])

print(f" ini list biasa: {list_biasa1}")     # <- list biasa
# print(f" ini list biasa dengan kuadrat: {list_biasa1 ** 2}")    # <- akan error

print(f" ini np : {vector_1}")      # <- jadi berupa matriks 
print(f" ini np dengan kuadrat : {vector_1 ** 2}")      # <- Jalan karena ini np

# Example for
ini_matriks2 = np.array([(1,2,3,4,5), (6,7,8,9,10)])
print(f"ini matriks 2 : \n{ini_matriks2}")

# Example for zeros (nol)
zeros_0 = np.zeros((50, 50))        # <- Membuat bilangan di dalam isi array jadi nol
print(f"ini Zeros : \n{zeros_0}")

# Example for ones (1)
ones_1 = np.ones((50))        # <- Membuat bilangan di dalam isi array jadi nol
print(f"ini ones : \n{ones_1}")