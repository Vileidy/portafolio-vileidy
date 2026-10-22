#!/usr/bin/env python3
"""Convierte el material original del portafolio en archivos listos para la web y para Git.

    python scripts/preparar-material.py                 procesa todo el catálogo
    python scripts/preparar-material.py --solo hdi-menu,moxi-du
    python scripts/preparar-material.py --origen "D:/otra/carpeta"

Qué hace:
  * Lee cada pieza de scripts/catalogo.py desde "PORTAFOLIO 2026 OK/Imag Categorias".
  * Quita el marco de presentación (borde negro + pie "Programa/Diseño") que traen las
    láminas de 550/600 px y deja solo la pieza.
  * Convierte JPG/PNG/TIF/PSD/GIF/PDF a WebP (los GIF quedan animados) y los guarda en
    src/assets/work/<disciplina>/<id>.webp, ya redimensionados.
  * Genera src/data/catalogo.json con medidas y textos, que es lo que lee el sitio.
  * Extrae de Portada.jpg y Barra inicial.psd el retrato y el patrón "V" de la marca
    (src/assets/brand/).

Los originales (156 MB) no se tocan ni se suben a Git. Requisitos: Python 3.10+ y
`pip install -r scripts/requirements.txt`.
"""
import argparse
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import fitz  # PyMuPDF
import numpy as np
from PIL import Image, ImageSequence
from psd_tools import PSDImage

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalogo import DISCIPLINAS, ITEMS  # noqa: E402

Image.MAX_IMAGE_PIXELS = None

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "PORTAFOLIO 2026 OK"
OUT_WORK = ROOT / "src" / "assets" / "work"
OUT_BRAND = ROOT / "src" / "assets" / "brand"
OUT_JSON = ROOT / "src" / "data" / "catalogo.json"

# Alias del catálogo -> nombre real de la carpeta, comparado sin símbolos ni mayúsculas
CARPETAS = {
    "banners": "banners",
    "email": "emailmarketing",
    "logos": "logos",
    "mobile": "mobileaplicaciones",
    "pop": "pop",
    "web": "paginaweb",
    "pendones": "pendones",
    "redes": "redessociales",
    "ia": "generadasia",  # imágenes generadas con IA (ver docs/imagenes-con-codex.md)
}

# Colores de la marca (extraídos de Barra inicial.psd) y su versión pastel
MARCA_TEAL, MARCA_MORADO = "#35b1cd", "#6f3e97"
PASTEL_AQUA, PASTEL_LAVANDA = "#a9e4f0", "#cbb5f0"


def clave(nombre: str) -> str:
    """Nombre sin espacios, símbolos ni mayúsculas, conservando la extensión."""
    p = Path(nombre.strip())
    stem = unicodedata.normalize("NFKD", p.stem.lower())
    return re.sub(r"[^a-z0-9]+", "", stem) + p.suffix.lower()


