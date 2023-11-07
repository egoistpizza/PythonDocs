### declaring a class
class User:
    pass
u1 = User()
u2 = User()

### constructor methods
# < __init__ yardımıyla tanımlanan constructor'lar, class'a ait bir object oluşturulmasıyla beraber
# otomatik olarak çalıştırılır >
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
p1 = Person('Eric Ericsson', 68432165491)
p2 = Person('Markus Markusson', 39451287624)

### class attributes
class Constructor:

    # class attributes
    address = 'none'
    birth = 'none'
    email = 'none'
    phone = 'none'

    # constructor
    def __init__(self, name, id):

        # object attributes
        self.name = name
        self.id = id

c1 = Constructor('Eric Ericsson', 68432165491)
c2 = Constructor('Markus Markusson', 39451287624)

# update attributes
c1.address = input('Adress: ')
c1.birth = input('Birth Year: ')
c1.email = input('E-mail: ')
c1.phone = input('Phone Number: ')

c2.address = input('Adress: ')
c2.birth = input('Birth Year: ')
c2.email = input('E-mail: ')
c2.phone = input('Phone Number: ')

print(f'Info c1 = Name: {c1.name} , ID: {c1.id} , Adress: {c1.address} , Birth Year: {c1.birth} , E-mail: {c1.email} , Phone Number: {c1.phone}')
print(f'Info c2 = Name: {c2.name} , ID: {c2.id} , Adress: {c2.address} , Birth Year: {c2.birth} , E-mail: {c2.email} , Phone Number: {c2.phone}')