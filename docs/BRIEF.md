# Brief del portafolio

Estado del encargo. Lo marcado como **Pendiente** necesita datos o decisiones de Vileidy.

## Encargo

- **Quién**: Vileidy Muñoz, diseñadora UI/UX (con trabajo de diseño gráfico, web y campañas digitales).
- **Dirección pedida**: portafolio divertido, animado y colorido en pasteles, tomando como referencia `Portada.jpg` y `Barra inicial.psd`.
- **Público y objetivo**: **Pendiente** (¿clientes, estudios, reclutadores? ¿qué acción principal: que escriban, que pidan presupuesto?).
- **Tono**: divertido, cercano y ordenado.

## Decidido

| Tema | Decisión |
|---|---|
| Paleta | Pasteles derivados del cian `#35b1cd` y el morado `#6f3e97` de la barra, más aqua, lavanda, rosa, durazno, mantequilla, menta y cielo. Texto en tinta `#231b3a`. |
| Tipografía | Anton (títulos, como el "PORTAFOLIO" de la portada), Fredoka (texto), Kristi (firma manuscrita). |
| Recursos de marca | Monograma "V" de la barra como banda decorativa; retrato de la portada con efecto duotono; comillas con barras de color. |
| Motion | Entrada del hero con letras que caen y stickers que aparecen con rebote; reveals al hacer scroll; tarjetas que se inclinan; galería con filtros animados; ventanas de navegador que se desplazan con el scroll. Todo se apaga con `prefers-reduced-motion`. |
| Estructura | Home con hero, marcas, "lo que hago", 5 casos destacados, galería filtrable, sobre mí y contacto; una página por caso. |

## Contenido

Las 112 piezas están ordenadas en 7 disciplinas (UI/UX, diseño web, banners, email marketing, redes sociales, logos y marca, impresos) en [`scripts/catalogo.py`](../scripts/catalogo.py).

| Caso | Piezas |
|---|---|
| HDI Seguros · app móvil | 11 pantallas, 4 páginas responsivas, 9 tableros de flujo |
| Datamars Livestock · web | 2 páginas |
| Centro Clínico Atenea · web y logo | maqueta + logotipo |
| Rip Curl · Rusty · Volcom | 10 banners, 9 emails (6 animados) |
| Tumedico.com | 12 redes, 5 banners, 2 emails, pendón y papelería |

## Pendiente

- [ ] Datos de contacto (correo, LinkedIn, Behance, Instagram, WhatsApp) en `src/data/site.ts`.
- [ ] Foto original recortada (la actual sale de la portada, de baja resolución).
- [ ] Revisar la biografía (es la de la portada con acentos y concordancia corregidos).
- [ ] Revisar títulos y marcas de las piezas sin logo visible (p. ej. "Moda infantil", "E-books") y la autoría de cada trabajo antes de publicar.
- [ ] Dominio final o nombre del repositorio.
- [ ] Imagen para compartir en redes (`og:image`).

## Accesibilidad mínima

Contraste AA, foco visible, teclado completo, `alt` en imágenes y respeto de `prefers-reduced-motion`.