def clave_carpeta(nombre: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", unicodedata.normalize("NFKD", nombre.lower()))


def indexar(origen: Path) -> dict:
    idx = {}
    for carpeta in origen.iterdir():
        if not carpeta.is_dir():
            continue
        ck = clave_carpeta(carpeta.name)
        for f in carpeta.iterdir():
            # los ._* son metadatos de macOS que se cuelan al comprimir, no imágenes
            if f.is_file() and not f.name.startswith("._"):
                idx[(ck, clave(f.name))] = f
    return idx


def localizar(idx: dict, src: str) -> Path | None:
    alias, nombre = src.split("/", 1)
    return idx.get((CARPETAS[alias], clave(nombre)))


# ───────────────────────── marcos de presentación ─────────────────────────
def _corrida_oscura(linea: np.ndarray):
    """(inicio, fin) del primer tramo oscuro si parece un borde de 5–40 px cerca del extremo."""
    oscuros = np.where(linea < 40)[0]
    if len(oscuros) == 0 or oscuros[0] > 30:
        return None
    s = int(oscuros[0])
    e = s
    while e < len(linea) and linea[e] < 128:
        e += 1
    return (s, e) if 5 <= e - s <= 40 else None


def caja_interior_marco(rgb: np.ndarray):
    """Caja interior de una lámina con borde negro, o None si la imagen no es una lámina."""
    h, w = rgb.shape[:2]
    if not (500 <= min(w, h) <= 620 and abs(w - h) <= 60):
        return None
    g = rgb.max(axis=2)
    izq, der = _corrida_oscura(g[h // 2]), _corrida_oscura(g[h // 2][::-1])
    sup, inf = _corrida_oscura(g[:, w // 2]), _corrida_oscura(g[:, w // 2][::-1])
    if None in (izq, der, sup, inf):
        return None
    return izq[1], sup[1], w - der[1], h - inf[1]


def quitar_marco(im: Image.Image, pie: float = 0.62) -> Image.Image:
    """Recorta una lámina de presentación y deja solo la pieza.

    pie: fracción del ancho donde puede llegar el texto del pie; subirla si el pie es muy largo.
    """
    rgb = np.asarray(im.convert("RGB"))
    caja = caja_interior_marco(rgb)
    if caja is None:
        return im
    x0, y0, x1, y1 = caja
    inset = 10  # el borde negro deja una franja difuminada en su lado interior
    sub = rgb[y0 + inset:y1 - inset, x0 + inset:x1 - inset].copy()
    ih, iw = sub.shape[:2]
    # Pie de la lámina: marca de agua (esquina) y texto "Programa / Diseño" en gris sin color.
    # Se borra por color y no por geometría para no cortar piezas que llegan hasta abajo.
    sub[int(ih * 0.84):, : int(iw * 0.13)] = 255
    zona = sub[int(ih * 0.88):, : int(iw * pie)]
    gris = ((zona.max(axis=2).astype(int) - zona.min(axis=2)) < 32) & (zona.min(axis=2) > 70)
    zona[gris] = 255
    contenido = sub.min(axis=2) < 244
    # las esquinas redondeadas del borde negro asoman dentro de la caja: no son contenido
    esquina = 14
    contenido[:esquina, :esquina] = contenido[:esquina, -esquina:] = False
    contenido[-esquina:, :esquina] = contenido[-esquina:, -esquina:] = False
    # filas/columnas con apenas unos píxeles son restos del pie, no la pieza
    filas = np.where(contenido.sum(axis=1) >= 6)[0]
    cols = np.where(contenido.sum(axis=0) >= 6)[0]
    if len(filas) == 0 or len(cols) == 0:
        return im
    pad = 4
    cx0, cx1 = max(cols.min() - pad, 0), min(cols.max() + 1 + pad, iw)
    cy0, cy1 = max(filas.min() - pad, 0), min(filas.max() + 1 + pad, ih)
    return Image.fromarray(sub[cy0:cy1, cx0:cx1])


# ───────────────────────── conversión ─────────────────────────
def ajustar_ancho(im: Image.Image, w: int) -> Image.Image:
    if im.width <= w:
        return im
    return im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)


def abrir_estatica(path: Path, item: dict) -> Image.Image:
    if path.suffix.lower() == ".pdf":
        doc = fitz.open(path)
        pg = doc[item["page"] - 1]
        z = item["w"] / pg.rect.width
        pix = pg.get_pixmap(matrix=fitz.Matrix(z, z), alpha=False)
        return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    im = Image.open(path)
    im.load()
    if item["crop"]:
        im = im.convert("RGB").crop(item["crop"])
    elif im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        im = im.convert("RGBA")
    else:
        im = quitar_marco(im.convert("RGB"), item["pie"])
    return im


def guardar_animado(path: Path, item: dict, destino: Path) -> tuple[int, int, int]:
    im = Image.open(path)
    frames, duraciones = [], []
    for f in ImageSequence.Iterator(im):
        duraciones.append(max(int(f.info.get("duration", 100)), 40))
        frames.append(ajustar_ancho(f.convert("RGBA"), item["w"]).copy())
    frames[0].save(destino, "WEBP", save_all=True, append_images=frames[1:],
                   duration=duraciones, loop=0, quality=80, method=4)
    return frames[0].width, frames[0].height, len(frames)


def procesar_item(item: dict, path: Path) -> dict:
    ext = path.suffix.lower()
    carpeta = OUT_WORK / item["disc"]
    carpeta.mkdir(parents=True, exist_ok=True)
    registro = {k: item[k] for k in ("id", "disc", "brand", "title", "alt", "desc", "project", "gallery", "kind")}
    frames = 1

    if ext == ".svg":
        texto = path.read_text(encoding="utf-8")
        if re.search(r"<script|onload=|javascript:", texto, re.I):
            raise ValueError(f"{path.name}: el SVG trae scripts; no se copia")
        destino = carpeta / f"{item['id']}.svg"
        shutil.copyfile(path, destino)
        m = re.search(r'viewBox="[\d.\-]+\s+[\d.\-]+\s+([\d.]+)\s+([\d.]+)"', texto)
        w, h = (round(float(m.group(1))), round(float(m.group(2)))) if m else (315, 119)
    elif ext == ".gif" and getattr(Image.open(path), "is_animated", False):
        destino = carpeta / f"{item['id']}.webp"
        w, h, frames = guardar_animado(path, item, destino)
    else:
        destino = carpeta / f"{item['id']}.webp"
        im = ajustar_ancho(abrir_estatica(path, item), item["w"])
        calidad = 90 if item["kind"] in ("screen", "flow", "web") else 84
        im.save(destino, "WEBP", quality=calidad, method=6)
        w, h = im.size

    registro.update(file=f"{item['disc']}/{destino.name}", w=w, h=h, frames=frames,
                    bytes=destino.stat().st_size)
    return registro


# ───────────────────────── identidad de marca ─────────────────────────
def procesar_marca():
    OUT_BRAND.mkdir(parents=True, exist_ok=True)
    portada = BASE / "Portada.jpg"
    barra = BASE / "Barra inicial.psd"

    if portada.exists():
        # El retrato sale de la portada. Se sube el blanco para que el gris del fondo (#DDD)
        # y el blanco de la camisa desaparezcan con mix-blend-mode: multiply sobre el pastel.
        g = Image.open(portada).convert("L").crop((225, 100, 565, 450))
        a = np.asarray(g).astype(np.float32)
        a = np.clip(a * (255.0 / 222.0), 0, 255).astype(np.uint8)
        r = Image.fromarray(a).resize((g.width * 2, g.height * 2), Image.LANCZOS)
        r.save(OUT_BRAND / "retrato.webp", "WEBP", quality=90, method=6)
        print(f"  marca/retrato.webp {r.size}")

    if barra.exists():
        # El monograma "V" vive como objeto inteligente vectorial (PDF) dentro del PSD.
        for capa in PSDImage.open(barra):
            if capa.kind == "smartobject":
                doc = fitz.open(stream=capa.smart_object.data, filetype="pdf")
                svg = doc[0].get_svg_image()
                svg = svg.replace(MARCA_TEAL, PASTEL_AQUA).replace(MARCA_MORADO, PASTEL_LAVANDA)
                (OUT_BRAND / "patron-v.svg").write_text(svg, encoding="utf-8")
                print(f"  marca/patron-v.svg ({len(svg) // 1024} KB)")
                break


# ───────────────────────── main ─────────────────────────
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--origen", help='carpeta con las subcarpetas de trabajos (por defecto "PORTAFOLIO 2026 OK/Imag Categorias")')
    ap.add_argument("--solo", help="ids separados por coma")
    args = ap.parse_args()

    origen = Path(args.origen) if args.origen else BASE / "Imag Categorias"
    if not origen.is_dir():
        sys.exit(f"No encuentro {origen}")
    solo = set(args.solo.split(",")) if args.solo else None

    idx = indexar(origen)
    ids = [i["id"] for i in ITEMS]
    duplicados = {i for i in ids if ids.count(i) > 1}
    if duplicados:
        sys.exit(f"Ids repetidos en catalogo.py: {sorted(duplicados)}")

    faltan = [i["src"] for i in ITEMS if localizar(idx, i["src"]) is None]
    if faltan:
        sys.exit("No se encontraron estos archivos:\n  " + "\n  ".join(faltan))

    print(f"Procesando {len(ITEMS)} piezas desde {origen}")
    registros = []
    for item in ITEMS:
        if solo and item["id"] not in solo:
            continue
        reg = procesar_item(item, localizar(idx, item["src"]))
        registros.append(reg)
        print(f"  {reg['file']:<46} {reg['w']:>5}x{reg['h']:<5} {reg['bytes'] // 1024:>5} KB"
              + (f"  [{reg['frames']} cuadros]" if reg["frames"] > 1 else ""))

    if not solo:
        procesar_marca()
        OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
        salida = {
            "disciplinas": [{"id": i, "label": l} for i, l in DISCIPLINAS],
            "items": [{k: v for k, v in r.items() if k != "bytes"} for r in registros],
        }
        OUT_JSON.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        total = sum(r["bytes"] for r in registros)
        print(f"\n{len(registros)} piezas, {total / 1024 / 1024:.1f} MB en total -> {OUT_JSON.relative_to(ROOT)}")
        grandes = sorted(registros, key=lambda r: -r["bytes"])[:5]
        print("Las más pesadas: " + ", ".join(f"{r['id']} ({r['bytes'] // 1024} KB)" for r in grandes))


if __name__ == "__main__":
    main()
