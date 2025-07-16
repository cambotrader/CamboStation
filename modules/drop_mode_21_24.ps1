# Wire cockpit modes 21–24 with clean syntax

$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw

# Add labels to $cmds list
if ($content -match '\$cmds\s*=\s*@\([^\)]*') {
    $content = $content -replace '(\$cmds\s*=\s*@\([^\)]*)', '$1,"myth index","mood chart","drift analyzer","consistency panel"'
}

# Add switch block entries
if ($content -notmatch '"myth index" {') {
    $content += "`n    `"myth index`"         { python `"$base\myth_index_score.py`" }"
}
if ($content -notmatch '"mood chart" {') {
    $content += "`n    `"mood chart`"         { python `"$base\myth_index_plot.py`" }"
}
if ($content -notmatch '"drift analyzer" {') {
    $content += "`n    `"drift analyzer`"     { python `"$base\identity_drift_analyzer.py`" }"
}
if ($content -notmatch '"consistency panel" {') {
    $content += "`n    `"consistency panel`"  { streamlit run `"$base\identity_consistency_panel.py`" }"
}

Set-Content $cockpitPath -Value $content -Encoding UTF8
Write-Host "Modes 21 through 24 wired into cockpit successfully."
