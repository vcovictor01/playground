import numpy as np
import matplotlib.pyplot as plt

# definindo tempo entre -1 s e 1 s com 200 'pontos'
t = np.linspace(-0.01, 0.01, 200)

#definindo a função de onda
def funcaoOnda(A, T):
    return A*np.sin(1000*T)

#definindo a função de tensão de saída
def funcaoVOUT(VIN):
    a = np.e**VIN
    return ((a-(1/a))/(a+(1/a)))


# vin para o caso 1
vin1 = funcaoOnda(10, t)
# vout para o caso 1
vout1 = funcaoVOUT(vin1)


# vin para o caso 2
vin2 = funcaoOnda(1, t)
# vout para o caso 2
vout2 = funcaoVOUT(vin2)


# criando v entrada para o gráfico 2
vin = np.linspace(-4,4,200)
# criando v saida para o gráfico 2
vout = funcaoVOUT(vin)


# plota o gráfico
plt.subplot(2,2,1)
plt.plot(t, vin1)
plt.xlabel("tempo (s)")
plt.xticks([-0.01, 0, 0.01])
plt.ylabel("tensão [V]")
plt.text(-0.01, 7, 'Input', fontsize=12, color='red')

plt.subplot(2,2,2)
plt.plot(vin, vout)
plt.xlabel("tensão de entrada [V]")
plt.ylabel("tensão de saída [V]")
plt.text(-4, 0.7, 'Característica de Transferência do Amplificador', fontsize=10, color='red')

plt.subplot(2,2,3)
plt.plot(t, vout1)
plt.xlabel("tempo (s)")
plt.xticks([-0.01, 0, 0.01])
plt.ylabel("tensão de saída [v]")
plt.text(-0.01, 0.5, 'Caso 1', fontsize=12, color='red')

plt.subplot(2,2,4)
plt.plot(t, vout2)
plt.xlabel("tempo (s)")
plt.xticks([-0.01, 0, 0.01])
plt.ylabel("tensão de saída [v]")
plt.text(-0.01, 0.5, 'Caso 2 - Small Signal', fontsize=12, color='red')

plt.show()