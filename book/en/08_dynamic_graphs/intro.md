# Dynamic Graphs

Below is a dynamic graph.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
line, = ax.plot(x, np.sin(x))
plt.title('Animated Sine Graph')
plt.close(fig)

def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

ani = FuncAnimation(fig, update, frames=60, interval=50, blit=True)
HTML(ani.to_jshtml())
```
