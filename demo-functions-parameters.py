# 1- Gönderilen bir kelimeyi belirtilen sayıda ekrana yazdıracak bir fonksiyon yazınız.

'''def function(string,value = 1):
    print(string * value)
input1 = str(input('Please give me a text: '))
input2 = int(input('Please give me a integer: '))
function(input1,input2)'''

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

'''def function(*args):
    list = []
    list.append(args)
    print(list)
function(1,6,5,7,34,95.3,24,9,21,75,19,63,'hi!',67,'end')'''

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

'''def asalBul(value1,value2):
    for value in range (value1,value2):
        if value > 1:
            for i in range(2,value):
                if value % i == 0:
                    break
            else:
                print(value)
input1 = int(input('İlk sayıyı giriniz: '))
input2 = int(input('İkinci sayıyı giriniz: '))
asalBul(input1,input2)'''

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.

'''def bolenBul(value1):
    bolenler = []
    for value in range (1,value1+1):
        if value1 % value == 0:
            bolenler.append(value)
        else:
            pass
    return bolenler
input1 = int(input('Sayı giriniz: '))
print(bolenBul(input1))'''