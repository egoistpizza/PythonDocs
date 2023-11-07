# 1- BMW, Mercedes, Opel, Mazda elemanlarına sahip bir liste oluşturun.
list1 = ['BMW','Mercedes','Opel','Mazda']
# 2- Liste kaç elemanlıdır?
'''print(len(list1))'''
# 3- Listenin ilk ve son elemanı nedir?
'''print(list1[0],list1[-1])'''
# 4- Mazda değerini Toyota ile değiştirin.
'''list1[-1] = 'Toyota'
print(list1)'''
# 5- Mercedes listenin bir elemanı mıdır?
'''print('Mercedes' in list1)'''
# 6- Listenin -2 index'indeki değer nedir?
'''print(list1[-2])'''
# 7- Listenin ilk 3 elemanını alın.
'''print(list1[:3])'''
# 8- Listenin son 2 elemanı yerine Toyota ve Renault değerlerini ekleyin.
'''list1[2:] = ['Toyota','Renault']
print(list1)'''
# 9- Listenin üzerine Audi ve Nissan değerlerini ekleyin.
'''list1 = list1 + ['Audi','Nissan']
print(list1)'''
# 10- Listenin son elemanını silin.
'''del list1[-1]
print(list1)'''
# 11- Liste elemanlarını tersten yazdırın.
'''print(list1[::-1])'''
# 12- Aşağıdaki verileri bir liste içinde saklayınız.
    # student0 = Yiğit Bilgi 2010, (70,60,70)
    # student1 = Sena Turan 1999, (80,80,70)
    # student2 = Ahmet Turan 1998, (80,70,90)
student0 = ['Yiğit','Bilgi',2010,[70,60,70]]
student1 = ['Sena','Turan',1999,[80,80,70]]
student2 = ['Ahmet','Turan',1998,[80,70,90]]
students = student0 + student1 + student2
# 13- Liste elemanlarını ekrana yazdırınız.
'''print(f'{student2[0]} {student2[1]} {2021-student2[2]} yaşında ve not ortalaması {(student2[3][0] + student2[3][1] + student2[3][2]) / 3} .')'''