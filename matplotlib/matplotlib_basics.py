# Docs: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

import matplotlib.pyplot as plt
import numpy as np

"""
matplotlib ile grafik oluşturma
"""

# x = [1,2,3,4]
# y = [1,4,9,16]

# # plt.plot(x,y,color="red",linewidth="5")
# plt.plot(x,y,"o--r")

# plt.axis([0,6,0,20])

# plt.title("Figure 1")
# plt.xlabel("values")
# plt.ylabel("sq values")

"""
tek grafikte birçok farklı çizim
"""

# x = np.linspace(0,2,100)

# plt.plot(x,x,label="linear",color="red")
# plt.plot(x,x**2,label="quadratic",color="yellow")
# plt.plot(x,x**3,label="cubic",color="green")

# plt.xlabel("x label")
# plt.ylabel("y label")

# plt.legend()

# plt.title("Simple Figure")


# plt.show()

"""
subplot çizimi
"""

# x = np.linspace(0,2,100)
# fgr,axs = plt.subplots(3)

# axs[0].plot(x,x,color="red")
# axs[1].plot(x,x**2,color="green")
# axs[2].plot(x,x**3,color="yellow")

# axs[0].set_title("linear")
# axs[1].set_title("quadratic")
# axs[2].set_title("qubic")

# plt.tight_layout()

"""
axes kullanarak çizim
"""

# x = np.linspace(0,2,100)
# fgr,axs = plt.subplots(2,2)
# fgr.suptitle("Linear-Quadratic-Qubic-4th power Functions")

# axs[0,0].plot(x,x,color="red")
# axs[0,1].plot(x,x**2,color="green")
# axs[1,0].plot(x,x**3,color="yellow")
# axs[1,1].plot(x,x**4,color="blue")

# axs[0,0].set_title("linear")
# axs[0,1].set_title("quadratic")
# axs[1,0].set_title("qubic")
# axs[1,1].set_title("4th power")

# plt.tight_layout()

"""
gerçek veriler üzerinde (nba.csv) çizim denemesi
"""

# import pandas as pd

# df = pd.read_csv("nba.csv")

# df = df.drop(["Number"], axis = 1).groupby("Team").mean()
# df.head().plot(subplots=True)
# plt.legend()

plt.show()




