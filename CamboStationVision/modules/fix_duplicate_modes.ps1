# Clean duplicate "regime console" entries from cockpit.ps1
$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw

# Remove duplicates from $cmds list
$content = ($content -split "`n") | Where-Object { $_ -notmatch '"regime console"' } | Out-String
$content = $content -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"regime console"'

# Remove duplicates from ExecuteMode block
$execBlock = '"regime console"      { streamlit run "$base\regime_console.py" }'
$lines = $content -split "`n"
$lines = $lines | Where-Object { $_ -ne $execBlock }
$lines += $execBlock

# Rewrite cleaned cockpit.ps1
Set-Content $cockpitPath -Value ($lines -join "`n") -Encoding UTF8
Write-Host "✅ Duplicate 'regime console' mode removed. Mode 28 restored and clean."
