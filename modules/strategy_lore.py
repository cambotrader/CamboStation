lore_book = []
def generate_lore(signal, archetype, belief):
    entry = f"{archetype} executed {signal} believing '{belief}'."
    lore_book.append(entry)
    return lore_book[-3:]
