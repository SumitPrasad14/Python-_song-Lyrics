import time, sys, os

# --- Hacker Terminal Style: K Khas Baat Tere Yaara ---
os.system("cls" if os.name == "nt" else "clear")
print("\nFinding: K Khas Baat Tere Yaara (New Verse)\n")
time.sleep(0.8)

lyrics = [
    "K khas baat tere yaara m, tu kudde s jinke dam p tnne reel m gunde dekhe s...",
    "Mka real m gunde hum s, are baat maan meri daaki dega tod mehakma lathi...",
    "Lukda hande tu tere saathi, jaan gwani hojya gi re j koe sedgya yaara n ghar t kaadlya salya n...",
    "Warning rihstedaara n kunba ghani hojya gi...",
    "",
    "Yaar mere sare s albaad, halak takk taar dewange haath r krte handenge...",
    "Panchayat r odd kahani hojagi...",
    "",
    "Tu mane kise ki daab nhi, tu khud m dada horya s...",
    "Are mera kaafila jaan meri, tere gaam t jyada hora s...",
    "Tu aage aage chale s, tere pache mittar khaas chale...",
    "Mera ek ishara kaafi s, ye kahan t phla naas kre...",
    "Teri gel khapitar utt r krde hando so kartut..."
]

def type_line(text, speed=0.02):   # adjust speed if needed
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# --- Run animation ---
for line in lyrics:
    type_line(line, speed=0.08)
    time.sleep(0.6)

print("\n-- Session Ended: Bhai Ka Code Band --\n")