import catalogo from '../data/catalogo.json';
import { proyectoPorSlug } from '../data/proyectos';

/** Colores pastel por disciplina (variables definidas en global.css). */
export const colorDisciplina: Record<string, string> = {
  uiux: 'lav',
  web: 'aqua',
  banners: 'pink',
  email: 'peach',
  redes: 'butter',
  identidad: 'mint',
  impreso: 'sky',
};

/** Programas que figuran en los pies de las láminas originales de cada disciplina. */
export const herramientasDisciplina: Record<string, string[]> = {
  uiux: ['Adobe XD', 'Illustrator'],
  banners: ['Photoshop'],
  email: ['Photoshop'],
  redes: ['Photoshop'],
  identidad: ['Illustrator'],
  impreso: ['Illustrator', 'Photoshop'],
};

export interface Pieza {
  id: string;
  disc: string;
  brand: string;
  title: string;
  alt: string;
  desc?: string | null;
  project: string | null;
  gallery: boolean;
  kind: string;
  file: string;
  w: number;
  h: number;
  frames: number;
  src: string;
}

const archivos = import.meta.glob<{ default: ImageMetadata }>('/src/assets/work/**/*.{webp,svg}', { eager: true });

export const disciplinas: { id: string; label: string }[] = catalogo.disciplinas;

export const piezas: Pieza[] = catalogo.items.map((it) => {
  const mod = archivos[`/src/assets/work/${it.file}`];
  if (!mod) throw new Error(`Falta el archivo ${it.file}; ejecuta python scripts/preparar-material.py`);
  return { ...(it as Omit<Pieza, 'src'>), src: mod.default.src };
});

// Cada pieza que dice pertenecer a un proyecto debe apuntar a una página que exista
for (const p of piezas) {
  if (p.project && !proyectoPorSlug(p.project)) {
    throw new Error(`La pieza "${p.id}" apunta al proyecto "${p.project}", que no existe en src/data/proyectos.ts`);
  }
}

const porId = new Map(piezas.map((p) => [p.id, p]));

/** Devuelve una pieza por id; si no existe rompe el build (mejor que una imagen rota en producción). */
export function pieza(id: string): Pieza {
  const p = porId.get(id);
  if (!p) throw new Error(`Pieza desconocida: ${id}`);
  return p;
}

export const enGaleria = piezas.filter((p) => p.gallery);

export const nombreDisciplina = (id: string) => disciplinas.find((d) => d.id === id)?.label ?? id;

/** Forma de la celda en la cuadrícula según la proporción de la pieza. */
export function formaCelda(p: Pieza): 'wide' | 'tall' | 'square' {
  const r = p.w / p.h;
  if (r >= 1.55) return 'wide';
  if (r < 0.8) return 'tall';
  return 'square';
}

export const marcasUnicas = new Set(piezas.map((p) => p.brand));

/**
 * Atributos data-* con los que un botón abre la pieza en el visor (lightbox.ts).
 * `conProyecto: false` en las páginas de caso, donde el enlace al proyecto sobra.
 */
export function atributosVisor(p: Pieza, grupo: string, conProyecto = true) {
  const proyecto = conProyecto && p.project ? proyectoPorSlug(p.project) : undefined;
  return {
    'data-lb': '',
    'data-lb-group': grupo,
    'data-src': p.src,
    'data-alt': p.alt,
    'data-marca': p.brand,
    'data-titulo': p.title,
    'data-desc': p.desc ?? '',
    'data-disciplina': nombreDisciplina(p.disc),
    'data-herramientas': (herramientasDisciplina[p.disc] ?? []).join(' · '),
    'data-proyecto': proyecto ? `${import.meta.env.BASE_URL}proyectos/${proyecto.slug}/` : '',
    'data-proyecto-nombre': proyecto?.marca ?? '',
  };
}
