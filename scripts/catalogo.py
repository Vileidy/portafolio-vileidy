"""Catálogo curado del portafolio de Vileidy Muñoz.

Cada pieza apunta a un archivo de "PORTAFOLIO 2026 OK/Imag Categorias" y dice dónde va:

  id        identificador único; es el nombre del .webp generado
  src       "carpeta/archivo". La carpeta usa un alias corto (ver CARPETAS en
            preparar-material.py); el archivo se compara sin mayúsculas ni símbolos,
            así que los espacios o caracteres raros del original no importan.
            "ia/..." son imágenes generadas con IA (carpeta generadas-ia junto a los originales).
  disc      disciplina (filtro de la galería): uiux | web | banners | email | redes | identidad | impreso
  brand     marca o cliente que se ve en la pieza
  title     título corto
  project   caso de estudio al que pertenece (hdi-seguros, datamars-livestock, centro-clinico-atenea, rip-curl, tumedico) o None
  gallery   False = solo aparece dentro de su caso de estudio, no en la galería general
  kind      cómo se muestra en el caso: screen (móvil) | flow (tablero de flujo) | web (captura larga) | plain
  w         ancho máximo en px del archivo final
  page      página (1..n) cuando la fuente es un PDF
  crop      (x0, y0, x1, y1) para recortar a mano cuando el original trae fondo sobrante
  desc      texto descriptivo opcional (se muestra en el visor)
  pie       fracción del ancho que ocupa el texto del pie de la lámina (0.62 por defecto);
            súbela si el pie es largo y se cuela en el recorte

Para añadir material nuevo: copia el archivo a la carpeta de origen, añade una línea aquí y
ejecuta `python scripts/preparar-material.py`.
"""

DISCIPLINAS = [
    ("uiux", "UI / UX"),
    ("web", "Diseño web"),
    ("banners", "Banners"),
    ("email", "Email marketing"),
    ("redes", "Redes sociales"),
    ("identidad", "Logos y marca"),
    ("impreso", "Impresos"),
]


def it(id, src, disc, brand, title, project=None, gallery=True, kind="plain", w=1400, page=None, crop=None, pie=0.62, desc=None, alt=None):
    return dict(
        id=id, src=src, disc=disc, brand=brand, title=title, project=project,
        gallery=gallery, kind=kind, w=w, page=page, crop=crop, pie=pie, desc=desc,
        alt=alt or f"{title} — {brand}",
    )


