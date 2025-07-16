from narrator_engine import narrate_session
from session_summary import generate_session_summary
from summary_poet import compose_closing_stanza
from regime_storyteller import narrate_regime
from session_poetry_index import build_poetry_index
from voice_archive import archive_voice

def run_myth_cycle():
    print("🔱 CamboStation — Full Myth Cycle")
    print("═" * 40)

    # Strategic Summary
    summary = generate_session_summary()
    print("📊 Strategic Summary:")
    print(summary["voice"])

    # Regime Breakdown
    print("\n🌀 Regime Story:")
    for line in narrate_regime():
        print(line)

    # Narrator Session Arc
    print("\n🎙️ Narrator Reflection:")
    for line in narrate_session():
        print(line)

    # Closing Stanza
    print("\n🪶 Poetic Closing:")
    print(compose_closing_stanza())

    # Voice Archive Save
    archived = archive_voice()
    print(f"\n📁 Voice archived to: {archived}")

    # Poetry Index
    print("\n📚 Session Poetry Index:")
    for poem in build_poetry_index():
        print(poem)

    print("\n✅ Myth cycle complete. Memory imprinted.")
run_myth_cycle()
