import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

"""
figure = plt.figure()

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
# figure alanını 1x1 olarak düşünüyoruz. parametre listedeki ilk
# değer soldan bırakılacak boşluk, ikinci değer alttan bırakılacak
# boşluk, üçüncü değer soldan sağa genişlik, dördüncü değer ise
# aşağıdan yukarı yüksekliği ifade eder.

axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("x value")
axes_cube.set_ylabel("y label")
axes_cube.set_title("Cubic")

axes_sq = figure.add_axes([0.15,0.6,0.25,0.25])

axes_sq.plot(x,z,"r")
axes_sq.set_xlabel("x value")
axes_sq.set_ylabel("z label")
axes_sq.set_title("Quadratic")

plt.legend()
"""

"""
figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=2) # loc = 1 -> sağ üst, 2 -> sol üst, 3 -> sol alt, 4 -> sağ alt
"""

"""
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(6,4))
# Verilen figsize parametresi figure boyutunu belirler.
# Örneğin yukarıda (6,4) verdiğimiz boyut sonucunda
# 600 x 400 bir düzlem karşımıza gelecektir.
# Bu durumda figsize=(x,y) dersek elimizdeki düzlem
# x*100 x y*100 pixel boyutunda olacaktır.

axes[0].plot(x,y)
axes[0].set_title("Qubic")

axes[1].plot(x,z)
axes[1].set_title("Quadratic")

plt.tight_layout()

# fig.savefig("qubicAndQuadraticFuncs.png")   # .png kaydeder
# fig.savefig("qubicAndQuadraticFuncs.pdf")   # .pdf kaydeder
"""


plt.show()
