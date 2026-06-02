# Gráficas Dinámicas

A continuación, se muestra una gráfica dinámica.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))
plt.title('Gráfica de Seno Animada')
plt.close(fig)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

ani = FuncAnimation(fig, update, frames=60, interval=50, blit=True)
HTML(ani.to_jshtml())
```
