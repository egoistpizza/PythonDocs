### Global ve Local Değişkenler ###

'''x = 'GlobalVariable' # global scope
def function():
    x = 'LocalVariable' # local scope
function()
print(x)'''

########################### (value/referance types benzeri)

'''var = 'Jack' # global
def function(new_var):
   var = new_var # local
function('Jackob')
print(var)'''

########################### (iç içe fonksiyon kullanımı)

'''name = 'Jack' # global
def greeting():
    name = 'Jackob' # local
    def hi():
        print(f'Hi {name} !')
    hi()
greeting()'''

###########################

'''var = 10 # global
def change(var):
    print(f'Var = {var}')
    var = 20 # local
    print(f'Var is changed to {var}')
change(var)'''

########################### global keyword kullanımı !!!

'''var = 'GlobalVariable'
def change():
    global var # Fonksiyon içerisinde var değişkeni üzerinde yapılan değişimler global olacak.
    var = 'ChangedVariable'
change()
print(var)'''