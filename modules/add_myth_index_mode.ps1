# ✅ Add "myth index" to cockpit.ps1
$cockpit = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$body = Get-Content $cockpit -Raw

if ($body -notmatch '"myth index"') {
    $body = $body -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"myth index"'
    $body += "`n    `"myth index`" { python `"$base\myth_index_score.py`" }"
    Set-Content $cockpit -Value $body -Encoding UTF8
    Write-Host "✅ Myth index mode added to cockpit."
} else {
    Write-Host "ℹ️ Myth index mode already exists."
}
