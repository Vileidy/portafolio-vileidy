// Convierte el material original (material/**) en imágenes web listas para Git (src/assets/work/**).
//
//   npm run images             procesa solo lo nuevo o modificado
//   npm run images -- --force  regenera todo
//
// Las carpetas se conservan (material/proyecto-a/foto.jpg -> src/assets/work/proyecto-a/foto.webp),
// los nombres se normalizan a minúsculas-con-guiones, se respeta la orientación EXIF y se
// eliminan los metadatos (incluida la ubicación GPS).
import { mkdir, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';

const SRC = 'material';
const OUT = 'src/assets/work';
const MAX_WIDTH = 2400;
const QUALITY = 82;
const WARN_BYTES = 1.5 * 1024 * 1024;

const INPUT_EXT = new Set(['.jpg', '.jpeg', '.png', '.webp', '.avif', '.tif', '.tiff']);
const SKIPPED_EXT = new Set(['.gif', '.mp4', '.mov', '.webm', '.psd', '.ai', '.heic']);
const force = process.argv.includes('--force');

const slug = (s) =>
  s
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '') || 'sin-nombre';

const kb = (bytes) => `${(bytes / 1024).toFixed(0)} KB`;

let entries;
try {
  entries = await readdir(SRC, { recursive: true, withFileTypes: true });
} catch {
  console.log(`No existe la carpeta ${SRC}/. Créala y coloca ahí tu material.`);
  process.exit(0);
}

const files = entries
  .filter((e) => e.isFile() && e.name !== 'README.md' && !e.name.startsWith('.'))
  .map((e) => path.join(e.parentPath, e.name))
  .sort();

const claimed = new Map();
let done = 0;
let upToDate = 0;
let bytesIn = 0;
let bytesOut = 0;
const ignored = [];
const heavy = [];

for (const file of files) {
  const ext = path.extname(file).toLowerCase();
  if (!INPUT_EXT.has(ext)) {
    if (SKIPPED_EXT.has(ext)) ignored.push(file);
    continue;
  }

  const rel = path.relative(SRC, file);
  const parts = path.dirname(rel) === '.' ? [] : path.dirname(rel).split(path.sep);
  const outFile = path.join(OUT, ...parts.map(slug), `${slug(path.parse(file).name)}.webp`);

  if (claimed.has(outFile)) {
    console.warn(`! ${file} y ${claimed.get(outFile)} generan el mismo nombre (${outFile}); se omite la segunda.`);
    continue;
  }
  claimed.set(outFile, file);

  const [inStat, outStat] = await Promise.all([stat(file), stat(outFile).catch(() => null)]);
  if (!force && outStat && outStat.mtimeMs >= inStat.mtimeMs) {
    upToDate++;
    continue;
  }

  await mkdir(path.dirname(outFile), { recursive: true });
  const info = await sharp(file)
    .rotate()
    .resize({ width: MAX_WIDTH, withoutEnlargement: true })
    .webp({ quality: QUALITY })
    .toFile(outFile);

  done++;
  bytesIn += inStat.size;
  bytesOut += info.size;
  if (info.size > WARN_BYTES) heavy.push(`${outFile} (${kb(info.size)})`);
  console.log(`+ ${outFile}  ${kb(inStat.size)} -> ${kb(info.size)}`);
}

console.log(`\n${done} generadas, ${upToDate} al día.${done ? ` ${kb(bytesIn)} -> ${kb(bytesOut)}.` : ''}`);
if (heavy.length) {
  console.log(`\nPesan más de ${kb(WARN_BYTES)} (revisa si hace falta tanto detalle):\n  ${heavy.join('\n  ')}`);
}
if (ignored.length) {
  console.log(
    `\nNo se procesan (GIF, vídeo y formatos de edición no van a Git tal cual):\n  ${ignored.join('\n  ')}\n` +
      'Vídeo: expórtalo a MP4/WebM ligero o súbelo a YouTube/Vimeo. Ver material/README.md.',
  );
}
