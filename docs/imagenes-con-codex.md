# Imágenes generadas con Codex

Para piezas que necesitan más realismo (por ejemplo, mockups fotográficos de un diseño plano) se usa la sesión de Codex CLI de la persona dueña del portafolio, que ya tiene la herramienta `image_generation` activa.

## Cuándo sí y cuándo no

- **Sí**: mockups de piezas propias (camisas, papelería, carteles) a partir de su diseño plano, y fondos o escenas sin personas.
- **No**: fotos de personas ni retoques de su rostro (la foto de Vileidy se usa tal cual); material confidencial de clientes sin permiso; piezas con mucho texto pequeño (la IA suele deformarlo).
- Todo lo que se envía (brief y referencias) sale hacia OpenAI por la cuenta de ChatGPT con la que Codex tiene la sesión iniciada, y consume de su cuota.

## Cómo se hace

```powershell
.\scripts\generar-imagen-codex.ps1 `
  -Brief docs\briefs-ia\camisa-tumedico.md `
  -Referencias "PORTAFOLIO 2026 OK\Imag Categorias\P.OP\camisa.jpg" `
  -Salida "PORTAFOLIO 2026 OK\Imag Categorias\generadas-ia"
```

1. Escribe un brief en `docs/briefs-ia/` (ver `camisa-tumedico.md`): qué imagen, qué **no** debe cambiar (colores, textos exactos) y dónde guardarla.
2. El script ejecuta `codex exec` con `-m gpt-5.6-sol`. Si el `config.toml` de Codex fija un modelo que la cuenta no admite (error 400 con `gpt-6.1-sol`), este `-m` evita tocar la configuración. Los modelos válidos salen de `~\.codex\models_cache.json`.
3. **Revisa el resultado a ojo**: textos escritos exactamente, colores y logos fieles al diseño, nada inventado. Si falla, ajusta el brief y repite.
4. La imagen queda en `PORTAFOLIO 2026 OK\Imag Categorias\generadas-ia\` (fuera de Git, como el resto de originales).
5. Añádela a `scripts/catalogo.py` con `src="ia/<archivo>"` y una `desc` que diga que está generada con IA, y ejecuta `npm run material`.

## Transparencia

Las piezas generadas con IA se identifican en su descripción ("generado con IA a partir del diseño plano"), y el diseño original se conserva junto al mockup.

## Piezas hechas así

| Pieza | Origen |
|---|---|
| `tm-camisa` | Mockup de la camisa corporativa de Tumedico.com, a partir de `P.OP/camisa.jpg` |
