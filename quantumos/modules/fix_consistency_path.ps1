# Patch identity_consistency_score.py with safe raw string

$filePath = "$HOME\CamboStation_QuantumOS\modules\identity_consistency_score.py"
$content = Get-Content $filePath -Raw

# Replace broken line with safe syntax
$fixed = $content -replace 'path\s*=\s*os\.path\.expandvars\(".*?"\)', 'path = os.path.expandvars(r"$HOME\\CamboStation_QuantumOS\\modules\\myth_legacy.json")'

Set-Content $filePath -Value $fixed -Encoding UTF8
Write-Host "✅ identity_consistency_score.py path patched successfully."
