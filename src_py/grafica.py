import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.title("Mi primer grafico")
plt.xlabel("Eje de la X")
plt.ylabel("Eje de las y")
plt.plot(x, y, label= "Datos")
plt.legend()

plt.show()