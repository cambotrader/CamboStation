# Final patch for cockpit.ps1 → modes 21 to 24

$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw

# Inject labels into $cmds
if ($content -match '\$cmds\s*=\s*@\([^\)]*') {
    $content = $content -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"myth index","mood chart","drift analyzer","consistency panel"'
}

# Add switch blocks if missing
$patch = @'
    "myth index"         { python "$base\myth_index_score.py" }
    "mood chart"         { python "$base\myth_index_plot.py" }
    "drift analyzer"     { python "$base\identity_drift_analyzer.py" }
    "consistency panel"  { streamlit run "$base\identity_consistency_panel.py" }
'@

if ($content -notmatch '"myth index"') {
    $content += "`n$patch"
}

Set-Content $cockpitPath -Value $content -Encoding UTF8
Write-Host "Modes 21 to 24 wired successfully."
