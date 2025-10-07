# Grafico de barras
# ¿Cuantas tazas de cafe tomas al dia?

import matplotlib.pyplot as plt
import numpy as np

categorias = ["0 tazas", "1 taza", "2 tazas"]
frecuencias = [5, 4, 2] 


x_pos = np.arange(len(categorias))

color_purpura = '#673ab7'
barras = plt.bar(x_pos, frecuencias, color=color_purpura)

plt.xticks(x_pos, categorias)
plt.ylabel("Número de Respuestas")
plt.title("¿Cuántas tazas de café tomas al día?")
plt.ylim(0, max(frecuencias) + 1) 


for bar in barras:
    yval = bar.get_height()
    
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom')

plt.show()