$base = "$HOME\CamboStation_QuantumOS\modules"
$console = "$base\cockpit.ps1"

$sequence = @(
    "pulse",
    "sync regime",
    "annotate drift",
    "compose belief",
    "myth engine"
)

foreach ($mode in $sequence) {
    Write-Host "`n▶️ Executing mode → $mode"
    & $console $mode
}
