import { gsap } from 'gsap';
import { Flip } from 'gsap/Flip';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(Flip, ScrollTrigger);

const raiz = document.querySelector<HTMLElement>('[data-galeria]');

if (raiz) {
  const tiles = [...raiz.querySelectorAll<HTMLElement>('.tile')];
  const botones = [...raiz.querySelectorAll<HTMLButtonElement>('[data-filtro]')];
  const total = raiz.querySelector<HTMLElement>('[data-galeria-total]');
  const hayMovimiento = document.documentElement.dataset.motion === 'on';
  let actual = 'todo';

  const filtrar = (id: string, { animar = true } = {}) => {
    if (id === actual && animar) return;
    actual = id;
    const estado = hayMovimiento && animar ? Flip.getState(tiles) : null;

    let visibles = 0;
    tiles.forEach((t) => {
      const mostrar = id === 'todo' || t.dataset.disc === id;
      t.hidden = !mostrar;
      if (mostrar) visibles++;
    });
    botones.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.filtro === id)));
    if (total) total.textContent = String(visibles);

    if (estado) {
      Flip.from(estado, {
        duration: 0.6,
        ease: 'power3.inOut',
        absolute: true,
        scale: true,
        stagger: 0.012,
        onEnter: (els) => gsap.fromTo(els, { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.5, ease: 'back.out(1.6)' }),
        onLeave: (els) => gsap.to(els, { opacity: 0, scale: 0.5, duration: 0.3 }),
        onComplete: () => ScrollTrigger.refresh(),
      });
    }
  };

  botones.forEach((b) => b.addEventListener('click', () => filtrar(b.dataset.filtro ?? 'todo')));

  // Las tarjetas de "Lo que hago" activan un filtro y bajan a la galería
  document.querySelectorAll<HTMLElement>('[data-filtrar]').forEach((el) => {
    el.addEventListener('click', () => {
      filtrar(el.dataset.filtrar ?? 'todo');
      const destino = document.getElementById('trabajo');
      if (!destino) return;
      if (window.__lenis) window.__lenis.scrollTo(destino, { offset: -72 });
      else destino.scrollIntoView({ behavior: 'smooth' });
    });
  });
}
