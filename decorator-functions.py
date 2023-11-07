# ---------- ÖRNEK 1 ----------

# Decorator fonksiyonlar, işlemleri tek çatı altında birleştirerek
# işi kolaylaştıran fonksiyonlardır. Fonksiyonun üst satırına
# @decorator_ismi yazarak onun referansını decorator'a atarız
# ve işlem orada devam eder. Örn.: flag 1

"""def my_decorator(func):
	def wrapper(name):
		print("fonksiyondan önce olan işlemler")
		func(name)
		print("fonksiyondan sonra olan işlemler")
	return wrapper

@my_decorator                   # flag 1
def sayHello(name):
	print("hello " + name)

sayHello("ali")"""

# ---------- ÖRNEK 2 ----------

# Şimdi daha gerçekçi bir işlem yapalım. math modülünü içe
# aktardık ve usalma, faktoriyel, toplama adlarında 3 işlem
# fonksiyonu tanımladık. decorator fonksiyonumuzsa
# calculate_time, işlemin ne kadar sürede yapıldığını gösteren
# bir fonksiyon. içerisindeki kodları tek tek her fonksiyona
# ekleyip kodları karıştırmaktansa tüm fonksiyonların referansını
# calculate_time'a verdik ve bunun sonucunda hepsi tek çatı
# altında yapılıyor.

"""import math
import time

def calculate_time(func):
	def inner(*args,**kwargs):
		start = time.time()
		time.sleep(1)
		func(*args,**kwargs)
		finish = time.time()
		print("fonksiyon " + func.__name__ + " " + str(finish-start) + " saniye sürdü.")
	return inner

@calculate_time
def usalma(a,b):
	print(math.pow(a,b))

@calculate_time
def faktoriyel(a):
	print(math.factorial(a))

@calculate_time
def toplama(a,b):
	print(a + b)

usalma(2,3)
faktoriyel(5)
toplama(3,7)"""
