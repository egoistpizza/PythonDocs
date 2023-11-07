# error handing => hata yönetimi

'''
x = int(input('x: '))
y = int(input('y: '))

print(x/y)
'''
# ondalıklı değer verince ValueError döndürüyor.
# y'ye 0 verince ZeroDivisionError döndürüyor.


### HATA YÖNETİMİ ###

# bu hatalara karşı error handling (hata yönetimi) yapmak için
# hata gelebilecek kodları TRY bloğuna alıyoruz.

# öngördüğümüz hataları ise EXCEPT'le belirtiyoruz.
'''
try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)

except ValueError:
    print('Lütfen sadece tam sayı giriniz.')

except ZeroDivisionError:
    # print('Lütfen y değişkenine 0 (sıfır) vermeyiniz.')
    # VEYA
    print('Tanımsız değer.')

# birden fazla hata türünü tek except bloğunda toplayabiliriz. parantezi unutma !

except (ValueError, ZeroDivisionError):
    print('Lütfen sadece tam sayı giriniz. y != 0')

# hatalara değişken atayabiliriz !

except (ValueError, ZeroDivisionError) as error:
    print('Lütfen sadece tam sayı giriniz. y != 0')
    print(error)

# eğer spesifik hatalar yerine tüm hataları yakalamak istiyorsak
# hata ismi belirtmiyoruz.

except:
    print('Lütfen sadece tam sayı giriniz. y != 0')
'''

# except blokları da if gibi çalışır, ELSE atayabiliriz !

'''
try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
except:
    print('Lütfen sadece tam sayı giriniz. y != 0')
else:
    print('Aferin lan sorun yok.')
'''

# tabi ki kodu while döngüsüne alıp else: break yapabiliriz.
# bu sayede hata alırsa tekrar çalıştırır, almazsa sonlanır.

'''
while True:
    try:
            x = int(input('x: '))
            y = int(input('y: '))
            print(x/y)
    except:
        print('Lütfen sadece tam sayı giriniz. y != 0')
    else:
        break
'''

# except'te spesifik bir hata belirtmediğimizde kafa rahat olur
# ama hata log'u tutuyorsak hatanın kaynağını bilemeyiz.
# bunun içinde except: Exception(üst hata class'ı) verebiliriz.
# sonrasında hataya da değişken atayarak log'u tutabiliriz.

'''
while True:
    try:
            x = int(input('x: '))
            y = int(input('y: '))
            print(x/y)
    except Exception as error:
        print('Lütfen sadece tam sayı giriniz. y != 0')
        print(error)
    else:
        break
'''

# FINALLY bloğu, try-except çalıştıktan sonra daima devreye girer.
# FINALLY bloğunu script çalıştıktan sonra işlemleri sonlandırmak için
# kullanabiliriz. örneğin bir dosyayı açmışsak finally ile kapatırız.

'''
while True:
    try:
            x = int(input('x: '))
            y = int(input('y: '))
            print(x/y)
    except:
        print('Lütfen sadece tam sayı giriniz. y != 0')
    else:
        break
    finally:
        print('Hata yakalama başarılı !')
'''
