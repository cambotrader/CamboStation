# Inject regime panel as cockpit mode 27

$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw

# Add to command list
if ($content -match '\$cmds\s*=\s*@\([^\)]*') {
    $content = $content -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"regime panel"'
}

# Inject switch block
$patch = @"
    "regime panel"      { streamlit run "$base\regime_consistency_panel.py" }
"@

if ($content -notmatch '"regime panel"') {
    $content += "`n$patch"
}

Set-Content $cockpitPath -Value $content -Encoding UTF8
Write-Host "✅ Cockpit mode 27 wired: regime panel activated."
