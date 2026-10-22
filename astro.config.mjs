import { defineConfig } from 'astro/config';

// SITE_URL y BASE_PATH los inyecta el workflow de GitHub Pages (.github/workflows/deploy.yml)
// a partir de la configuración real del repo, así el mismo código sirve para
// usuario.github.io/<repo>/, usuario.github.io o un dominio propio.
// En local no hace falta definirlas.
//
// configure-pages entrega base_path sin barra final ("/repo" o ""), así que se normaliza:
// import.meta.env.BASE_URL queda siempre con barra inicial y final ("/" o "/repo/").
const base = `/${(process.env.BASE_PATH ?? '').replace(/^\/+|\/+$/g, '')}/`.replace('//', '/');

export default defineConfig({
  site: process.env.SITE_URL || 'http://localhost:4321',
  base,
});
