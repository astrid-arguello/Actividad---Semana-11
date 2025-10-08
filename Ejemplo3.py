# Gráfico de pastel
#Cual red social usas mas 

import matplotlib.pyplot as plt

redes = ['Instagram', 'Tik Tok', 'Tiktok', 'Todas', 'WhatsApp', 'tiktok']
porcentajes = [36.4, 18.2, 18.2, 9.1, 9.1, 9.1]

plt.pie(
    porcentajes,
    labels=redes,
    autopct='%1.1f%%',   # Muestra los porcentajes
    startangle=90,       
    colors=['violet', 'purple', 'mediumpurple', 'plum', 'orchid', 'thistle']
)

plt.title('¿Cuál red social usas más?')

plt.axis('equal')

plt.show()
