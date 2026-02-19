import time, sys, os

# --- Hacker Terminal Style: Raat Ke Shikari ---
os.system("cls" if os.name == "nt" else "clear")
print("\nFinding: Raat Ke Shikari (Masoom Sharma)\n")
time.sleep(0.8)

lyrics = [
    "Se mahra mind different, tu se chhori innocent...",
    "Soch samajh ke layie dil yaara ki gailan...",
    "Banava kaidiyan ki rail, second'an mein deva pel...",
    "Issa khel khelya kara hathiyara ki gailan...",
    "",
    "Saa hum raat ke shikari, jane duniya yan saari...",
    "Tu kariye na mahre pe trust bawli...",
    "Re laya khopdi pe sun tere yaar ne saman...",
    "Fer kar diya asla bharasht bawli...",
    "",
    "Re laya khopdi pe sun tere yaar ne saman...",
    "Fer kar diya asla bharasht bawli...",
    "",
    "Ho levya Shambhu ji ki butti, tu cheli nahi uthi...",
    "Chale kafila mahra, na line gadiyan ki tutti...",
    "Tu se hussan aa ki rani, hum rakha bande khani...",
    "Bande thokne mein aaye sada ist bawli...",
    "",
    "Re laya khopdi pe sun tere yaar ne saman...",
    "Fer kar diya asla bharasht bawli...",
    "",
    "Sda bhaichara rakha, kade rakhi na mashook..."
]

def type_line(text, speed=0.02):
    """Typewriter-style effect"""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# --- Typing animation ---
for line in lyrics:
    type_line(line, speed=0.08)
    time.sleep(0.6)

print("\n-- Session Ended: Yaadein Reh Gayi --\n")