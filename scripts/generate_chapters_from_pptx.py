import os
from pathlib import Path
import glob

# Paths
RESOURCES_DIR = Path(r"u:/antigravityprojects/libroprueba/pruebacurso/Recursos")
STATIC_IMG_DIR = Path(r"u:/antigravityprojects/libroprueba/pruebacurso/book/_static/recursos")
ES_CHAPTER_DIR = Path(r"u:/antigravityprojects/libroprueba/pruebacurso/book/es/recursos")
EN_CHAPTER_DIR = Path(r"u:/antigravityprojects/libroprueba/pruebacurso/book/en/recursos")

ES_CHAPTER_DIR.mkdir(parents=True, exist_ok=True)
EN_CHAPTER_DIR.mkdir(parents=True, exist_ok=True)

# Mapping for English titles (simple placeholders)
EN_TITLES = {
    "TEMA 1 - Campo Electrico I": "Electric Field I",
    "TEMA 2 - Campo Electrico II": "Electric Field II",
    "TEMA 3 - Potencial Electrico": "Electric Potential",
    "TEMA 4 - Capacidad": "Capacitance",
    "TEMA 5 - Corriente Electrica y Circuitos de Corriente Continua": "Electric Current and DC Circuits",
    "TEMA 6 - Campo Magnetico new": "Magnetic Field",
    "TEMA 7 - Fuentes del Campo Magnetico new": "Magnetic Field Sources",
    "TEMA 8 - Induccion Electromagnetica": "Electromagnetic Induction",
    "TEMA 9 - Corriente Alterna": "Alternating Current",
    "TEMA 10 - Ecuaciones de Maxwell": "Maxwell Equations",
}

def slugify(name: str) -> str:
    # Replace spaces and special chars with underscores, remove diacritics not needed for filenames
    return name.replace(' ', '_').replace('-', '_').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')

for pptx_path in RESOURCES_DIR.glob('*.pptx'):
    stem = pptx_path.stem  # e.g., "TEMA 1 - Campo Electrico I"
    # Build filenames compatibles con TOC
    # Convert "TEMA 1 - Campo Electrico I" → "TEMA_1_Campo_Electrico_I.md"
    def to_toc_name(name: str) -> str:
        # Replace " - " and spaces with underscores, collapse multiple underscores
        return "_".join(part for part in name.replace(" - ", "_").replace(" ", "_").split("_") if part) + ".md"
    es_file_name = to_toc_name(stem)
    en_title = EN_TITLES.get(stem, stem)
    en_file_name = to_toc_name(en_title)

    # Gather images for this pptx
    image_pattern = STATIC_IMG_DIR / f"{stem}_slide*.*"
    image_files = sorted(STATIC_IMG_DIR.glob(f"{stem}_slide*.*"))

    # Build markdown content
    es_content = f"# {stem}\n\n*Resumen del contenido del PPT proporcionado por el docente.*\n\n"
    en_content = f"# {en_title}\n\n*Summary of the PPT content provided by the teacher.*\n\n"
    for img_path in image_files:
        rel_path = img_path.relative_to(Path(r"u:/antigravityprojects/libroprueba/pruebacurso/book"))
        figure_block = f"```{{figure}} {rel_path.as_posix()}\n:alt: Diapositiva\n:width: 80%\n:align: center\n```\n\n"
        es_content += figure_block
        en_content += figure_block

    # Write files
    (ES_CHAPTER_DIR / es_file_name).write_text(es_content, encoding='utf-8')
    (EN_CHAPTER_DIR / en_file_name).write_text(en_content, encoding='utf-8')

print('Capítulos generados exitosamente.')
