import mod

# modüller var sayılan olarak python klasörünün içerisinde bulunur.
# aynı şekilde kendi yazdığımız modülü onların arasına koysak da
# sonradan kolayca içe aktarabiliriz.

# mod.py dosyası mod-test.py dosyasıyla aynı klasörde
# bulunsa da /usr/lib/python3.10 dizininde bulunsa da kodumuz çalışıyor.

# help(mod)
# help(mod.func)

number = mod.number
numbers = mod.numbers
person = mod.person
age = mod.person["age"]
func = mod.func("veli")

p0 = mod.Person()
p0.speak()

print(number, numbers, person, age)
