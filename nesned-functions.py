"""def greeting(name):
	print(f"hello {name}")"""

"""greeting("ali")
print(greeting)"""

"""sayHello = greeting"""

"""print(sayHello)
print(greeting)"""

# ----------------------------------

# ENCAPSULATION, İÇ İÇE FONKSİYONLAR:

"""def outer(num1):
	print("outer çalıştı")
	def inner_increment(num1):
		print("inner çalıştı")
		return num1 + 1
	num2 = inner_increment(num1)   # flag
	print(num1,num2)

outer(10)
inner_increment(10)
"""

"""def factorial(number):
	if not isinstance(number, int):
		raise TypeError("number must be an integer")

	if not number >= 0:
		raise ValueError("number must be zero or positive")

	def inner_factorial(number):
		if number <= 1:
			return 1

		return number * inner_factorial(number-1)
	return inner_factorial(number)

try:
	print(factorial(6))
except Exception as error:
	print(error)
	"""
	