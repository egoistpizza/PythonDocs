list = [57,'XYZ',18.79]
tuple = (57,'XYZ',18.79)

'''List ve Tuple veri tiplerinin hemen hemen her özelliği aynıdır.'''
'''Aşağıdaki kodları denerseniz veri tipleri dışında her sonucu aynı alırsınız.'''

# print(type(list))
# print(type(tuple))

# print(list[1])
# print(tuple[1])

# print(len(list))
# print(len(tuple))

'''Peki ikisi de aynı sonuçları veriyorsa aradaki fark nedir ?'''
'''--- Tuple veri tipinde değiştirme yapamazsınız. Değişkeni tekrardan atamanız gerekir. ---'''
'''--- Örnek 1 :'''
# list[0] = 58
# tuple[0] = 58
'''TypeError: 'tuple' object does not support item assignment.'''

'''Hata almamak için tekrardan atamalısınız : '''
# list = [57,'XYZ',18.79,58]
# tuple = [57,'XYZ',18.79,58]

'''Tuple sadece .index ve .count metotlarını destekler.'''
# tuple.count(57)
# tuple.index('XYZ')

'''Tuple tipindeki verileri toplayabilirsiniz. (Tuple + Tuple)'''
# brands0 = ('MSI','Lenovo','Dell')
# brands1 = ('Asus','Acer','Monster')
# print(brands0 + brands1)