import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import Lenis from 'lenis';
import 'lenis/dist/lenis.css';

gsap.registerPlugin(ScrollTrigger);

const html = document.documentElement;
const hayMovimiento = html.dataset.motion === 'on';
const puntero = matchMedia('(hover: hover) and (pointer: fine)').matches;

declare global {
  interface Window {
    __lenis?: Lenis;
  }
}

/** Entrada del hero: letras que caen, retrato que aparece con rebote, stickers que "pop". */
function entradaHero() {
  if (!document.querySelector('.hero')) return;
  const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });
  tl.to('.letra', { opacity: 1, y: 0, rotate: 0, duration: 1, stagger: 0.07, ease: 'back.out(1.8)' }, 0.1)
    .fromTo(
      '[data-hero="retrato"]',
      { opacity: 0, scale: 0.84, rotate: -5, transformOrigin: '50% 100%' },
      { opacity: 1, scale: 1, rotate: 0, duration: 1.1, ease: 'back.out(1.4)' },
      0.45,
    )
    .fromTo('[data-hero="quien"]', { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.9 }, 0.8)
    .fromTo('[data-hero="saludo"]', { opacity: 0, x: 40 }, { opacity: 1, x: 0, duration: 0.9 }, 0.9)
    .to('[data-hero="sticker"]', { opacity: 1, scale: 1, duration: 0.9, stagger: 0.09, ease: 'elastic.out(1, 0.5)' }, 1.0);
}

/** Cada letra del título se menea al pasar el cursor. */
function letrasJuguetonas() {
  if (!puntero) return;
  document.querySelectorAll<HTMLElement>('.letra').forEach((letra) => {
    letra.addEventListener('pointerenter', () => {
      gsap.to(letra, { y: -14, rotate: gsap.utils.random(-9, 9), scale: 1.07, duration: 0.35, ease: 'back.out(3)', overwrite: 'auto' });
    });
    letra.addEventListener('pointerleave', () => {
      gsap.to(letra, { y: 0, rotate: 0, scale: 1, duration: 0.6, ease: 'elastic.out(1, 0.45)', overwrite: 'auto' });
    });
  });
}

/** Los stickers siguen un poco al cursor, cada uno a su profundidad. */
function paralajeStickers() {
  if (!puntero) return;
  const stickers = [...document.querySelectorAll<HTMLElement>('[data-prof]')];
  if (!stickers.length) return;
  const mover = stickers.map((el) => ({
    x: gsap.quickTo(el, 'x', { duration: 0.8, ease: 'power3' }),
    y: gsap.quickTo(el, 'y', { duration: 0.8, ease: 'power3' }),
    prof: Number(el.dataset.prof),
  }));
  window.addEventListener('pointermove', (e) => {
    const nx = e.clientX / window.innerWidth - 0.5;
    const ny = e.clientY / window.innerHeight - 0.5;
    mover.forEach((m) => {
      m.x(nx * m.prof);
      m.y(ny * m.prof);
    });
  });
}

/** Aparición al hacer scroll. */
function revelar() {
  ScrollTrigger.batch('.reveal', {
    start: 'top 90%',
    once: true,
    onEnter: (els) =>
      gsap.to(els, { opacity: 1, y: 0, rotate: 0, duration: 0.85, stagger: 0.1, ease: 'power3.out', overwrite: true }),
  });
}

/** Contadores que suben desde cero. */
function contadores() {
  document.querySelectorAll<HTMLElement>('[data-cuenta]').forEach((el) => {
    const meta = Number(el.dataset.cuenta);
    el.textContent = '0';
    ScrollTrigger.create({
      trigger: el,
      start: 'top 92%',
      once: true,
      onEnter: () => {
        const o = { v: 0 };
        gsap.to(o, { v: meta, duration: 1.5, ease: 'power2.out', onUpdate: () => (el.textContent = String(Math.round(o.v))) });
      },
    });
  });
}

