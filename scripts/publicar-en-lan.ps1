<#
.SYNOPSIS
  Publica el portafolio en un hub de apps de red local (carpeta public\ de un servidor estático).

.DESCRIPTION
  Compila el sitio con base /<slug>, copia dist\ a <Hub>\public\<slug>\ (espejo: borra lo que ya no existe)
  y escribe el app.json que el hub usa para listarlo. No toca el firewall ni arranca servidores.

.EXAMPLE
  .\scripts\publicar-en-lan.ps1 -Hub C:\ruta\al\hub

  # o con npm:
  npm run lan -- -Hub C:\ruta\al\hub

.NOTES
  El nombre de la carpeta (-Slug) es también la ruta en el hub: http://<ip>:<puerto>/<slug>/
#>
param(
  [Parameter(Mandatory)] [string]$Hub,
  [string]$Slug = 'portafolio'
)

$ErrorActionPreference = 'Stop'
$raiz = Split-Path $PSScriptRoot -Parent
$public = Join-Path $Hub 'public'
if (-not (Test-Path $public)) { throw "No encuentro la carpeta public\ dentro de $Hub" }
$destino = Join-Path $public $Slug

Push-Location $raiz
try {
  $env:BASE_PATH = "/$Slug"
  npm run build
  if ($LASTEXITCODE -ne 0) { throw 'El build falló; no se publicó nada.' }
} finally {
  Remove-Item Env:BASE_PATH -ErrorAction SilentlyContinue
  Pop-Location
}

# robocopy: códigos 0-7 son éxito; /MIR borra del destino lo que ya no está en dist
robocopy (Join-Path $raiz 'dist') $destino /MIR /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy falló (código $LASTEXITCODE)." }

# /MIR elimina el app.json en cada pasada, así que se vuelve a escribir (UTF-8 sin BOM)
$meta = @'
{
  "name": "Portafolio · Vileidy Muñoz",
  "desc": "Diseño UI/UX, web, campañas y marca",
  "icon": "🎨"
}
'@
[IO.File]::WriteAllText((Join-Path $destino 'app.json'), $meta + "`n", (New-Object Text.UTF8Encoding($false)))

$archivos = Get-ChildItem $destino -Recurse -File
Write-Host ("Publicado en {0}: {1} archivos, {2:N1} MB" -f $destino, $archivos.Count, (($archivos | Measure-Object Length -Sum).Sum / 1MB))
Write-Host "Ábrelo desde la red: http://<IP-de-este-PC>:<puerto-del-hub>/$Slug/"
