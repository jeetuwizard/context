# Renders every design source in design-src/ to a PNG at its exact size, using headless Microsoft Edge.
# Usage (from the repo root):  powershell -ExecutionPolicy Bypass -File scripts\render-assets.ps1

$ErrorActionPreference = 'Stop'

$edge = @(
    "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
    "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { throw 'Microsoft Edge not found.' }

$root = Split-Path -Parent $PSScriptRoot
$src  = Join-Path $root 'design-src'

$jobs = @(
    @{ Html = 'banner.html';                 Out = 'assets\final\banner_wizard.png';         Size = '2560,1440'; Transparent = $false },
    @{ Html = 'profile_picture.html';        Out = 'assets\final\dp_option2.png';            Size = '800,800';   Transparent = $false },
    @{ Html = 'watermark.html';              Out = 'assets\final\watermark_subscribe.png';   Size = '150,150';   Transparent = $true  },
    @{ Html = 'alt_profile_wizard_hat.html'; Out = 'assets\alternates\dp_wizard_hat.png';    Size = '800,800';   Transparent = $false },
    @{ Html = 'alt_profile_mascot.html';     Out = 'assets\alternates\dp_mascot.png';        Size = '800,800';   Transparent = $false }
)

foreach ($job in $jobs) {
    $html = Join-Path $src $job.Html
    $out  = Join-Path $root $job.Out
    $url  = 'file:///' + ($html -replace '\\', '/')
    $edgeArgs = @('--headless', '--disable-gpu', '--hide-scrollbars', "--screenshot=$out", "--window-size=$($job.Size)", $url)
    if ($job.Transparent) { $edgeArgs += '--default-background-color=00000000' }
    $started = Get-Date
    # Edge logs harmless errors to stderr, which Windows PowerShell 5.1 would treat as fatal.
    Start-Process -FilePath $edge -ArgumentList $edgeArgs -Wait -WindowStyle Hidden
    if (-not (Test-Path $out) -or (Get-Item $out).LastWriteTime -lt $started) {
        throw "Rendering failed for $($job.Html)"
    }
    Write-Host "Rendered $($job.Out)"
}
