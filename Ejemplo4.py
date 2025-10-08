#Histrograma
#¿Cuanto tiempo tardas en llegar a la Universidad en minutos?
import matplotlib.pyplot as plt


tiempos = [10, 120, 60, 120, 20, 200, 40, 300, 90, 10, 120]


plt.hist(tiempos, bins=8, color='purple', edgecolor='black', alpha=0.8)


plt.title("Tiempo para llegar a la Universidad (en minutos)")
plt.xlabel("Minutos")
plt.ylabel("Frecuencia de estudiantes")


plt.show()

