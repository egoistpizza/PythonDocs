# Inheritance (Kalıtım) => Miras Alma

# Person => name, lastname, id, age, eat(), run, drink()
# Student(Person), Teacher(Person)

# Şöyle örneklendirmek gerekirse:
# Animal => Dog(Animal), Cat(Animal)     bu durumda Animal class'ına ait özellikler
#                                        kalıtım yoluyla Dog ve Cat class'larına geçer.
#                                        Fakat bunun sonrasında bu class'lara eklenen
#                                        özelliklerin Animal class'ıyla senkronize
#                                        olması söz konusu değildir.

# ----------------------------------------------------
# Örnek 1.1:
'''
class Person:
    def __init__(self):
        print('Person Created.')
class Student(Person):
    pass

p1 = Person()
s2 = Student()
'''
# OUTPUT: 2 kez 'Person Created.' yazdırır.
# ----------------------------------------------------

# ----------------------------------------------------
# Örnek 1.2:
'''
class Person:
    def __init__(self):
        print('Person Created.')
class Student(Person):
    def __init__(self):
        print('Student Created.')

p1 = Person()
s2 = Student()
'''
# OUTPUT: 1 kez 'Person Created.', 1 kez 'Student Created.' yazdırır.
# ----------------------------------------------------

# Not: Örnek 1.2'de de görüldüğü üzere kalıtılan yeni class'a eklenen yeni __init__ bloğu temeldekini
# etkisiz hale getirir. Öncekini kullanmaya devam etmek, ayrı bir ekleme yapmak istiyorsak Örnek 1.3'deki
# (flag) yolu izlemeliyiz.

# ----------------------------------------------------
# Örnek 1.3:
'''
class Person:
    def __init__(self):
        print('Person Created.')
class Student(Person):
    def __init__(self):
        Person.__init__(self)                  # flag
        print('Student Created.')

p1 = Person()
s2 = Student()
'''
# OUTPUT: 2 kez 'Person Created.', 1 kez 'Student Created.' yazdırır. 
# ----------------------------------------------------

# Not 2: Temel class'ta ek parametreler oluşturulması durumunda kalıtılan class'tan parametreler temel 
# class'a gönderilerek işlem tamamlanır. Örnek 1.4, (flag 2).

# ----------------------------------------------------
# Örnek 1.4:
'''
class Person:
    def __init__(self,fname,lname):
        self.firstName = fname.title()
        self.lastName = lname.upper()
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)                  # flag 2: Görüldüğü üzere aynı (fname,lname)
#                                                          # parametreleri Student class'ına ekledik.

p1 = Person('Eric','Ericsson')
s1 = Student('Markus','Markusson')
print(f'''
'''p1 info = {p1.firstName} {p1.lastName}
s1 info = {s1.firstName} {s1.lastName}'''
''')
'''
# OUTPUT:
# p1 info = Eric ERICSSON   
# s1 info = Markus MARKUSSON
# ----------------------------------------------------

# Not 3: Oluşturulan metotlar kalıtılan tüm class'lar için de ulaşılabilirdir. Örnek 1.5.

# ----------------------------------------------------
# Örnek 1.5:
'''
class Person:
    def __init__(self,fname,lname):
        self.firstName = fname.title()
        self.lastName = lname.upper()
    def whoAmI(self):
        print(f'I am a {(str(type(self)))[17:-2]}.')     ### Bu satırı incele !!!
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

p1 = Person('Eric','Ericsson')
s1 = Student('Markus','Markusson')

p1.whoAmI()
s1.whoAmI() # Person için tanımlanan metoda Student da kalıtım yoluyla erişebiliyor.
'''
# OUTPUT:
# I am a Person.
# I am a Student.
# ----------------------------------------------------

# Not 4: Aynı konuda bir örnek daha (Örnek 1.6):

# ----------------------------------------------------
# Örnek 1.6:
'''
class Person:
    def __init__(self,fname,lname):
        self.firstName = fname.title()
        self.lastName = lname.upper()
    def whoAmI(self):                                   #
        print(f'I am a {(str(type(self)))[17:-2]}')     ### Bu satırı incele !!!
    def eat(self):                                      #
        print('Hart-Hurt !')                            #
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

p1 = Person('Eric','Ericsson')
s1 = Student('Markus','Markusson')

p1.whoAmI()
s1.whoAmI() # Person için tanımlanan metoda Student da kalıtım yoluyla erişebiliyor.
p1.eat()
s1.eat() # Person için tanımlanan metoda Student da kalıtım yoluyla erişebiliyor.
'''
# OUTPUT:
# I am a Person.
# I am a Student.
# Hart-Hurt !
# Hart-Hurt !
# ----------------------------------------------------

# Not 5: Kalıtım yoluyla aktarılan bir metodu yeni class'ta etkisiz hale getirmek için aynı
# isimde farklı bir metot tanımlar ve istediğimiz işlemi bloğa aktarırız.
### Buna overriding denir.

# Not 6: Yeni class'a __init__ eklemeleri yapmak için __init__ bloğuna doğrudan ekleme yaparız.
# (Örnek 1.6) (flag 3: Student class'ına number verisi ekledik.)

# ----------------------------------------------------
# Örnek 1.6:
'''
class Person:
    def __init__(self,fname,lname):
        self.firstName = fname.title()
        self.lastName = lname.upper()
class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.number = number                      # flag 3


p1 = Person('Eric','Ericsson')
s1 = Student('Markus','Markusson',9515564)
print(s1.number)
'''
# OUTPUT:
# 9515564
# ----------------------------------------------------

# Not 7: Kalıtım yoluyla aktarılan yeni class'a ait yeni metotlar local'dir.
# (Örnek 1.7) (flag 4)

# ----------------------------------------------------
# Örnek 1.7:
'''
class Person:
    def __init__(self,fname,lname):
        self.firstName = fname.title()
        self.lastName = lname.upper()
class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.number = number
    def greetings(self):                            # flag 4
        greeting = 'Hello, I am a Student !'        #
        return greeting                             #

p1 = Person('Eric','Ericsson')
s1 = Student('Markus','Markusson',9515564)
print(s1.greetings())
'''
# OUTPUT:
# Hello, I am a Student !
# ----------------------------------------------------

# Not 8: Kalıtılan fonksiyonun __init__ constructor'ını çağırmak için farklı bir yöntem olan
# super() metodunun kullanımı (Örnek 1.8) (flag 5):

# ----------------------------------------------------
# Örnek 1.8:
'''
class Person:
    def __init__(self,fname,lname):
        self.firstName = fname.title()
        self.lastName = lname.upper()
class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.number = number
    def greetings(self):
        greeting = 'Hello, I am a Student !'
        return greeting
class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)                  # flag 5: super() metodu kullanıldığında parametreler
        self.branch = branch                           # bölümüne 'self' eklememiz gerekmiyor.
    def greetings(self):
        greeting = f'Hello, I am a {self.branch} Teacher !'
        return greeting
p1 = Person('Eric','Ericsson')
s1 = Student('Markus','Markusson',9515564)
t1 = Teacher('Lilly','Lillysson','Chemistry')
print(t1.greetings())
'''
# OUTPUT:
# Hello, I am a Chemistry Teacher !
# ----------------------------------------------------