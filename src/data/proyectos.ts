/** Casos de estudio. Los textos describen solo lo que se ve en las piezas. */

export type Bloque =
  | { tipo: 'moviles'; titulo: string; texto?: string; ids: string[] }
  | { tipo: 'dispositivos'; titulo: string; texto?: string; ids: string[] }
  | { tipo: 'flujos'; titulo: string; texto?: string; ids: string[] }
  | { tipo: 'navegador'; titulo: string; texto?: string; ids: string[] }
  | { tipo: 'rejilla'; titulo: string; texto?: string; ids: string[] }
  | { tipo: 'tiras'; titulo: string; texto?: string; ids: string[] };

export type Portada =
  | { tipo: 'moviles'; ids: string[] }
  | { tipo: 'navegador'; id: string; sello?: string }
  | { tipo: 'collage'; ids: string[] };

export interface Proyecto {
  slug: string;
  marca: string;
  titulo: string;
  resumen: string;
  intro: string;
  color: string; // variable pastel de global.css
  disciplinas: string[];
  herramientas: string[];
  periodo?: string;
  portada: Portada;
  bloques: Bloque[];
}

export const proyectos: Proyecto[] = [
  {
    slug: 'hdi-seguros',
    marca: 'HDI Seguros',
    titulo: 'App móvil de seguros',
    resumen: 'Pantallas y flujos de una app para gestionar seguros, desde el acceso con huella hasta la autoinspección del vehículo.',
    intro:
      'Diseño de la experiencia y de las pantallas de la app de HDI Seguros: acceso con huella, menú de servicios, autoinspección fotográfica del vehículo, consulta de póliza, denuncio de siniestros y solicitud de grúa. Cada flujo quedó documentado en un tablero con notas de comportamiento por pantalla.',
    color: 'mint',
    disciplinas: ['uiux'],
    herramientas: ['Adobe XD', 'Illustrator', 'Photoshop'],
    portada: { tipo: 'moviles', ids: ['hdi-login-huella', 'hdi-menu', 'hdi-autoinspeccion'] },
    bloques: [
      {
        tipo: 'moviles',
        titulo: 'Pantallas',
        texto: 'Desliza para recorrer la app: del acceso a la confirmación de un trámite.',
        ids: [
          'hdi-login-huella',
          'hdi-menu',
          'hdi-automotriz',
          'hdi-patente',
          'hdi-autoinspeccion',
          'hdi-toma-foto',
          'hdi-grua',
          'hdi-grua-mapa',
          'hdi-consulta',
          'hdi-denuncio',
          'hdi-felicidades',
        ],
      },
      {
        tipo: 'dispositivos',
        titulo: 'Páginas responsivas dentro de la app',
        texto: 'Los seguros de automóvil y hogar cargan páginas web responsivas integradas a la app.',
        ids: ['hdi-responsive', 'hdi-web-automotriz', 'hdi-web-hogar', 'hdi-ios'],
      },
      {
        tipo: 'flujos',
        titulo: 'Tableros de flujo',
        texto: 'Nueve tableros que mapean cada recorrido pantalla por pantalla. Toca uno para verlo grande y hacer zoom.',
        ids: [
          'hdi-flujo-login',
          'hdi-flujo-automotriz',
          'hdi-flujo-soap',
          'hdi-flujo-hogar',
          'hdi-flujo-autoinspeccion',
          'hdi-flujo-consulta',
          'hdi-flujo-tarjeta',
          'hdi-flujo-siniestros',
          'hdi-flujo-gruas',
        ],
      },
    ],
  },
  {
    slug: 'datamars-livestock',
    marca: 'Datamars Livestock',
    titulo: 'Sitio web',
    resumen: 'Diseño de la página de inicio y de la Training Academy en amarillo, azul y fotografía de campo.',
    intro:
      'Páginas del sitio de Datamars Livestock: la portada con sus accesos por línea de producto y la Training Academy, con testimonios de usuarios. Capturas de febrero de 2021.',
    color: 'butter',
    disciplinas: ['web'],
    herramientas: [],
    periodo: '2021',
    portada: { tipo: 'navegador', id: 'datamars-inicio' },
    bloques: [
      {
        tipo: 'navegador',
        titulo: 'Las dos páginas',
        texto: 'Haz scroll: la página se desplaza sola dentro del navegador.',
        ids: ['datamars-inicio', 'datamars-academy'],
      },
    ],
  },
  {
    slug: 'centro-clinico-atenea',
    marca: 'Centro Clínico Atenea',
    titulo: 'Sitio web y logotipo',
    resumen: 'Maqueta de la página de inicio y logotipo «Bienestar para ti» de un centro clínico.',
    intro:
      'Maqueta del sitio web del Centro Clínico Atenea y su logotipo: un árbol-persona en verde y turquesa con la firma «Bienestar para ti».',
    color: 'aqua',
    disciplinas: ['web', 'identidad'],
    herramientas: ['Illustrator'],
    portada: { tipo: 'navegador', id: 'atenea-web', sello: 'atenea-logo' },
    bloques: [
      { tipo: 'rejilla', titulo: 'Logotipo', ids: ['atenea-logo'] },
      {
        tipo: 'navegador',
        titulo: 'Maqueta de la página de inicio',
        texto: 'Haz scroll para recorrerla.',
        ids: ['atenea-web'],
      },
    ],
  },
  {
    slug: 'rip-curl',
    marca: 'Rip Curl · Rusty · Volcom',
    titulo: 'Campañas digitales',
    resumen: 'Banners, emails animados y una landing para campañas de moda surf: Extended, New Arrivals, All Day y Sale.',
    intro:
      'Piezas digitales para campañas de moda surf entre 2021 y 2023: banners web y móviles, emails de venta con versiones animadas y una página de producto para la línea Anti Series.',
    color: 'peach',
    disciplinas: ['banners', 'email', 'web'],
    herramientas: ['Photoshop'],
    periodo: '2021 – 2023',
    portada: { tipo: 'collage', ids: ['rc-surfers-1', 'volcom-bags', 'rusty-summer'] },
    bloques: [
      {
        tipo: 'rejilla',
        titulo: 'Banners',
        texto: 'Rip Curl, Rusty, Volcom y Equinox.',
        ids: [
          'rc-extended-bf',
          'rc-extended-movil',
          'rc-surfers-1',
          'rc-surfers-2',
          'rusty-summer',
          'rusty-tshirts',
          'rusty-extended',
          'volcom-spring',
          'volcom-bags',
          'equinox-poleras',
        ],
      },
      {
        tipo: 'tiras',
        titulo: 'Emails',
        texto: 'Seis de ellos animados. Toca uno para verlo completo.',
        ids: [
          'rc-email-mujer',
          'rc-email-summer',
          'rc-email-sale',
          'rc-email-escolar',
          'rc-email-polerones',
          'rc-email-arrivals',
          'rc-email-antiseries',
          'rc-email-allday-1',
          'rc-email-allday-2',
        ],
      },
    ],
  },
  {
    slug: 'tumedico',
    marca: 'Tumedico.com',
    titulo: 'Marca digital de salud',
    resumen: 'Banners, publicaciones de redes, emailing, un pendón y papelería para una plataforma de salud en línea.',
    intro:
      'Piezas para Tumedico.com, «tu red de salud»: banners web, publicaciones para redes con efemérides, frases y consejos de salud, emailing, un pendón y papelería corporativa.',
    color: 'sky',
    disciplinas: ['banners', 'redes', 'email', 'impreso'],
    herramientas: ['Photoshop', 'Illustrator'],
    portada: { tipo: 'collage', ids: ['tm-red-videojuego', 'tm-red-sueno', 'tm-red-recetas', 'tm-red-ambiente'] },
    bloques: [
      {
        tipo: 'rejilla',
        titulo: 'Redes sociales',
        texto: 'Efemérides, frases, recetas e investigaciones.',
        ids: [
          'tm-red-videojuego',
          'tm-red-sueno',
          'tm-red-ambiente',
          'tm-red-salud-mental',
          'tm-red-vitiligo',
          'tm-red-alimentos',
          'tm-red-recetas',
          'tm-red-bailar',
          'tm-red-sexualidad',
          'tm-red-investigaciones',
          'tm-red-confort',
          'tm-red-miedo',
        ],
      },
      {
        tipo: 'rejilla',
        titulo: 'Banners',
        ids: ['tm-banner-espacio', 'tm-banner-opinion', 'tm-banner-home', 'tm-banner-registro', 'tm-banner-linkedin'],
      },
      { tipo: 'tiras', titulo: 'Emailing', ids: ['tm-email-citas', 'tm-email-usuarios'] },
      {
        tipo: 'dispositivos',
        titulo: 'Camisa corporativa',
        texto: 'El diseño plano original y un mockup realista generado con IA a partir de él.',
        ids: ['tm-camisa', 'tm-camisa-plano'],
      },
      { tipo: 'rejilla', titulo: 'Pendón y papelería', ids: ['tm-pendon', 'tm-carpeta'] },
    ],
  },
];

export const proyectoPorSlug = (slug: string) => proyectos.find((p) => p.slug === slug);
