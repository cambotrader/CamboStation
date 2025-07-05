from datetime import datetime
from summary_poet import compose_closing_stanza
from narrator_engine import narrate_session

def archive_voice():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    narrator_lines = narrate_session()
    stanza = compose_closing_stanza()

    archive = f"🕒 Session {timestamp}\n"
    archive += "\n".join(narrator_lines)
    archive += f"\n\n{stanza}"

    filename = f"voice_archive_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(archive)

    return filename
