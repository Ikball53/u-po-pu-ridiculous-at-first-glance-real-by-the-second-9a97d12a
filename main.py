import os

# One sentence, 178 characters: a bizarre startup pitch that reads like a
# joke until the money logic lands — cheap guilty supply, subscription demand.
SENTENCE = "We buy abandoned craft kits from guilty hobbyists for $3 and resell them as mystery 'finish-it' boxes to retirees who pay $19 a month to complete a stranger's half-knitted scarf."

assert 1 <= len(SENTENCE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(SENTENCE)
