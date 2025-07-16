# Patch regime_consistency_panel.py with proper $HOME path
$panelPath = "$HOME\CamboStation_QuantumOS\modules\regime_consistency_panel.py"
$content = Get-Content $panelPath -Raw

# Replace hardcoded Windows path with safe $HOME-based path
$content = $content -replace 'path\s*=\s*os\.path\.expandvars\(".*?"\)', 'path = os.path.expandvars(r"$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")'

Set-Content $panelPath -Value $content -Encoding UTF8
Write-Host "✅ regime_consistency_panel.py path patched successfully."
