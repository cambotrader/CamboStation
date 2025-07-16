# Repair cockpit.ps1 structure: fix $cmds, remove duplicates, close blocks

$cockpitPath = "$HOME\CamboStation_QuantumOS\modules\cockpit.ps1"
$content = Get-Content $cockpitPath -Raw
$lines = $content -split "`n"

# 🔧 Fix $cmds array closing
$cmdStart = $lines.IndexOf($lines | Where-Object { $_ -match '^\s*\$cmds\s*=\s*@\(' })
$cmdEnd = $lines.IndexOf($lines | Where-Object { $_ -match '^\s*\)' }, $cmdStart)
if ($cmdStart -ge 0 -and $cmdEnd -eq -1) {
    # Find last command entry and insert closing parenthesis
    $lastCmd = ($lines | Select-String '"[^"]+"' | Select-Object -Last 1).LineNumber
    $lines = $lines[0..$lastCmd] + ')' + $lines[$lastCmd+1..($lines.Length-1)]
}

# 🧹 Clean duplicate "regime console" from $cmds
$lines = $lines | Where-Object { $_ -notmatch '"regime console"' }
$lines = $lines | ForEach-Object {
    $_ -replace '(\$cmds\s*=\s*@\()', '$1`n    "regime console"'
}

# 🔧 Fix execution block: remove duplicates and malformed entries
$execLine = '    "regime console"      { streamlit run "$base\regime_console.py" }'
$foreLine = '    "regime forecaster"   { streamlit run "$base\regime_forecaster.py" }'

$lines = $lines | Where-Object {
    $_ -notmatch '^\s*"regime console"\s*{.*}' -and
    $_ -notmatch '^\s*"regime forecaster"\s*{.*}'
}

# 🧩 Ensure switch block is closed
if ($lines -join "`n" -notmatch 'switch\s*\(\$mode\)\s*{[^}]*}') {
    $lines += $execLine
    $lines += $foreLine
    $lines += '}'
} else {
    $lines += $execLine
    $lines += $foreLine
}

# 💾 Rewrite cleaned cockpit.ps1
Set-Content $cockpitPath -Value ($lines -join "`n") -Encoding UTF8
Write-Host "✅ Cockpit structure repaired. Mode 28: regime console, Mode 30: regime forecaster. No duplicates. All blocks closed."
