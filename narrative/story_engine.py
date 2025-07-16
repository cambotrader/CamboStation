# story_engine.py — Market Narrative Engine

class StoryEngine:
    def __init__(self):
        self.fragments = []

    def narrate(self, context):
        fragment = f"📝 Market shift due to: {context}"
        self.fragments.append(fragment)
        print(fragment)

    def summarize(self):
        print("📘 Story Summary:")
        for frag in self.fragments:
            print(f"→ {frag}")
