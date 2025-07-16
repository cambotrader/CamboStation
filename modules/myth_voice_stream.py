from signal_overlay import get_recent_signals
from identity_myth_engine import synthesize_identity_myth

def narrate_voice_stream():
    logs = get_recent_signals()
    if not logs:
        print("📭 No recent signals found. Voice stream is quiet.")
        return

    stream = []
    for s in logs:
        tone = "expanding" if s['conviction'] > 0.75 else "contracting"
        line = f"🎙️ CamboStation spoke as '{s['archetype']}', in a mood of '{s['mood']}', while {tone} toward '{s['signal']}' @ {s['conviction']:.2f}"
        stream.append(line)

    print("\n🌌 Current Identity:")
    print(synthesize_identity_myth())
    print("\n📜 Voice Stream:")
    for line in stream:
        print(line)

# Call the function to trigger narration
narrate_voice_stream()
