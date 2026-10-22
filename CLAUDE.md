# CLAUDE.md

Portafolio de **Vileidy Muñoz** (diseñadora UI/UX): divertido, animado y en pasteles. Astro + GSAP + Lenis, estático, publicado en GitHub Pages desde Git. Idioma del sitio: español.

## Comandos

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # genera dist/
npm run preview    # sirve dist/ tal como lo verá GitHub Pages
npm run material   # python scripts/preparar-material.py: regenera src/assets/work y src/data/catalogo.json
npm run lan -- -Hub <ruta-al-hub>   # (opcional) publica en un hub de apps de la red local con base /portafolio
```

Node >= 22.23.4 (`.nvmrc` fija 24). Cada push a `main` ejecuta `.github/workflows/deploy.yml`.

## Dirección visual (ya decidida)

- Referencias: `PORTAFOLIO 2026 OK/Portada.jpg` (título gigante con tracking, firma manuscrita, comillas con barras) y `Barra inicial.psd` (monograma "V" en cian `#35b1cd` y morado `#6f3e97`).
- Tokens en `src/styles/global.css`: tinta `--ink` casi negra, fondo `--cream` y pasteles `--aqua --lav --pink --peach --butter --mint --sky`. Contornos de tinta de 2 px y sombras sólidas desplazadas (estilo sticker). No introduzcas colores fuera de esta paleta.
- Tipografías (autoalojadas con `@fontsource`): `Anton` para títulos en mayúsculas, `Fredoka Variable` para texto, `Kristi` para la firma.
- `src/assets/brand/`: `retrato.webp` (se usa con `mix-blend-mode: multiply` sobre un fondo pastel) y `patron-v.svg` (el patrón original recoloreado). Ambos los genera `preparar-material.py` a partir de la portada y del PSD.

## Estructura

- `src/data/site.ts` textos y **contacto** (vacío a propósito: se rellena con datos reales; lo vacío no se muestra).
- `src/data/proyectos.ts` casos de estudio (`slug`, textos, portada y bloques).
- `src/data/catalogo.json` **generado**; no se edita a mano. Su fuente es `scripts/catalogo.py`.
- `src/lib/work.ts` une catálogo e imágenes y **rompe el build** si una pieza apunta a un proyecto o a un id que no existe.
- `src/components/` secciones de la home, `Bloque.astro` (bloques de caso), `Doodle.astro` (stickers SVG).
- `src/scripts/` `motion.ts` (Lenis, hero, reveals, tilt), `galeria.ts` (filtros con Flip), `lightbox.ts`.

## Material y Git

- `PORTAFOLIO 2026 OK/` (156 MB: PSD, TIF, PDF) está en `.gitignore`. Nunca lo añadas. El sitio solo usa `src/assets/work/` (6.7 MB en WebP).
- Para añadir una pieza: archivo en su carpeta de origen, una línea en `scripts/catalogo.py`, `npm run material`. El campo `project` debe ser el `slug` de un caso de `proyectos.ts`.
- El sitio puede servirse bajo `/<repo>/`. Usa `import.meta.env.BASE_URL` (siempre termina en `/`) para enlaces y assets estáticos; nunca `href="/ruta"`. Las imágenes del catálogo ya resuelven su ruta con la base.
- No commitear `.env`, claves ni tokens. **No pidas ni uses contraseñas de cuentas para hacer push**: la sesión de GitHub la inicia el usuario (`gh auth login`). No hacer commit ni push sin que lo pidan.
- Imágenes generadas con IA: solo con Codex CLI de la persona dueña (ya autorizado para mockups de sus propias piezas), siguiendo `docs/imagenes-con-codex.md`. Nunca fotos de personas, revisa textos y colores a ojo y márcalas como "generado con IA" en su `desc`.
- No subas vídeos pesados ni nada > 10 MB. Un archivo > 100 MB rompe el push.

## Ritmo vertical

- Sin huecos vacíos entre secciones: `.section` usa `padding-block` compacto, `Divisor.astro` (franja con el patrón "V") separa secciones y `TrabajemosJuntos.astro` (cintas cruzadas) llena el hueco entre la galería y "Sobre mí".
- En los bloques de caso, los grids se adaptan al número de piezas (`--resto`, `--c2/--c3/--c4`, `data-pocas`) para no dejar medias filas vacías. Al estilar por estado usa atributos `data-*`: Astro poda las clases que no ve estáticamente (p. ej. con `class:list`).
- El título del hero va por encima del retrato y nunca lo cubre.

## Motion

- `html[data-motion]` lo decide un script inline en `Base.astro` antes del primer pintado: `on` solo si no hay `prefers-reduced-motion`. Los estados iniciales ocultos (`.reveal`, letras y stickers del hero) existen **solo bajo `[data-motion='on']`**; sin JS o con movimiento reducido todo se ve en su estado final.
- Si `motion.ts` falla, vuelve a `data-motion="off"` (el contenido nunca queda invisible).
- Un elemento no puede tener a la vez una animación CSS sobre `transform` y un tween de GSAP: usa un contenedor para GSAP (entrada, parallax) y un hijo para el keyframe (`.sticker` y `.sticker__in` en `Hero.astro`). Tampoco uses las propiedades CSS `rotate`/`scale` en elementos que anime GSAP.
- Solo `transform` y `opacity`. Lo continuo (manchas, marquee, stickers) es CSS puro.
- Los componentes con `data-lenis-prevent` (el visor) no deben quedar bajo el scroll suave.

## Verificación

Con `npm run dev` (o `npm run preview` con `BASE_PATH=/nombre-del-repo`), usa Playwright MCP en 375, 768 y 1280+: consola sin errores, ninguna imagen rota, sin desborde horizontal, visor con teclado (Enter, flechas, Escape) y `prefers-reduced-motion: reduce`. Guarda capturas en `evidence/` (ignorada por Git) y di qué probaste y qué quedó pendiente. No afirmes que algo funciona si no lo comprobaste.

## Criterio de entrega

- **Contenido**: textos reales; sin lorem ipsum ni datos inventados (contacto, cifras, fechas). Todo lo que se afirma sale de las piezas.
- **Responsive**: 375, 768 y 1280+; sin desbordamiento horizontal.
- **Interacción**: menú, filtros, visor, carriles y formularios si los hubiera.
- **Accesibilidad**: foco visible, teclado, contraste, `alt` en imágenes, movimiento reducido.
- **Técnica**: consola limpia, `npm run build` limpio y comprobado también con `BASE_PATH`, imágenes optimizadas.

## Skills instaladas (`.claude/skills/`)

Emil Kowalski (`emil-design-eng`, `animate`, `review-animations`, `improve-animations`, `find-animation-opportunities`, `animation-performance`, `animation-vocabulary`, `apple-design`, `mobile-native`, `break-ui`, `prototype`, `pick-ui-library`) y `/taste <url>` (salidas en `docs/referencias/`). Aportan criterio, no identidad de marca; no copies textos, logos, imágenes ni código de terceros.
