# Lending kit setup for Windows 10/11: Git, Node.js LTS, VS Code, PATH.
# Run in PowerShell (not as admin needed, Windows will ask for permission itself):
#   irm https://monforje.github.io/lendingi-2026/setup/win.txt | iex

$ErrorActionPreference = 'Stop'
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}

function Say($t) { Write-Host "`n== $t" -ForegroundColor Cyan }
function Ok($t)  { Write-Host "   OK  $t" -ForegroundColor Green }
function Warn($t){ Write-Host "   !!  $t" -ForegroundColor Yellow }
function Has($c) { [bool](Get-Command $c -ErrorAction SilentlyContinue) }
function Refresh-Path {
  $m = [Environment]::GetEnvironmentVariable('Path','Machine')
  $u = [Environment]::GetEnvironmentVariable('Path','User')
  $env:Path = ($m + ';' + $u)
}
function Add-UserPath($dir) {
  if (-not (Test-Path $dir)) { return }
  $u = [Environment]::GetEnvironmentVariable('Path','User'); if (-not $u) { $u = '' }
  if (($u -split ';') -notcontains $dir) {
    [Environment]::SetEnvironmentVariable('Path', ($u.TrimEnd(';') + ';' + $dir).TrimStart(';'), 'User')
    Ok "PATH += $dir"
  }
}
$HasWinget = Has winget
function WG($id) {
  winget install -e --id $id --silent --accept-source-agreements --accept-package-agreements
  if ($LASTEXITCODE -ne 0 -and $LASTEXITCODE -ne -1978335189) { throw "winget $id exit $LASTEXITCODE" }
}
function Download($url, $out) {
  Write-Host "   download $url"
  Invoke-WebRequest -UseBasicParsing -Uri $url -OutFile $out
}

Write-Host "Lending kit setup: Git + Node.js LTS + VS Code" -ForegroundColor Cyan
if (-not $HasWinget) { Warn "winget not found, using direct downloads" }

# 1. Git
Say "Git"
Refresh-Path
if (Has git) { Ok (git --version) } else {
  try {
    if ($HasWinget) { WG 'Git.Git' } else { throw 'no winget' }
  } catch {
    $rel = Invoke-RestMethod 'https://api.github.com/repos/git-for-windows/git/releases/latest'
    $arch = if ($env:PROCESSOR_ARCHITECTURE -eq 'ARM64') { 'arm64' } else { '64-bit' }
    $asset = $rel.assets | Where-Object { $_.name -match "^Git-.*-$arch\.exe$" } | Select-Object -First 1
    $exe = Join-Path $env:TEMP $asset.name
    Download $asset.browser_download_url $exe
    Start-Process $exe -ArgumentList '/VERYSILENT','/NORESTART','/SP-' -Verb RunAs -Wait
  }
  Add-UserPath "$env:ProgramFiles\Git\cmd"
  Refresh-Path
  if (Has git) { Ok (git --version) } else { Warn "Git installed, open a new terminal" }
}

# 2. Node.js LTS (node + npm + npx)
Say "Node.js LTS"
if (Has node) { Ok ("node " + (node -v)) } else {
  try {
    if ($HasWinget) { WG 'OpenJS.NodeJS.LTS' } else { throw 'no winget' }
  } catch {
    $lts = (Invoke-RestMethod 'https://nodejs.org/dist/index.json' | Where-Object { $_.lts } | Select-Object -First 1).version
    $arch = if ($env:PROCESSOR_ARCHITECTURE -eq 'ARM64') { 'arm64' } else { 'x64' }
    $msi = Join-Path $env:TEMP "node-$lts-$arch.msi"
    Download "https://nodejs.org/dist/$lts/node-$lts-$arch.msi" $msi
    Start-Process msiexec.exe -ArgumentList '/i', "`"$msi`"", '/qn', '/norestart' -Verb RunAs -Wait
  }
  Refresh-Path
}
Add-UserPath "$env:ProgramFiles\nodejs"
Add-UserPath "$env:APPDATA\npm"
New-Item -ItemType Directory -Force "$env:APPDATA\npm" | Out-Null
Refresh-Path
if (Has node) { Ok ("node " + (node -v) + ", npm " + (npm -v)) } else { Warn "Node installed, open a new terminal" }

# npm scripts (*.ps1) are blocked by default on Windows. Allow local scripts for this user only.
try {
  if ((Get-ExecutionPolicy -Scope CurrentUser) -in 'Undefined','Restricted','AllSigned') {
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force
    Ok "ExecutionPolicy CurrentUser = RemoteSigned (npm, npx work in PowerShell)"
  }
} catch { Warn "Could not change ExecutionPolicy: $($_.Exception.Message)" }

# 3. VS Code
Say "VS Code"
if (Has code) { Ok "VS Code already installed" } else {
  try {
    if ($HasWinget) { WG 'Microsoft.VisualStudioCode' } else { throw 'no winget' }
  } catch {
    $exe = Join-Path $env:TEMP 'VSCodeUserSetup.exe'
    $a = if ($env:PROCESSOR_ARCHITECTURE -eq 'ARM64') { 'win32-arm64-user' } else { 'win32-x64-user' }
    Download "https://update.code.visualstudio.com/latest/$a/stable" $exe
    Start-Process $exe -ArgumentList '/VERYSILENT','/NORESTART','/MERGETASKS=!runcode,addcontextmenufiles,addcontextmenufolders,addtopath' -Wait
  }
  Add-UserPath "$env:LOCALAPPDATA\Programs\Microsoft VS Code\bin"
  Refresh-Path
  if (Has code) { Ok "VS Code installed" } else { Warn "VS Code installed, open a new terminal" }
}

# 4. Git settings
Say "Git settings"
if (Has git) {
  git config --global init.defaultBranch main
  git config --global core.autocrlf true
  if (-not (git config --global user.name)) {
    $n = Read-Host "   Your name for commits (Enter = skip)"
    if ($n) { git config --global user.name "$n" }
  }
  if (-not (git config --global user.email)) {
    $e = Read-Host "   Email from GitHub (Enter = skip)"
    if ($e) { git config --global user.email "$e" }
  }
  Ok "branch main, user: $(git config --global user.name) <$(git config --global user.email)>"
}

Say "Done"
foreach ($c in 'git','node','npm','code') {
  if (Has $c) { Ok "$c found" } else { Warn "$c not found yet" }
}
Write-Host "`nClose this window and open a NEW terminal. Then check: node -v; npm -v; git --version" -ForegroundColor Green