ITEMS = [
    # ───────────────────────── HDI Seguros · app móvil (UI/UX) ─────────────────────────
    it("hdi-flujo-login", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de login y acceso con huella",
       project="hdi-seguros", kind="flow", w=2400, page=1, alt="Tablero de flujo del login de la app de HDI Seguros: splash, registro, Touch ID y recuperación de contraseña"),
    it("hdi-flujo-automotriz", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de seguro automotriz",
       project="hdi-seguros", kind="flow", w=2400, page=2, gallery=False, alt="Tablero de flujo del seguro automotriz de HDI Seguros"),
    it("hdi-flujo-soap", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de SOAP",
       project="hdi-seguros", kind="flow", w=2400, page=3, gallery=False, alt="Tablero de flujo del SOAP en la app de HDI Seguros"),
    it("hdi-flujo-hogar", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de seguro hogar",
       project="hdi-seguros", kind="flow", w=2400, page=4, gallery=False, alt="Tablero de flujo del seguro de hogar de HDI Seguros"),
    it("hdi-flujo-autoinspeccion", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de autoinspección fotográfica",
       project="hdi-seguros", kind="flow", w=2400, page=5, alt="Tablero de flujo de la autoinspección fotográfica del vehículo, con nueve tomas guiadas"),
    it("hdi-flujo-consulta", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de consulta de póliza",
       project="hdi-seguros", kind="flow", w=2400, page=6, gallery=False, alt="Tablero de flujo de consulta de póliza de HDI Seguros"),
    it("hdi-flujo-tarjeta", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de tarjeta de asistencia",
       project="hdi-seguros", kind="flow", w=2400, page=7, gallery=False, alt="Tablero de flujo de la tarjeta de asistencia de HDI Seguros"),
    it("hdi-flujo-siniestros", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de siniestros",
       project="hdi-seguros", kind="flow", w=2400, page=8, gallery=False, alt="Tablero de flujo de denuncio de siniestros de HDI Seguros"),
    it("hdi-flujo-gruas", "mobile/Aplicación Mobile HDI.pdf", "uiux", "HDI Seguros", "Flujo de asistencia de grúas",
       project="hdi-seguros", kind="flow", w=2400, page=9, gallery=False, alt="Tablero de flujo de asistencia de grúas de HDI Seguros"),

    it("hdi-menu", "mobile/inscritos.png", "uiux", "HDI Seguros", "Menú principal de servicios",
       project="hdi-seguros", kind="screen", w=720, alt="Pantalla de menú principal de la app HDI Seguros con ocho accesos a servicios"),
    it("hdi-login-huella", "mobile/7.jpg", "uiux", "HDI Seguros", "Inicio de sesión con huella",
       project="hdi-seguros", kind="screen", w=720, alt="Pantalla de inicio de sesión con huella dactilar de la app HDI Seguros"),
    it("hdi-automotriz", "mobile/3.1.png", "uiux", "HDI Seguros", "Seguro automotriz",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla de datos del seguro automotriz"),
    it("hdi-toma-foto", "mobile/29.png", "uiux", "HDI Seguros", "Toma fotográfica guiada",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla de toma fotográfica guiada del número VIN"),
    it("hdi-patente", "mobile/identificar.png", "uiux", "HDI Seguros", "Identificar vehículo",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla para ingresar la patente del vehículo"),
    it("hdi-autoinspeccion", "mobile/auto.png", "uiux", "HDI Seguros", "Autoinspección fotográfica",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla de inicio de la autoinspección fotográfica"),
    it("hdi-grua", "mobile/2.png", "uiux", "HDI Seguros", "Solicita tu grúa",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla para solicitar una grúa con mapa"),
    it("hdi-grua-mapa", "mobile/6.png", "uiux", "HDI Seguros", "Ubicación de la grúa",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla con la ruta y la ubicación de la grúa"),
    it("hdi-consulta", "mobile/Consulta.png", "uiux", "HDI Seguros", "Consulta tu póliza",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla de consulta de póliza"),
    it("hdi-denuncio", "mobile/3.png", "uiux", "HDI Seguros", "Denuncio de siniestro",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla de denuncio con selección de póliza asociada"),
    it("hdi-felicidades", "mobile/felicidades.png", "uiux", "HDI Seguros", "Confirmación de documentos",
       project="hdi-seguros", kind="screen", w=720, gallery=False, alt="Pantalla de confirmación: documentos cargados correctamente"),
    it("hdi-responsive", "mobile/fondo.jpg", "uiux", "HDI Seguros", "Páginas responsivas integradas a la app",
       project="hdi-seguros", alt="Las páginas web de HDI Seguros adaptadas a computador, tableta y móvil"),
    it("hdi-ios", "mobile/1.jpg", "uiux", "HDI Seguros", "Ícono de la app",
       project="hdi-seguros", gallery=False, alt="Ícono de la app HDI Seguros en la pantalla de inicio de un iPhone"),
    it("hdi-web-hogar", "mobile/hogar.jpg", "uiux", "HDI Seguros", "Seguro hogar",
       project="hdi-seguros", gallery=False, alt="Página responsiva del seguro de hogar"),
    it("hdi-web-automotriz", "mobile/automotriz.jpg", "uiux", "HDI Seguros", "Seguro automotriz",
       project="hdi-seguros", gallery=False, alt="Página responsiva del seguro automotriz"),

    # ───────────────────────── Diseño web ─────────────────────────
    it("datamars-inicio", "web/screencapture-livestock-datamars-es-2021-02-24-16_29_12 (1).png", "web", "Datamars Livestock", "Página de inicio",
       project="datamars-livestock", kind="web", w=1600, alt="Página de inicio de Datamars Livestock"),
    it("datamars-academy", "web/screencapture-livestock-datamars-es-training-academy-2021-02-24-16_38_20.png", "web", "Datamars Livestock", "Training Academy",
       project="datamars-livestock", kind="web", w=1600, alt="Página Training Academy de Datamars Livestock"),
    it("atenea-web", "web/centro-clinico-ATENEAMaqueta1.jpg", "web", "Centro Clínico Atenea", "Maqueta del sitio web",
       project="centro-clinico-atenea", kind="web", w=1600, alt="Maqueta de la página de inicio del Centro Clínico Atenea"),
    it("koslan-web", "web/pagina web.png", "web", "Koslan", "Sitio e-commerce", kind="web", w=1400, crop=(574, 66, 1051, 620),
       alt="Diseño de tienda en línea de Koslan, empresa de bombas y soluciones de agua"),

    # ───────────────────────── Rip Curl · Rusty · Volcom (campañas digitales) ─────────────────────────
    it("rc-extended-bf", "banners/Extended BF_Ripcurl_Bloque 03.jpg", "banners", "Rip Curl", "Extended Black Friday: hasta 30% off", project="rip-curl"),
    it("rc-extended-movil", "redes/Extended BF Mobile_Ripcurl_Banner General.jpg", "banners", "Rip Curl", "Extended Black Friday, versión móvil", project="rip-curl"),
    it("rc-surfers-1", "banners/Surf_producto_Ripcurl.jpg", "banners", "Rip Curl", "Original Surfers Products", project="rip-curl"),
    it("rc-surfers-2", "banners/Wetsuit generico_Ripcurl.jpg", "banners", "Rip Curl", "Original Surfers Products: wetsuits", project="rip-curl"),
    it("rusty-summer", "banners/General.jpg", "banners", "Rusty", "New Arrivals Summer", project="rip-curl"),
    it("rusty-tshirts", "banners/Polera.jpg", "banners", "Rusty", "New Arrivals T-Shirts", project="rip-curl"),
    it("rusty-extended", "banners/Polera Extended.jpg", "banners", "Rusty", "Extended: T-Shirts hasta 40% off", project="rip-curl"),
    it("volcom-spring", "banners/_banner.newarrivals.jpeg", "banners", "Volcom", "New Arrivals Spring 2021", project="rip-curl"),
    it("volcom-bags", "banners/banner-BAGS_Volcom.jpg", "banners", "Volcom", "Bags Collection: 20% off", project="rip-curl"),
    it("equinox-poleras", "banners/Banner POLERA MUJER.jpg", "banners", "Equinox", "New Arrivals Poleras", project="rip-curl"),

    it("rc-email-mujer", "email/1-20230309 Mujer-NewArrivals.jpg", "email", "Rip Curl", "Mujer: New Arrivals", project="rip-curl", w=900),
    it("rc-email-summer", "email/20230104-Mujer.gif", "email", "Rip Curl", "Summer Sale animado", project="rip-curl", w=900),
    it("rc-email-sale", "email/20230105-Sale_rip.psd", "email", "Rip Curl", "Sale: hasta 50% off", project="rip-curl", w=900),
    it("rc-email-escolar", "email/20230118-Escolar.gif", "email", "Rip Curl", "Vuelta a clases animado", project="rip-curl", w=900),
    it("rc-email-polerones", "email/20230125-Escolar-Polerones.gif", "email", "Rip Curl", "Vuelta a clases: polerones", project="rip-curl", w=900),
    it("rc-email-arrivals", "email/20230201-1-New-Arrivals.gif", "email", "Rip Curl", "New Arrivals animado", project="rip-curl", w=900),
    it("rc-email-allday-1", "email/20230710 ALLDay_50%.jpg", "email", "Rip Curl", "All Day: 50% off en polerones", project="rip-curl"),
    it("rc-email-allday-2", "email/20230717 AllDay_Casaca-Parkas.jpg", "email", "Rip Curl", "All Day: casacas y parkas", project="rip-curl"),
    it("rc-email-antiseries", "web/20230216 Antiseries.jpg", "email", "Rip Curl", "Anti Series: anti wind, anti cold, anti rain", project="rip-curl", w=900),

    # ───────────────────────── Tumedico.com (salud en línea) ─────────────────────────
    it("tm-banner-espacio", "banners/2.jpg", "banners", "Tumedico.com", "Su espacio de salud en línea", project="tumedico"),
    it("tm-banner-opinion", "banners/3.jpg", "banners", "Tumedico.com", "Opinión Médica: desde cualquier lugar", project="tumedico"),
    it("tm-banner-home", "banners/7.jpg", "banners", "Tumedico.com", "Banner de la página de inicio", project="tumedico"),
    it("tm-banner-registro", "banners/clinicvirtual.jpg", "banners", "Tumedico.com", "Regístrese gratis", project="tumedico"),
    it("tm-banner-linkedin", "banners/google.jpg", "banners", "Tumedico.com", "Banner para LinkedIn", project="tumedico"),

    it("tm-red-alimentos", "redes/Alimentos_que_envejecen01-07.jpg", "redes", "Tumedico.com", "Alimentos que envejecen tu piel", project="tumedico"),
    it("tm-red-videojuego", "redes/EFEMERIDES 12-09 dia del videohuego.jpg", "redes", "Tumedico.com", "Día del videojuego", project="tumedico"),
    it("tm-red-sueno", "redes/EFEMERIDES...jpg", "redes", "Tumedico.com", "Día mundial del sueño", project="tumedico"),
    it("tm-red-confort", "redes/FRASES, La zona de confort es un lugar maravilloso, pero nada crece alli...jpg", "redes", "Tumedico.com", "Frase: la zona de confort", project="tumedico"),
    it("tm-red-miedo", "redes/Frases, El miedo no existe en otro lugar excepto en la mente.jpg", "redes", "Tumedico.com", "Frase: el miedo no existe", project="tumedico"),
    it("tm-red-investigaciones", "redes/INVESTIGACIONES...jpg", "redes", "Tumedico.com", "Investigaciones: tatuaje que mide el azúcar", project="tumedico"),
    it("tm-red-recetas", "redes/RECETAS...jpg", "redes", "Tumedico.com", "Receta: pastel de queso bajo en calorías", project="tumedico"),
    it("tm-red-sexualidad", "redes/SEXUALIDAD...jpg", "redes", "Tumedico.com", "Sexualidad", project="tumedico"),
    it("tm-red-vitiligo", "redes/Vitiligo 25-06.jpg", "redes", "Tumedico.com", "Día mundial del vitiligo", project="tumedico"),
    it("tm-red-bailar", "redes/beneficios_de_bailar_30-07.jpg", "redes", "Tumedico.com", "Beneficios de bailar", project="tumedico"),
    it("tm-red-salud-mental", "redes/efe.jpg", "redes", "Tumedico.com", "Día mundial de la salud mental", project="tumedico"),
    it("tm-red-ambiente", "redes/medio_ambiente_5_de_junio.jpg", "redes", "Tumedico.com", "Día mundial del medio ambiente", project="tumedico"),

    it("tm-email-citas", "email/citasmedicas.jpg", "email", "Tumedico.com", "Gestione sus citas médicas", project="tumedico", w=900, pie=0.98),
    it("tm-email-usuarios", "email/usuarios.jpg", "email", "Tumedico.com", "Invitación para usuarios", project="tumedico", w=900, pie=0.98),

    it("tm-pendon", "pendones/pendones.jpg", "impreso", "Tumedico.com", "Pendón: espacio de salud en línea", project="tumedico",
       desc="Pendón para una campaña en Perú."),
    it("tm-camisa", "ia/camisa-tumedico.png", "impreso", "Tumedico.com", "Camisa corporativa: mockup realista", project="tumedico", w=1536,
       desc="Mockup fotorrealista de la camisa corporativa, generado con IA a partir del diseño plano."),
    it("tm-camisa-plano", "pop/camisa.jpg", "impreso", "Tumedico.com", "Camisa corporativa: diseño plano", project="tumedico", gallery=False,
       desc="Diseño original en vectores, frente y espalda."),
    it("tm-carpeta", "pop/carpeta.jpg", "impreso", "Tumedico.com", "Carpeta corporativa", project="tumedico"),

    # ───────────────────────── Zapacos ─────────────────────────
    it("zp-donna-kuin", "redes/Donna-Kuin.jpg", "redes", "Zapacos", "Ejercítate al mejor estilo de Donna Kuin"),
    it("zp-look-comodo", "redes/Look-05-11-2015.jpg", "redes", "Zapacos", "Un look cómodo para tu día"),
    it("zp-lasftft", "redes/Lasftft.jpg", "redes", "Zapacos", "Un look LOSFTF"),
    it("zp-estilo-moda", "redes/frase-06-01-2016.jpg", "redes", "Zapacos", "Frase: estilo y moda"),
    it("zp-mujer-elegante", "redes/frase-11-11-2015.jpg", "redes", "Zapacos", "Frase: la mujer elegante"),
    it("zp-lenguaje-corporal", "redes/frase-16-julio-2015..jpg", "redes", "Zapacos", "Frase: los zapatos y la actitud"),
    it("cygnus", "redes/Cygnus.jpg", "redes", "Cygnus", "Añade un estilo único a tus pisadas"),
    it("zp-news-1", "email/1.jpg", "email", "Zapacos", "Newsletter de temporada", w=900, pie=0.98),
    it("zp-news-2", "email/2.jpg", "email", "Zapacos", "Newsletter de temporada: regalos", w=900, pie=0.98),
    it("zp-news-3", "email/esta utilizarla.jpg", "email", "Zapacos", "Newsletter: Celebra 2015", w=900, pie=0.98),
    it("zp-news-4", "email/marcketing000.jpg", "email", "Zapacos", "Newsletter: Reír 2016", w=900, pie=0.98),

    # ───────────────────────── Banners de moda y estilo de vida ─────────────────────────
    it("bn-infantil", "banners/1.jpg", "banners", "Moda infantil", "Bebés que son súper"),
    it("bn-bommer", "banners/4.jpg", "banners", "Bommer", "Ejercítate con Bommer"),
    it("bn-converse", "banners/5.jpg", "banners", "Converse", "Banner de producto"),
    it("bn-ebooks", "banners/6.jpg", "banners", "E-books", "Contenido de valor para una mejor calidad de vida"),
    it("bn-paez", "banners/anner-paez.jpg", "banners", "Paez", "Banner de producto"),
    it("bn-valmy", "banners/banner-Valmy.jpg", "banners", "Valmy", "Maquillaje"),
    it("bn-basinger", "banners/banner-basingerr.jpg", "banners", "Basinger", "Colección"),
    it("bn-boaonda", "banners/banner-boaonda.jpg", "banners", "Boaonda", "Añade estilo a tus pisadas"),
    it("bn-gdc", "banners/banner-collares-gdc-moda.jpg", "banners", "GDC Moda", "¿Quieres realzar tu elegancia?"),
    it("bn-elf", "banners/banner-elf.jpg", "banners", "e.l.f.", "Eyes, lips, face"),
    it("bn-rio-bags", "banners/banner-rio-bags.jpg", "banners", "Rio Bags", "Banner de colección"),
    it("bn-ropa-intima", "banners/banner-ropa-intima.jpg", "banners", "Ropa íntima", "Resalta tu sensualidad"),
    it("bn-regalo", "banners/cacao-2.jpg", "banners", "Día de los enamorados", "El regalo perfecto"),
    it("bn-qiloo", "banners/iloo-4.jpg", "banners", "Qiloo", "Banner de producto"),
    it("bn-prevaler", "banners/prevaler-1-2.jpg", "banners", "Prevaler", "Valore su salud"),
    it("bn-sublimacion", "banners/sublimacion.jpg", "banners", "Sublimación", "Cómodas y frescas: franelillas atléticas"),

    # ───────────────────────── Logos y marca ─────────────────────────
    it("moxi-du", "logos/00-LOGO.png", "identidad", "Moxi Du", "Logo para tienda de diseño", w=900),
    it("adoptame-logo", "logos/adoptame.jpg", "identidad", "Adóptame", "Logo para agenda a favor de animales rescatados", pie=0.98,
       desc="Logo de agenda con la finalidad de recaudar fondos para fundaciones de animales callejeros y crear conciencia de que la adopción es la mejor alternativa al problema."),
    it("cooklim", "logos/cooklim.jpg", "identidad", "Cooklim", "Logo de bebida infantil", pie=0.98,
       desc="Logo de bebida infantil: se trabajó con un juego de palabras en inglés para darle sentido al nombre."),
    it("guahibos", "logos/guahibos.jpg", "identidad", "Guahibos Gourmet", "Logo de restaurante", pie=0.98,
       desc="Logo de restaurante. Los guahibos son un pueblo indígena que habita en los Llanos del Orinoco, en Venezuela."),
    it("monstruo-yo", "logos/mostruo.jpg", "identidad", "Monstruo Yo", "Logo de marca de ropa", pie=0.98,
       desc="Logo de una marca de ropa."),
    it("smagic-logo", "logos/smagic.jpg", "identidad", "Smagic", "Logo de producto infantil", pie=0.98,
       desc="Logo de un producto infantil: la forma que se le da al logo crea una conexión inmediata con el niño."),
    it("atenea-logo", "logos/centroclinico-ATENEA-LogoHeader_Logo final.svg", "identidad", "Centro Clínico Atenea", "Logotipo: bienestar para ti", project="centro-clinico-atenea", kind="svg"),

    # ───────────────────────── Impresos, vallas y papelería ─────────────────────────
    it("smagic-anuncio", "banners/anuncio de revista.tif", "impreso", "Smagic", "Anuncio de revista"),
    it("valla-festival", "pendones/7 valla.jpg", "impreso", "Festival Cinematográfico", "Valla publicitaria"),
    it("adoptame-pendon", "pendones/adoptame.jpg", "impreso", "Adóptame", "Pendón de promoción: los amigos no se compran",
       desc="Pendón para la promoción de la agenda Adóptame."),
    it("sufragio", "pendones/sufragio.jpg", "impreso", "Sufragio femenino", "Pendón de campaña conmemorativa", pie=0.98,
       desc="Pendón para una campaña de conmemoración del Sufragio Femenino."),
    it("zambia-carpeta", "pop/carpeta1.jpg", "impreso", "Zambia Soluciones", "Carpeta corporativa"),
    it("zambia-sobre", "pop/sobre1.jpg", "impreso", "Zambia Soluciones", "Sobre corporativo"),
    it("zambia-tarjeta", "pop/tarjeta1.jpg", "impreso", "Zambia Soluciones", "Tarjeta corporativa tiro y retiro"),
    it("valera-tarjeta", "pop/tarjeta.jpg", "impreso", "Darwin Valera, abogado", "Tarjeta para bufetes de abogados"),

    # ───────────────────────── Email marketing de otros clientes ─────────────────────────
    it("em-hacienda", "email/MAILING HACIENDA (1).jpg", "email", "Hacienda Chacabuco", "Mailing: construye la casa que quieres"),
]
