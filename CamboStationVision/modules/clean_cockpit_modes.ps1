# Clean duplicated cockpit entries
$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw

# 🧹 Clean duplicate entries in $cmds array
$lines = $content -split "`n"
$cmdBlock = $lines | Where-Object { $_ -match '"regime console"' }
if ($cmdBlock.Count -gt 1) {
    $lines = $lines | Where-Object { $_ -notmatch '"regime console"' }
    $lines = $lines + '    "regime console"'
}

# 🧹 Remove duplicate execution blocks
$execBlock = '"regime console"      { streamlit run "$base\regime_console.py" }'
$execLines = $lines | Where-Object { $_ -match $execBlock }
if ($execLines.Count -gt 1) {
    $lines = $lines | Where-Object { $_ -ne $execBlock }
    $lines = $lines + $execBlock
}

# 💾 Rewrite cockpit.ps1 clean
Set-Content $cockpitPath -Value ($lines -join "`n") -Encoding UTF8
Write-Host "✅ Duplicate cockpit modes cleaned. 'regime console' is now singular and locked to mode 28."
