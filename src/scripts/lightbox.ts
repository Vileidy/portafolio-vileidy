import { gsap } from 'gsap';

const dlg = document.querySelector<HTMLDialogElement>('#lightbox');

if (dlg) {
  const q = <T extends HTMLElement>(s: string) => dlg.querySelector<T>(s)!;
  const zona = q<HTMLElement>('[data-lb-zona]');
  const img = q<HTMLImageElement>('[data-lb-img]');
  const marca = q('[data-lb-marca]');
  const titulo = q('[data-lb-titulo]');
  const desc = q('[data-lb-desc]');
  const meta = q('[data-lb-meta]');
  const proyecto = q<HTMLAnchorElement>('[data-lb-proyecto]');
  const contador = q('[data-lb-contador]');
  const prev = q<HTMLButtonElement>('[data-lb-prev]');
  const next = q<HTMLButtonElement>('[data-lb-next]');
  const zoom = q<HTMLButtonElement>('[data-lb-zoom]');
  const marco = q('.lb__marco');

  let grupo: HTMLElement[] = [];
  let i = 0;
  let disparador: HTMLElement | null = null;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const setZoom = (on: boolean) => {
    zona.dataset.zoom = on ? 'on' : 'off';
    zoom.setAttribute('aria-pressed', String(on));
    zoom.textContent = on ? 'Reducir' : 'Ampliar';
    if (!on) zona.scrollTo(0, 0);
  };

  const pintar = () => {
    const t = grupo[i];
    const d = t.dataset;
    setZoom(false);
    img.src = d.src ?? '';
    img.alt = d.alt ?? '';
    marca.textContent = d.marca ?? '';
    titulo.textContent = d.titulo ?? '';
    desc.textContent = d.desc ?? '';
    meta.textContent = [d.disciplina, d.herramientas].filter(Boolean).join(' · ');
    if (d.proyecto) {
      proyecto.href = d.proyecto;
      proyecto.textContent = `Ver el proyecto ${d.proyectoNombre ?? ''} →`.replace('  ', ' ');
      proyecto.hidden = false;
    } else {
      proyecto.hidden = true;
    }
    contador.textContent = `${i + 1} / ${grupo.length}`;
    prev.disabled = i === 0;
    next.disabled = i === grupo.length - 1;
    // precarga de las vecinas
    [grupo[i - 1], grupo[i + 1]].forEach((v) => {
      if (v?.dataset.src) new Image().src = v.dataset.src;
    });
    if (!reduce) gsap.fromTo(img, { opacity: 0, y: 14, scale: 0.97 }, { opacity: 1, y: 0, scale: 1, duration: 0.4, ease: 'power3.out' });
  };

  const abrir = (t: HTMLElement) => {
    const nombre = t.dataset.lbGroup ?? 'galeria';
    grupo = [...document.querySelectorAll<HTMLElement>(`[data-lb][data-lb-group="${nombre}"]`)].filter((el) => !el.closest('[hidden]'));
    i = Math.max(grupo.indexOf(t), 0);
    disparador = t;
    document.documentElement.classList.add('lb-open');
    window.__lenis?.stop();
    dlg.showModal();
    pintar();
    if (!reduce) gsap.fromTo(marco, { opacity: 0, y: 30, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: 'back.out(1.5)' });
  };

  const ir = (delta: number) => {
    const n = i + delta;
    if (n < 0 || n >= grupo.length) return;
    i = n;
    pintar();
  };

  document.addEventListener('click', (e) => {
    const t = (e.target as Element).closest<HTMLElement>('[data-lb]');
    if (t) abrir(t);
  });

  q('[data-lb-cerrar]').addEventListener('click', () => dlg.close());
  prev.addEventListener('click', () => ir(-1));
  next.addEventListener('click', () => ir(1));
  zoom.addEventListener('click', () => setZoom(zona.dataset.zoom !== 'on'));
  img.addEventListener('click', () => setZoom(zona.dataset.zoom !== 'on'));

  // Clic en la capa oscura (fuera del marco) cierra
  dlg.addEventListener('click', (e) => {
    if (e.target === dlg) dlg.close();
  });

  dlg.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') ir(-1);
    if (e.key === 'ArrowRight') ir(1);
  });

  dlg.addEventListener('close', () => {
    document.documentElement.classList.remove('lb-open');
    window.__lenis?.start();
    disparador?.focus({ preventScroll: true });
  });
}
