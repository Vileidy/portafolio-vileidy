<#
.SYNOPSIS
  Genera una imagen con la sesión de Codex CLI de la persona que ejecuta el script.

.DESCRIPTION
  Copia el brief y las imágenes de referencia a una carpeta de trabajo, ejecuta `codex exec` con la
  herramienta integrada de generación de imágenes y deja el resultado en -Salida.
  Las referencias y el brief se ENVÍAN a OpenAI a través de la cuenta de ChatGPT con la que Codex tiene
  la sesión iniciada: no incluyas fotos de personas ni material confidencial sin permiso.

.EXAMPLE
  .\scripts\generar-imagen-codex.ps1 -Brief docs\briefs-ia\camisa-tumedico.md `
      -Referencias "PORTAFOLIO 2026 OK\Imag Categorias\P.OP\camisa.jpg" `
      -Salida "PORTAFOLIO 2026 OK\Imag Categorias\generadas-ia"

.NOTES
  -Modelo: el config.toml de Codex puede fijar un modelo que la cuenta no admite
  (p. ej. gpt-6.1-sol, error 400). Aquí se fuerza uno válido solo para esta ejecución,
  sin tocar la configuración. Los disponibles salen de `~\.codex\models_cache.json`.
#>
param(
  [Parameter(Mandatory)] [string]$Brief,
  [string[]]$Referencias = @(),
  [Parameter(Mandatory)] [string]$Salida,
  [string]$Modelo = 'gpt-5.6-sol'
)

$ErrorActionPreference = 'Stop'
if (-not (Get-Command codex -ErrorAction SilentlyContinue)) { throw 'No encuentro Codex CLI (npm i -g @openai/codex).' }

$trabajo = Join-Path ([IO.Path]::GetTempPath()) ("codex-img-" + [guid]::NewGuid().ToString('N').Substring(0, 8))
New-Item -ItemType Directory -Force (Join-Path $trabajo 'out') | Out-Null
Copy-Item $Brief (Join-Path $trabajo 'brief.md')
$refs = foreach ($r in $Referencias) { $d = Join-Path $trabajo (Split-Path $r -Leaf); Copy-Item $r $d; $d }
New-Item -ItemType Directory -Force $Salida | Out-Null

Push-Location $trabajo
try {
  $argumentos = @('exec', 'Read brief.md in the current directory and carry it out with your image generation tool. Save the result exactly where the brief says.',
            '-m', $Modelo, '-s', 'workspace-write', '--skip-git-repo-check', '--json', '-o', 'out\ultimo-mensaje.txt')
  if ($refs) { $argumentos += @('-i') + $refs }   # -i va al final: acepta varios archivos y se comería el prompt
  # Codex escribe avisos inofensivos por stderr; con 'Stop' PowerShell 5.1 los trataría como error
  $ErrorActionPreference = 'Continue'
  & codex @argumentos 2>&1 | Out-File -Encoding utf8 'out\eventos.jsonl'
  $ErrorActionPreference = 'Stop'
} finally { Pop-Location }

$imagenes = Get-ChildItem (Join-Path $trabajo 'out') -File | Where-Object { $_.Extension -match 'png|jpe?g|webp' }
if (-not $imagenes) { Write-Warning "Codex no dejó ninguna imagen. Revisa $trabajo\out\eventos.jsonl"; exit 1 }
foreach ($i in $imagenes) { Copy-Item $i.FullName $Salida -Force; Write-Host "Guardada: $(Join-Path $Salida $i.Name)" }
Write-Host 'Revisa la imagen a ojo (textos, colores, logos) antes de usarla y añádela a scripts/catalogo.py con src "ia/...".'
