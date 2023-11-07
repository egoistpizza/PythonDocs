### Functions-Parameters ###


'''def changeValue(x):                       # String, value type olduğu için changeString fonksiyonu
    x = 'This string was changed.'           # tarafından değiştirilemedi.

string = 'This string was not changed.'
changeValue(string)
print(string)'''



'''def changeReferance(x):                   # List, referance type olduğu için changeReferance fonksiyonu
    x.remove('not')                          # tarafından değiştirildi.

list = ['This','list','was','not','changed']
changeReferance(list)
print(list)'''

# Not : Eğer referance type bir veriyi başka bir değişkenle senkronize etmeden, sadece içeriğini
# kopyalamak istersek değişken1 = değişken2 değil, değişken1 = değişken2[:] yazarak içeriği kopyalarız.
# Buna 'slicing' adı verilir.

'''def add(*numbers):                        # Python ile birlikte built-in gelen sum fonksiyonu liste
    return sum(numbers)                      # halinde verilen integer/float verileri toplar.
#                                            # Örnekteki kullanım istenen sayıda verinin toplanmasını 
print(add(67,21,53))'''                      # sağlar.

'''def creatDict(**dict):                    # Oluşturulan fonksiyona ait parametre * ile başlarsa tuple,
    for key, value in dict.items():          # ** ile başlarsa dict veri tipi belirtilmiş olur.
        print(f'{key} is {value}')           # Örnekte ** ile başlayan parametre dict veri belirtmiş,
#                                            # Sonrasında da .items metoduyla dict veri tipi ikili
creatDict(Name = 'Ali', Age = '49')          # gruplar halinde ayrılmış. Ve son olarak bu ikili veriler
creatDict(Name = 'Veli', Age = '36')'''      # key ve value olarak atanmıştır.