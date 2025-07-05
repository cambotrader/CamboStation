param(
    [ValidateSet("ready", "reload")]
    [string]$state = "reload"
)

$flagPath = "$HOME\CamboStation_QuantumOS\modules\.reload_flag"
Set-Content -Path $flagPath -Value $state -Encoding UTF8
Write-Host ""
Write-Host "Reload flag set to → $state"

