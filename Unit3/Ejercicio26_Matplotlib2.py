import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 2, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

# Completar la gráfica
# Etiqueta en el eje X
plt.xlabel('tiempo(s)')
# Etiqueta en el eje Y
plt.ylabel('voltaje (mV)')
# Título
plt.title('Gráfico simple de DAW')
# grid rejilla
plt.grid(True)
plt.savefig('ej26imagen.png')
plt.show()