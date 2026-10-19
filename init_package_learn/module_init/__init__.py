# Cara tanpa import all 
# cara 1
from . import matem     # <- titik disini mengartikan sebagai folder module init, jadi "from module_init import matem"
# Cara 2
from .matem import tambah   # <- tanpa harus memanggil module

# cara dengan import all 
__all__ = [
    "matem",
    "physic"
]

# cara chaining
from .matem import tambah, kali
from .physic import gaya

# ini cara kalau mau lebih dalam atau jelas
from . import physic