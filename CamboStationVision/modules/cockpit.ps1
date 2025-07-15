$base = "$HOME\CamboStation_QuantumOS\modules"

$cmds = @(
    "legend plus",
    "voice stream",
    "reload",
    "ready",
    "pulse",
    "sync regime",
    "annotate drift",
    "compose belief",
    "narrate execution",
    "myth engine",
    "run full sequence",
    "end-of-day protocol",
    "run myth cycle",
    "memory suite",
    "legend panel",
    "menu",
    "harmonics panel",
    "ritual tab",
    "vision initiator",
    "ignition panel",
    "myth index",
    "mood chart",
    "drift analyzer",
    "consistency panel",
    "regime tracker",
    "consistency score",
    "regime panel",
    "regime console",
    "regime forecaster"
)

Write-Host "`nCamboStation Command Menu"
for ($i = 0; $i -lt $cmds.Length; $i++) {
    $num = $i + 1
    Write-Host "$num → $($cmds[$i])"
}

$mode = Read-Host "`nChoose mode (1-$($cmds.Length))"
$mode = [int]$mode
$selection = $cmds[$mode - 1]

function ExecuteMode($mode) {
    switch ($mode) {
        "legend plus"        { Write-Host "Launching legend plus..." }
        "voice stream"       { Write-Host "Starting voice stream..." }
        "reload"             { Write-Host "Reloading modules..." }
        "ready"              { Write-Host "System ready..." }
        "pulse"              { Write-Host "Emitting pulse..." }
        "sync regime"        { Write-Host "Syncing regime..." }
        "annotate drift"     { Write-Host "Annotating drift..." }
        "compose belief"     { Write-Host "Composing belief..." }
        "narrate execution"  { Write-Host "Narrating execution..." }
        "myth engine"        { Write-Host "Spinning myth engine..." }
        "run full sequence"  { Write-Host "Running full sequence..." }
        "end-of-day protocol"{ Write-Host "Executing end-of-day protocol..." }
        "run myth cycle"     { Write-Host "Cycling mythflow..." }
        "memory suite"       { Write-Host "Opening memory suite..." }
        "legend panel"       { Write-Host "Showing legend panel..." }
        "menu"               { Write-Host "Showing menu..." }
        "harmonics panel"    { Write-Host "Launching harmonics panel..." }
        "ritual tab"         { Write-Host "Starting ritual tab..." }
        "vision initiator"   { Write-Host "Triggering vision initiator..." }
        "ignition panel"     { Write-Host "Igniting panel..." }
        "myth index"         { Write-Host "Accessing myth index..." }
        "mood chart"         { Write-Host "Displaying mood chart..." }
        "drift analyzer"     { Write-Host "Opening drift analyzer..." }
        "consistency panel"  { Write-Host "Showing consistency panel..." }
        "regime tracker"     { Write-Host "Launching regime tracker..." }
        "consistency score"  { Write-Host "Computing consistency score..." }
        "regime panel"       { streamlit run "$base\regime_consistency_panel.py" }
        "regime console"     { streamlit run "$base\regime_console.py" }
        "regime forecaster"  { streamlit run "$base\regime_forecaster.py" }
        default              { Write-Host "Mode '$mode' not recognized." }
    }
}

ExecuteMode $selection
