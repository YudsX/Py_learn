# Import module

import ngitung_ngitung as math # <- gini juga bisa jadi mengubah nama module\
from ngitung_ngitung import plus, kali, kuadrat # <- mengambil module ngitung_ngitung dan fungsi yang di dalam module nya

plus_result = math.plus(1,2,3,4,5)
print(f"Hasil Plus jadinya adalah: {plus_result}")

kali_result = math.kali(1,2,3,4,5)
print(f"Hasil Kali nya adalah: {kali_result}")

kuadrat_result = math.kuadrat(3)
print(f"Hasil Kuadrat adalah: {kuadrat_result(3)}")