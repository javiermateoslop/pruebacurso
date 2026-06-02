import os
import shutil

base_dir = "book"

# 1. Update configs
def update_config(config_path):
    if not os.path.exists(config_path): return
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('execute_notebooks: off', 'execute_notebooks: auto')
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(content)

update_config(os.path.join(base_dir, '_config_es.yml'))
update_config(os.path.join(base_dir, '_config_en.yml'))

# 2. Cleanup old folders
for lang in ['es', 'en']:
    lang_dir = os.path.join(base_dir, lang)
    for item in os.listdir(lang_dir):
        if item == 'intro.md':
            continue
        item_path = os.path.join(lang_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

# 3. Create new content
es_dir = os.path.join(base_dir, 'es', '08_graficas_dinamicas')
en_dir = os.path.join(base_dir, 'en', '08_dynamic_graphs')
os.makedirs(es_dir, exist_ok=True)
os.makedirs(en_dir, exist_ok=True)

es_content = """# Gráficas Dinámicas

A continuación, se muestra una gráfica dinámica.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Gráfica de Seno')
plt.show()
```
"""

en_content = """# Dynamic Graphs

Below is a dynamic graph.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Graph')
plt.show()
```
"""

with open(os.path.join(es_dir, 'intro.md'), 'w', encoding='utf-8') as f:
    f.write(es_content)

with open(os.path.join(en_dir, 'intro.md'), 'w', encoding='utf-8') as f:
    f.write(en_content)

# 4. Overwrite TOCs
toc_es = """format: jb-book
root: es/intro
parts:
  - caption: Gráficas Dinámicas
    chapters:
    - file: es/08_graficas_dinamicas/intro
"""

toc_en = """format: jb-book
root: en/intro
parts:
  - caption: Dynamic Graphs
    chapters:
    - file: en/08_dynamic_graphs/intro
"""

with open(os.path.join(base_dir, '_toc_es.yml'), 'w', encoding='utf-8') as f:
    f.write(toc_es)

with open(os.path.join(base_dir, '_toc_en.yml'), 'w', encoding='utf-8') as f:
    f.write(toc_en)

print("Cleanup and creation complete.")
