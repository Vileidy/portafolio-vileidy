/** Datos generales del sitio. Lo que está vacío no se muestra en la web. */
export const site = {
  nombre: 'Vileidy Muñoz',
  rol: 'Diseñadora UI / UX',
  titulo: 'Vileidy Muñoz · Diseñadora UI/UX',
  descripcion:
    'Portafolio de Vileidy Muñoz, diseñadora UI/UX: apps móviles, diseño web, campañas digitales, identidad de marca y piezas impresas.',

  // Texto de la portada original, con los acentos y la concordancia corregidos.
  saludo:
    'Me caracterizo por ser estratégica y orientada a resultados, con sólida capacidad de organización y alto nivel de atención al detalle.',
  bio: [
    'Me caracterizo por ser estratégica y orientada a resultados, con sólida capacidad de organización y alto nivel de atención al detalle.',
    'Tengo amplia experiencia colaborando con equipos en entornos dinámicos y remotos, generando satisfacción del usuario y alineando cada diseño con los objetivos del negocio.',
  ],
  rasgos: ['Estratégica', 'Orientada a resultados', 'Atención al detalle'],

  // Programas que figuran en los pies de las láminas originales.
  herramientas: ['Adobe XD', 'Illustrator', 'Photoshop'],

  // Marcas con las que se ha trabajado (todas aparecen en las piezas del catálogo).
  marcas: [
    'Rip Curl',
    'Volcom',
    'Rusty',
    'HDI Seguros',
    'Zapacos',
    'Tumedico.com',
    'Datamars Livestock',
    'Centro Clínico Atenea',
    'Koslan',
    'Smagic',
    'Moxi Du',
    'Adóptame',
    'Guahibos Gourmet',
    'Zambia Soluciones',
    'Hacienda Chacabuco',
    'Monstruo Yo',
  ],

  // Completar con los datos reales. Cada enlace aparece solo si tiene valor.
  contacto: {
    email: '',
    linkedin: '', // URL completa
    behance: '', // URL completa
    instagram: '', // URL completa
    whatsapp: '', // solo dígitos con prefijo país, p. ej. 584121234567
  },
};

export const hayContacto = Object.values(site.contacto).some(Boolean);
