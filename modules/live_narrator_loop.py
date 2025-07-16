import time
from narrator_engine import narrate_session
from summary_poet import compose_closing_stanza

def loop_voice(refresh=60):
    while True:
        print("🎙️ Narrator Update:")
        for line in narrate_session():
            print(line)
        print("\n🪶 Stanza:\n" + compose_closing_stanza())
        time.sleep(refresh)
