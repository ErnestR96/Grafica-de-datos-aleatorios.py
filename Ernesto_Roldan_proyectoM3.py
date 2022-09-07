#Será la simulación de una máquina de Galton de 3000 canicas. 
#En total tendrá 12 niveles de obstáculos 
#El resultado final será un histograma que represente la cantidad de canicas en cada contenedor\
# como el siguiente -No olvides colocar nombre a los ejes y un título al gráfico. 
#Deberás emplear dos funciones, una para calcular los resultados de las canicas y la \
# segunda para la graficación del histograma. 

import numpy as np
import matplotlib.pyplot as plt
from random import randint

# se definen dos funciones: la primera para obtener el factor que multiplicado por cada canica \
#distribuya 3000 canicas en una gráfica de manera proporcional dando como resultado una forma de campana
#la segunda función pretende generar la gráfica de histograma a traves de 3 variables: valores del eje X\
  #número de barras y color
def factor(x):
    numero =(x)**1*250
    return (numero)
    """
    Función que calcula el factor que origina la distribución de la campana de Galton 
    """
def graficar(columna):
    X = np.arange(len(columna))
    plt.suptitle('Tablero de Galton')
    plt.bar(X, columna, color = 'red')
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')
    plt.show()
    """
    Función que gráfica un histograma
    """
#A continuación se pide al usuario definir el número de barras o niveles del histograma    
niveles = int(input('Dime cuantos niveles de la campana (min 1/ max 12): '))

#mediante iteraciones con el ciclo "for" se repite el proceso de distribuir las canicas en los\
#niveles respectivos definidos por el usuario
carriles = [0]*(niveles)
for i in range(factor(niveles)):
  guardado = -1

  for i in range(niveles):
    guardado += randint(0, 1)
  carriles[guardado] += 1

#finalmente se gráfican los valores 
print(f' se usaron {factor(niveles)}, canicas en total')
print(carriles)

graficar(carriles)

    