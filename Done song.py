import time
import sys

def print_lyrics():
    lyrics = [
        "Dil Mein Ab Koi Khayal Bhi Nehin Hai",
        "Tere Jaaane Ka Malal Bhi Nehin Hai",
        "Muntazir Main Tha Joh Tere Aane Ka",
        "Ab Toh Tera Intezar Hi Nehin Hai",
        "",
        "Man Mein Mere Ab Sawal Hi Nehin Hain",
        "Hua Yeh Koi Kamal Bhi Nehin Hai",
        "Jeet Gaya Tujhe Bhul Ke Main Aise Jaise",
        "Zindegi Mein Koi Haar Hi Nehin Hai",
        "Ab Toh Tera Intezar Hi Nehin Hai",
        "Ab Toh Tera Intezar Hi Nehin Hai",
        "Tere Jaaane Ka Malal Bhi Nehin Hai",
        "Ab Toh Tera Intezar Hi Nehin Hai...!",
        "",
        "Teri Taraf, Nazar Mudi",
        "Toh Dekha Hai Koi Bagal Mein Tere",
        "Teri Nazar, Se Jo Mili Meri Nazar",
        "Toh Dekha Hai Noor Chehre Pe Tere",
        "Tujhe Bulaane Ko Aawaaz Hi Nehin Hai",
        "Tujhe Bataane Ko Alfaaz Hi Nehin Hai",
        "Bhujh Rahi Hai Yeh Shamma Mere Hathon Mein"
    ]

    delays = [
        0.3, 0.3, 0.4, 0.5,  # stanza 1
        0.4, 0.3, 0.4, 0.4, 0.3, 0.4, 0.3, 0.3, 0.6,  # stanza 2
        0.4, 0.3, 0.4, 0.4, 0.4, 0.3, 0.4, 0.6,  # stanza 3̥
    ]

    print("\n🎵 Pal Pal Song (Python Lyrics Animation) 🎵\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()