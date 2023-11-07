# Math modülü hakkında dokümantasyon.

# Yöntem 1

'''
import math

commands = dir(math)
help = help(math)

kombinasyon = math.comb(5, 2)  # 10
karekok = math.sqrt(144)  # 12.0 (bu arkadas float sonuc donduruyor)
faktoriyel = math.factorial(5)  # 120
tabanaYuvarlama = math.floor(518.999999)  # 518
tavanaYuvarlama = math.ceil(35.0000001)  # 36

print(kombinasyon, karekok, faktoriyel, tabanaYuvarlama, tavanaYuvarlama)
'''

# kütüphaneleri içe aktarırken "import x as y" olarak aktarabiliriz.
# bu da kullanımda kolaylık sağlar, mesela "import math as islem" yazarsak
# kullanım esnasında fonksiyonları islem.comb , islem.sqrt , islem.factorial ,
# islem.floor , islem.ceil olarak aktarabiliriz.

# Yöntem 2

# kütüphaneleri içe aktarmak yerine içlerindeki fonksiyonları içe aktarabiliriz.
# bunun için de from ve * kullanırız. bu sayede math.factorial() kullanmak
# yerine direkt factorial() kullanabiliriz !

'''
from math import *

kombinasyon = comb(5, 2)  # 10
karekok = sqrt(144)  # 12.0 (bu arkadas float sonuc donduruyor)
faktoriyel = factorial(5)  # 120
tabanaYuvarlama = floor(518.999999)  # 518
tavanaYuvarlama = ceil(35.0000001)  # 36

print(kombinasyon, karekok, faktoriyel, tabanaYuvarlama, tavanaYuvarlama)
'''

# Yöntem 3

# e tabi istersek daha minimal de takılabiliriz. "from x import a,b,c" ile
# sadece kullanacağımız fonksiyonları içe aktarabiliriz.

'''
from math import comb, sqrt, factorial, floor, ceil
kombinasyon = comb(5, 2)  # 10
karekok = sqrt(144)  # 12.0 (bu arkadas float sonuc donduruyor)
faktoriyel = factorial(5)  # 120
tabanaYuvarlama = floor(518.999999)  # 518
tavanaYuvarlama = ceil(35.0000001)  # 36

print(kombinasyon, karekok, faktoriyel, tabanaYuvarlama, tavanaYuvarlama)
'''
