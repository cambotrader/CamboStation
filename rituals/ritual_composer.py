# ritual_composer.py — Symbolic Cycle Builder

class RitualComposer:
    def __init__(self):
        self.cycles = []

    def invoke_ritual(self, name, symbols):
        ritual = {"name": name, "symbols": symbols}
        self.cycles.append(ritual)
        print(f"🔮 Ritual invoked: {name} with symbols {symbols}")

    def perform_all(self):
        print("Performing all stored rituals:")
        for ritual in self.cycles:
            print(f"→ {ritual['name']} → {ritual['symbols']}")
