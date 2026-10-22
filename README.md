# Portafolio de Vileidy Muñoz

Portafolio de diseño (UI/UX, web, campañas digitales, marca e impresos), divertido, animado y en tonos pastel. Sitio estático hecho con [Astro](https://astro.build), [GSAP](https://gsap.com) y [Lenis](https://lenis.darkroom.engineering), listo para publicarse en GitHub Pages.

La paleta sale de la barra original (cian `#35b1cd` y morado `#6f3e97`) llevada a pastel; el título enorme, la firma manuscrita, las comillas con barras y el monograma "V" vienen de `Portada.jpg` y `Barra inicial.psd`.

## Qué hay en el sitio

| Ruta | Contenido |
|---|---|
| `/` | Hero, marcas, "lo que hago", 5 casos destacados, galería filtrable con visor, sobre mí, contacto |
| `/proyectos/hdi-seguros/` | App móvil: 11 pantallas, páginas responsivas y 9 tableros de flujo (del PDF) |
| `/proyectos/datamars-livestock/` | Dos páginas web en ventanas de navegador que se desplazan con el scroll |
| `/proyectos/centro-clinico-atenea/` | Maqueta web y logotipo |
| `/proyectos/rip-curl/` | Banners y emails animados de Rip Curl, Rusty y Volcom |
| `/proyectos/tumedico/` | Redes, banners, emailing, pendón y papelería de Tumedico.com |

## Empezar

Requiere Node >= 22.23.4 (`.nvmrc` indica 24).

```bash
npm install
npm run dev        # http://localhost:4321
```

| Comando | Qué hace |
|---|---|
| `npm run dev` | Servidor de desarrollo |
| `npm run build` | Genera el sitio en `dist/` |
| `npm run preview` | Sirve `dist/` como lo verá GitHub Pages |
| `npm run material` | Reprocesa el material original (ver abajo) |
| `npm run images` | Optimiza imágenes sueltas de `material/` (alternativa simple) |

## Datos que faltan

Se rellenan en [`src/data/site.ts`](src/data/site.ts). Lo que está vacío no se muestra:

- **Contacto** (`contacto`): correo, LinkedIn, Behance, Instagram y WhatsApp. Mientras estén vacíos, la sección "Contacto" no aparece.
- **Foto**: el retrato sale de `Portada.jpg` (baja resolución). Con la foto original recortada se verá más nítida (`src/assets/brand/retrato.webp`).
- **Textos**: la biografía es la de la portada con acentos y concordancia corregidos; revísala.

## Material (imágenes)

Los originales (156 MB entre PSD, TIF y PDF) están en `PORTAFOLIO 2026 OK/` y **no se suben a Git**. El sitio usa versiones optimizadas (6.7 MB en total) que genera un script:

```bash
pip install -r scripts/requirements.txt   # una sola vez
npm run material                          # = python scripts/preparar-material.py
```

El script lee [`scripts/catalogo.py`](scripts/catalogo.py), donde cada pieza tiene su disciplina, marca, título y proyecto. Quita los marcos de presentación con borde negro, convierte PSD/TIF/GIF/PDF a WebP (los GIF siguen animados) y escribe `src/assets/work/` y `src/data/catalogo.json`.

**Para añadir una pieza**: copia el archivo a su carpeta de origen, añade una línea en `catalogo.py` y ejecuta `npm run material`. Si es un caso de estudio nuevo, añade también su entrada en [`src/data/proyectos.ts`](src/data/proyectos.ts); el `project` de cada pieza debe coincidir con el `slug` (el build falla si no).

**Imágenes generadas con IA**: para mockups realistas se usa la sesión de Codex CLI de quien ejecuta el script (la camisa de Tumedico se hizo así). Ver [`docs/imagenes-con-codex.md`](docs/imagenes-con-codex.md) y `scripts/generar-imagen-codex.ps1`.

Límites de GitHub: un archivo no puede pasar de 100 MB y el repo conviene mantenerlo bajo ~1 GB. Los vídeos pesados no van aquí: súbelos a YouTube/Vimeo y haz *embed*.

## Verlo desde otra computadora de la red local (opcional)

Si tienes un servidor estático en casa que sirva las carpetas de su `public/` (un "hub" de apps), el portafolio se puede publicar ahí como una app más, visible solo desde tu Wi‑Fi:

```powershell
npm run lan -- -Hub <ruta-al-hub>
```

Compila con base `/portafolio`, copia `dist/` a `<ruta-al-hub>\public\portafolio\` y escribe su `app.json`. Repite el comando cada vez que cambies el sitio. La dirección queda como `http://<IP-del-PC>:<puerto-del-hub>/portafolio/`. Es independiente de GitHub Pages.

## Publicar en GitHub Pages

1. Crea el repositorio en GitHub y sube el código a la rama `main`.
2. En el repo: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Cada push a `main` construye y despliega solo (`.github/workflows/deploy.yml`). El workflow calcula la URL y el *base path* reales (repo de proyecto, repo `usuario.github.io` o dominio propio), así que no hay nada que editar.

Para probar localmente cómo se comporta bajo un subdirectorio:

```powershell
$env:BASE_PATH = "/nombre-del-repo"; npm run build; npm run preview
```

**Credenciales**: nunca guardes contraseñas en el repositorio ni se las compartas a una herramienta. `.env` está en `.gitignore`, pero lo seguro es no dejar ahí claves. Para subir el código inicia sesión tú mismo con `gh auth login` (o con una llave SSH) en la cuenta que corresponda.

## Estructura

```
src/
  pages/          index, proyectos/[slug], 404
  components/     Hero, Marquee, Servicios, Divisor, Proyectos, Galeria, TrabajemosJuntos, Sobre, Contacto, Lightbox, Bloque…
  data/           site.ts (textos y contacto), proyectos.ts (casos), catalogo.json (generado)
  lib/work.ts     conecta el catálogo con las páginas y valida los ids en el build
  scripts/        motion.ts (GSAP + Lenis), galeria.ts (filtros con Flip), lightbox.ts
  assets/work/    imágenes optimizadas por disciplina (generadas)
  assets/brand/   retrato y patrón "V" extraídos de la portada y la barra
scripts/          preparar-material.py + catalogo.py
```

## Movimiento y accesibilidad

- Con `prefers-reduced-motion` no se carga Lenis ni ninguna animación: todo aparece ya en su estado final, y las ventanas de navegador se pueden desplazar a mano.
- Las animaciones usan `transform` y `opacity`. Lo continuo (manchas, stickers, marquee) es CSS puro.
- El visor usa `<dialog>` nativo: Escape cierra, las flechas navegan y el foco vuelve a la miniatura.

## Herramientas de diseño con Claude Code

Skills y herramientas del PDF `paginasproconanimaciones.pdf`, ya instaladas:

- **Emil Kowalski** (`.claude/skills/`): criterio de interfaz y motion (`emil-design-eng` es la principal).
- **`/taste <url>`**: extrae principios de diseño de una web pública, como referencia.
- **Playwright MCP** (`.mcp.json`): abre el sitio, prueba, captura y graba vídeo. Claude Code pide aprobar el servidor la primera vez (`/mcp`).
- **Figma MCP** (opcional): solo si hay diseños en Figma.

Los criterios de entrega están en [`CLAUDE.md`](CLAUDE.md).