/** Las tarjetas se inclinan hacia el cursor. */
function inclinar() {
  if (!puntero) return;
  document.querySelectorAll<HTMLElement>('[data-tilt]').forEach((el) => {
    const rx = gsap.quickTo(el, 'rotationX', { duration: 0.5, ease: 'power3' });
    const ry = gsap.quickTo(el, 'rotationY', { duration: 0.5, ease: 'power3' });
    gsap.set(el, { transformPerspective: 1000 });
    el.addEventListener('pointermove', (e) => {
      const r = el.getBoundingClientRect();
      ry(((e.clientX - r.left) / r.width - 0.5) * 7);
      rx(-((e.clientY - r.top) / r.height - 0.5) * 7);
    });
    el.addEventListener('pointerleave', () => {
      rx(0);
      ry(0);
    });
  });
}

/** La página de una captura larga se desplaza sola dentro de su ventana de navegador. */
function navegadores() {
  document.querySelectorAll<HTMLElement>('[data-navegador]').forEach((marco) => {
    const pantalla = marco.querySelector<HTMLElement>('[data-pantalla]');
    const img = pantalla?.querySelector('img');
    if (!pantalla || !img) return;
    gsap.to(img, {
      y: () => -Math.max(img.offsetHeight - pantalla.clientHeight, 0),
      ease: 'none',
      scrollTrigger: {
        trigger: marco,
        start: 'top 80%',
        end: 'bottom 30%',
        scrub: 0.6,
        invalidateOnRefresh: true,
      },
    });
  });
}

/** Carriles horizontales: se pueden arrastrar con el ratón. */
function carriles() {
  document.querySelectorAll<HTMLElement>('[data-carril]').forEach((carril) => {
    let activo = false;
    let inicioX = 0;
    let inicioScroll = 0;
    let movido = false;
    carril.addEventListener('pointerdown', (e) => {
      if (e.pointerType !== 'mouse') return;
      activo = true;
      movido = false;
      inicioX = e.clientX;
      inicioScroll = carril.scrollLeft;
    });
    window.addEventListener('pointermove', (e) => {
      if (!activo) return;
      const dx = e.clientX - inicioX;
      if (Math.abs(dx) > 4) movido = true;
      carril.scrollLeft = inicioScroll - dx;
    });
    window.addEventListener('pointerup', () => {
      activo = false;
    });
    // Un arrastre no debe abrir el visor
    carril.addEventListener(
      'click',
      (e) => {
        if (movido) {
          e.stopPropagation();
          e.preventDefault();
          movido = false;
        }
      },
      true,
    );
  });
}

/** Confeti de colores pastel al tocar un sticker. */
function confeti() {
  if (!hayMovimiento) return;
  const colores = ['#a9e4f0', '#cbb5f0', '#ffc4dd', '#ffd3b0', '#fff0a6', '#bdebcb'];
  document.addEventListener('click', (e) => {
    const objetivo = (e.target as Element).closest('.sticker--carita, .nav__logo');
    if (!objetivo) return;
    const { clientX: x, clientY: y } = e;
    for (let i = 0; i < 18; i++) {
      const p = document.createElement('span');
      Object.assign(p.style, {
        position: 'fixed',
        left: `${x}px`,
        top: `${y}px`,
        width: `${gsap.utils.random(8, 14)}px`,
        height: `${gsap.utils.random(8, 14)}px`,
        borderRadius: Math.random() > 0.5 ? '50%' : '3px',
        background: gsap.utils.random(colores),
        border: '2px solid #231b3a',
        pointerEvents: 'none',
        zIndex: '200',
      });
      document.body.append(p);
      gsap.to(p, {
        x: gsap.utils.random(-140, 140),
        y: gsap.utils.random(-170, 90),
        rotate: gsap.utils.random(-300, 300),
        opacity: 0,
        duration: gsap.utils.random(0.8, 1.4),
        ease: 'power3.out',
        onComplete: () => p.remove(),
      });
    }
  });
}

function iniciar() {
  if (!hayMovimiento) return;

  const lenis = new Lenis({ lerp: 0.1, anchors: { offset: -72 } });
  window.__lenis = lenis;
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((t) => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);

  entradaHero();
  letrasJuguetonas();
  paralajeStickers();
  revelar();
  contadores();
  inclinar();
  navegadores();
  confeti();
}

carriles();
try {
  iniciar();
} catch (error) {
  // Si algo falla, el contenido debe quedar visible
  console.error(error);
  html.dataset.motion = 'off';
}
