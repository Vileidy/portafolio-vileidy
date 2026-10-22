# material/

Zona de trabajo para material **nuevo** y sencillo (fotos, capturas). **Todo lo que pongas aquí se queda fuera de Git**; solo este README se versiona.

> El material actual del portafolio vive en `PORTAFOLIO 2026 OK/` y se procesa con `npm run material` (ver el README principal). Esta carpeta es una alternativa rápida para imágenes sueltas que no necesiten curarse en `scripts/catalogo.py`.

## Uso

1. Crea una carpeta por proyecto y mete dentro las imágenes: `material/nombre-del-proyecto/01-portada.jpg`.
2. Ejecuta `npm run images`. Genera WebP (máx. 2400 px de ancho, calidad 82, sin metadatos ni GPS) en `src/assets/work/<carpeta>/`, que sí va a Git. Los nombres se normalizan (`Mi Foto.JPG` → `mi-foto.webp`).
3. `npm run images -- --force` regenera todo.

Para que una imagen aparezca en el sitio hay que registrarla en `scripts/catalogo.py` y volver a ejecutar `npm run material`.

## Límites de Git / GitHub Pages

- Un archivo individual no puede pasar de **100 MB** y el repo conviene mantenerlo por debajo de ~1 GB. El sitio publicado en Pages tiene un límite de ~1 GB.
- **Vídeo y GIF animados**: no los pongas tal cual. Exporta a MP4/WebM ligero (< 10 MB por clip) o súbelos a YouTube/Vimeo y haz *embed*. Los GIF de email actuales se convierten a WebP animado.
- Archivos de edición (PSD, AI, TIFF enormes) se quedan fuera de `src/`.
