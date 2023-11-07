### Functions ###

'''def sayHey(name = 'mate'):                    # Eğer oluşturduğumuz fonksiyona parametre verilmezse hata
    if name == '':                               # almamak için bir varsayılan oluştururuz.
        print('Please give us a name.')          # name = 'mate' yazarak yaptığımız da tam olarak bu!
    else:                                        # Eğer kullanım sırasında fonksiyona parametre vermezsek
        print(f'Hey {name} !')                   # varsayılan olarak 'mate' string'ini kullanacak.
#
while True:   
    name = input('Name: ')
    sayHey(name)'''



'''def sayHey(name = 'mate'):                    # return komutu, cevap döndürmemizi sağlar.
    return 'Hey ' + name + ' !'                  # Yani örnekte yaptığımız gibi, sayHello fonksiyonunu
#                                                # kullandığımızda çıkan cevap message değişkenine atandı.
name = input('Name: ')                           # Sonradan istersek bu değişkeni yazdırabilir veya
message = sayHey(name)                           # kullanabiliriz.
print(message)'''


'''try:                                          # Parametrenin yanlış verilmesi durumunda ValueError veya
    def total(num1,num2):                        # çeşitli hatalar alabiliriz.
        return num1 + num2                       # Buna karşın try-except bloklarını kullanarak
#                                                # hata ayıklamak faydalı bir çözüm yoludur.
    input1 = float(input('Sayı_1 : '))
    input2 = float(input('Sayı_2 : '))
    total = total(input1,input2)
    print(total)
except ValueError:
    print('Please give me a number.')'''


'''try:                                             
    def findAge(yearOfTheBirth):                 # DOCSTRING, INPUT ve OUTPUT yorumlarını belirtilen
        '''                                      # şekilde ekleyerek print(help(*fonksiyonAdı*))
        DOCSTRING: Calculating the age.          # komutuna açıklama oluşturabilirsiniz.     
        INPUT: Year of the birth.                # Aynı şekilde modüller içerisinde gelen fonksiyon
        OUTPUT: Age.                             # ve metotların açıklamalarını da bu komutla
        '''                                      # ekrana yazdırabilirsiniz.
        return 2021 - yearOfTheBirth

    def retirementCounter(age):
        '''
        DOCSTRING: Calculating the remaining time to the retirement.
        INPUT: Age.
        OUTPUT: Remaining time to the retirement.
        '''
        retirement = 65 - age
        if retirement < 0:
            return 0
        else:
            return retirement

    input1 = int(input('Born Date: '))
    age = findAge(input1)
    retirement = retirementCounter(age)
    print(age)
    if retirement == 0:
        print('Your age is compatible to retirement !')
        exit()
    else:
        pass
    print(f'{retirement} year(s) remaining to the your retirement !')
except ValueError:
    print('Please give me a year.')'''