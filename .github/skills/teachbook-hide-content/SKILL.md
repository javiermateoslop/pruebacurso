---
name: teachbook-hide-content
description: >
  Guía paso a paso para ocultar capítulos o páginas del libro web y PDF correctamente,
  sin necesidad de borrar los archivos físicos del repositorio. Utiliza exclude_patterns
  para garantizar compatibilidad completa con Jupyter Book sin warnings de archivos huérfanos.
  Trigger phrases: "ocultar capítulo", "ocultar página", "esconder sección", "eliminar del PDF",
  "ocultar del menú", "no mostrar en PDF", "hide chapter".
---

# Skill: Ocultar contenido de forma segura (HTML y PDF)

## Cuándo usar esta skill

- Cuando el usuario quiere ocultar capítulos antiguos o borradores sin eliminar sus archivos `.md` o `.ipynb`.
- Cuando se desea que un capítulo no aparezca en la versión Web (HTML) y, por tanto, tampoco se imprima en el PDF exportado.
- Para evitar errores de "archivos huérfanos" (orphan pages) al quitar entradas del índice (`_toc.yml`).

## Concepto clave

En Jupyter Book, la construcción completa (y por tanto la exportación PDF) compila todo lo que hay en la carpeta, a menos que se le indique lo contrario. Para que un capítulo desaparezca **por completo** de todas las versiones, debes hacer **DOS** cosas simultáneamente en todos los idiomas:
1. Eliminarlo del árbol de navegación (`_toc.yml`).
2. Excluir el archivo físico en la configuración (`_config.yml`).

## Pasos a seguir por el agente

Cuando el usuario pida ocultar el capítulo `X` (por ejemplo, `es/02_grados/grado_fisica/intro.md`), aplica los siguientes pasos estrictamente en **TODOS** los idiomas configurados:

### Paso 1: Eliminar del Índice (`_toc.yml`)

1. Abre `book/_toc_es.yml` y `book/_toc_en.yml` (y otros idiomas si los hay).
2. Localiza la referencia al archivo (`- file: es/...`).
3. Bórrala o coméntala usando `#`.
   - Si la sección `chapters:` se queda vacía tras esto, bórrala también o añade un archivo placeholder temporal.

### Paso 2: Añadir a Exclusiones (`_config.yml`)

1. Abre `book/_config_es.yml` y localiza la clave `exclude_patterns`. Si no existe, créala en la raíz del YAML:
   ```yaml
   exclude_patterns: ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints", "en/", "_TRASH*"]
   ```
2. Añade la ruta del archivo o carpeta a ocultar. Puedes usar comodines `*`:
   ```yaml
   exclude_patterns: ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints", "en/", "_TRASH*", "es/02_grados/grado_fisica*"]
   ```
3. Repite el proceso EXACTAMENTE IGUAL en `book/_config_en.yml`, excluyendo el equivalente en inglés:
   ```yaml
   exclude_patterns: ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints", "es/", "_TRASH*", "en/02_degrees/physics_degree*"]
   ```

### Paso 3: Recompilar (Validación)

Una vez aplicados los cambios, verifica que la web y el PDF se compilan sin problemas y que no saltan warnings de "orphan pages" (páginas huérfanas).

```bash
python scripts/build_book.py
```
*(Si el usuario lo requiere expresamente, ejecuta también `python scripts/export_pdf.py --engine auto` para que compruebe los PDFs).*

## Alternativa: La carpeta \`_TRASH\`

El entorno tiene configurado de base que cualquier archivo o carpeta que empiece por `_TRASH` será ignorado (`exclude_patterns: ["_TRASH*"]`).
Una alternativa rápida y segura a modificar el `_config.yml` es mover la carpeta a desechar a una subcarpeta que empiece por `_TRASH`:

```bash
# Ejemplo PowerShell
mkdir book/es/_TRASH
mv book/es/02_grados book/es/_TRASH/02_grados
```

Recuerda que en todo caso **siempre debes quitar su referencia en el `_toc.yml`**.
