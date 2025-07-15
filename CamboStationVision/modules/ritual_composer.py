import glob

def compose_ritual_chain():
    files = sorted(glob.glob("voice_archive_*.txt"))
    chain = []
    for f in files:
        with open(f, "r", encoding="utf-8") as file:
            lines = [line for line in file if "🪶" in line or "Thus" in line]
            if lines:
                chain.append("\\n".join(lines))
    return chain
