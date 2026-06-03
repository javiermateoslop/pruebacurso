import os
import subprocess
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATIC_RECURSOS = PROJECT_ROOT / "book" / "_static" / "recursos"

def convert_wmf_to_png(wmf_path: Path) -> Path:
    """Convert a .wmf file to .png using ImageMagick (magick). Returns the new png path."""
    png_path = wmf_path.with_suffix('.png')
    # Use ImageMagick's magick command. It should be available in the .venv environment or system.
    subprocess.run(["magick", "convert", str(wmf_path), str(png_path)], check=True)
    return png_path

def update_markdown_references():
    """Search markdown files for .wmf references and replace with .png equivalents."""
    md_files = list(PROJECT_ROOT.glob('book/**/*.md'))
    for md_file in md_files:
        text = md_file.read_text(encoding='utf-8')
        updated = False
        for wmf_file in STATIC_RECURSOS.glob('*.wmf'):
            wmf_rel = f"../../_static/recursos/{wmf_file.name}"
            png_rel = f"../../_static/recursos/{wmf_file.stem}.png"
            if wmf_rel in text:
                text = text.replace(wmf_rel, png_rel)
                updated = True
        if updated:
            md_file.write_text(text, encoding='utf-8')
            print(f"Updated references in {md_file}")

def main():
    # Convert all .wmf files
    for wmf_file in STATIC_RECURSOS.glob('*.wmf'):
        try:
            png_path = convert_wmf_to_png(wmf_file)
            print(f"Converted {wmf_file.name} -> {png_path.name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {wmf_file.name}: {e}")
    # Update markdown files
    update_markdown_references()

if __name__ == "__main__":
    main()
