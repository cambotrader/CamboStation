from narrator_engine import narrate_session
from summary_poet import compose_closing_stanza
from session_summary import generate_session_summary
from signal_overlay import get_recent_signals
from belief_grid import render_belief_grid
from regime_storyteller import narrate_regime
from voice_archive import archive_voice

def run_end_of_day_sequence():
    print("🧠 CamboStation End-of-Day Orchestrator")
    print("—" * 40)

    # Session Summary
    summary = generate_session_summary()
    print("📊 Summary:")
    print(summary["voice"])

    # Regime Voice
    print("\n🌀 Regime Story:")
    for line in narrate_regime():
        print(line)

    # Narrator Voice
    print("\n🎙️ Narrator:")
    for line in narrate_session():
        print(line)

    # Poetic Stanza
    print("\n🪶 Closing Stanza:")
    print(compose_closing_stanza())

    # Archive
    saved_file = archive_voice()
    print(f"\n📁 Voice archived in: {saved_file}")
