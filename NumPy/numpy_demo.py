import numpy as np

# # 1

# array = np.array([10,15,30,45,60])

# # 2

# array = np.arange(5,15)

# # 3

# array = np.arange(50,100,5)

# # 4

# array = np.zeros(10)

# # 5

# array = np.ones(10)

# # 6

# array = np.linspace(0,100,5)

# # 7

# array = np.random.randint(10,30,5)

# # 8

# array = np.random.randn(10)

# # 9

# array = np.random.randint(10,50,15).reshape(3,5)

# # 10

# sum_v = array.sum(axis=1)
# sum_h = array.sum(axis=0)
# print(f"Satır sayıları toplamı = {sum_v} .\nSütun sayıları toplamı = {sum_h} .")

# # 11

# arg_min = array.min()
# arg_max = array.max()
# mean = array.mean()
# print(f"Max terim = {arg_max}\nMin terim = {arg_min}\nOrtalama = {mean}")

# # 12

# max_index = array.argmax()
# print(max_index)

# # 13

# array = np.arange(10,20)
# print(array[:3])

# # 14

# print(array[::-1])

# # 15

# multi_array = array.reshape(2,5)
# print(multi_array[0,:])
# print(multi_array)

# # 16

# print(multi_array[1,2])

# # 17

# print(multi_array[:,0])

# # 18   ek soru :)

# print(np.sqrt(array))

# # 19

# print(array ** 2)

# # 20

# array = np.arange(-50,50)
# term = (array % 2 == 0) & (array > 0)
# print(array[term])



print(array)
