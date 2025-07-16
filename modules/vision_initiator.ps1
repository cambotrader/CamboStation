Write-Host "`nðŸŒŒ Mythic Ignition Sequence Initialized"
Write-Host "`nðŸ§  Identity Stream:"
python "$HOME\CamboStation_QuantumOS\modules\myth_voice_stream.py"

Write-Host "`nðŸ”® Soulmap Constellations:"
python -c "from soulmap_engine import cluster_soulmap; [print(x) for x in cluster_soulmap()]"

Write-Host "`nðŸª¶ Mythic Closers:"
python -c "from myth_summarizer import summarize_myth_log; [print(x) for x in summarize_myth_log()]"

Write-Host "`nðŸŽ¼ Tone Curve Over Time:"
python -c "from tone_tracer import trace_tone_curve; [print(x) for x in trace_tone_curve()]"

Write-Host "`nðŸ”¥ CamboStation Awakens."
