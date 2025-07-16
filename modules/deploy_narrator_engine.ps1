$base = "$HOME\CamboStation_QuantumOS\modules"
$target = "$base\narrator_engine.py"

function Backup($file) {
    if (Test-Path $file) {
        Copy-Item $file "$file.bak" -Force
        Write-Host "📁 Backup → $([System.IO.Path]::GetFileName($file)).bak"
    }
}

$code = @'


$code = @'
from signal_overlay import get_recent_signals

def narrate_session():
    logs = get_recent_signals()
    lines = []

    for s in logs:
        archetype = s["archetype"]
        mood = s["mood"]
        signal = s["signal"]
        conviction = s["conviction"]

        if conviction > 0.75:
            sentiment = "with unwavering intent"
        elif conviction > 0.65:
            sentiment = "guided by quiet confidence"
        else:
            sentiment = "tentative yet reflective"

        line = f"🕒 {s['timestamp']} → The {archetype}, {mood.lower()} and alert, cast a {signal} {sentiment}. Conviction scored at {conviction}."
        lines.append(line)

    if not lines:
        lines.append("📭 No signals detected — silence speaks louder today.")

    return lines
'@

Backup $target
Set-Content -Path $target -Value $code -Encoding UTF8

Write-Host "`n✅ narrator_engine.py deployed."
Write-Host "📌 To hook into Streamlit dashboard:"
Write-Host "`nfrom narrator_engine import narrate_session"
Write-Host "with st.tabs(['🎙️ Session Narrator'])[0]:"
Write-Host "    for story in narrate_session():"
Write-Host "        st.markdown(story)"
