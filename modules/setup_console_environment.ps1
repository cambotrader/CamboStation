powershell "$env:USERPROFILE\CamboStation_QuantumOS\modules# Setup CamboStation Console Multipage Environment

$baseDir = "$env:USERPROFILE\CamboStation_QuantumOS\modules\regime_console"
New-Item -ItemType Directory -Path $baseDir -Force | Out-Null

# ───────────── Shared Core Module ─────────────
$corePath = Join-Path $baseDir "regime_console_core.py"
$coreContent = @'
import os, json
from collections import defaultdict, Counter
from datetime import datetime
import pandas as pd

def load_legacy():
    path = os.path.join(os.path.expanduser("~"), "CamboStation_QuantumOS", "modules", "myth_legacy.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_period(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%Y-%m")

def track_regimes(logs):
    by_period = defaultdict(list)
    for date, entry in logs.items():
        parts = entry.split("'")
        if len(parts) < 4:
            continue
        label = f"{parts[1]}:{parts[3]}"
        period = get_period(date)
        by_period[period].append(label)
    results = []
    for period in sorted(by_period):
        freq = Counter(by_period[period])
        top = freq.most_common(1)[0]
        results.append((period, top[0], top[1]))
    return results

def load_sample_ohlc():
    dates = pd.date_range(end=datetime.today(), periods=50)
    data = pd.DataFrame({
        "Open": pd.Series([100 + i + (i % 5) * 2 for i in range(50)], index=dates),
        "High": pd.Series([102 + i + (i % 3) * 2 for i in range(50)], index=dates),
        "Low": pd.Series([98 + i - (i % 4) * 2 for i in range(50)], index=dates),
        "Close": pd.Series([101 + i + (i % 2) * 2 for i in range(50)], index=dates),
    })
    return data
'@
Set-Content -Path $corePath -Value $coreContent -Encoding UTF8

# ───────────── Tab 1: Home.py ─────────────
$home = @'
import streamlit as st
from regime_console_core import track_regimes, load_legacy

st.title("📖 Regime Console - Identity Regime")
logs = load_legacy()
if not logs:
    st.error("No legacy data found.")
else:
    for period, label, count in track_regimes(logs):
        st.markdown(f"- {period}: **{label}** ({count} sessions)")
'@
Set-Content "$baseDir\Home.py" -Value $home -Encoding UTF8

# ───────────── Tab 2: IdentityScore.py ─────────────
$score = @'
import streamlit as st
try:
    from identity_consistency_score import compute_consistency_score
    score = compute_consistency_score()
    st.title("🧩 Identity Consistency Score")
    st.code(score, language="text")
except Exception as e:
    st.warning("Consistency score module missing or failed to load.")
'@
Set-Content "$baseDir\IdentityScore.py" -Value $score -Encoding UTF8

# ───────────── Tab 3: Candles.py ─────────────
$candles = @'
import streamlit as st
from regime_console_core import load_sample_ohlc
import talib

st.title("📈 Candlestick Pattern Recognition")
df = load_sample_ohlc()
hammer = talib.CDLHAMMER(df.Open, df.High, df.Low, df.Close)
df["Hammer"] = hammer
st.dataframe(df[["Open", "High", "Low", "Close", "Hammer"]].tail(10))
'@
Set-Content "$baseDir\Candles.py" -Value $candles -Encoding UTF8

# ───────────── Tab 4: ChartPatterns.py ─────────────
$patterns = @'
import streamlit as st
from regime_console_core import load_sample_ohlc

try:
    from patternpy.tradingpatterns import head_and_shoulders
    st.title("🗺️ PatternPy Chart Recognition")
    df = load_sample_ohlc()
    df = head_and_shoulders(df)
    st.dataframe(df.tail(10))
except ImportError:
    st.warning("PatternPy not installed. Clone from GitHub to enable chart pattern detection.")
'@
Set-Content "$baseDir\ChartPatterns.py" -Value $patterns -Encoding UTF8

Write-Host "✅ CamboStation Regime Console multipage layout successfully built."

