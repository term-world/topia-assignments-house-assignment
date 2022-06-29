import os
import requests

def main():
    print()
    key_file_exists = os.path.exists("../bedroom/key-making-kit-note.md")
    if key_file_exists == True:
        mirror_file_exists = os.path.exists("bathroom-mirror-note.md")
        if mirror_file_exists == True:
            print("You wash your hands while humming to the tune of 'Happy Birthday'.")
            print()
        else:
            print("TCTC--whoever that is--has definitely been here.")
            print("There's a note on the mirror above the sink, in his (her? their?) handwriting.")
            print()
            note = requests.get("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/bathroom-mirror-note.md")
            note_stringified = str(note.text)
            new_file = open("bathroom-mirror-note.md", "x")
            new_file.write(note_stringified)
            new_file.close()
            print("~You know the drill by now; there's another note in your File Explorer~")
            print("~See if you can locate it~")
            print()
    else:
        print("You wash your hands while humming to the tune of 'Happy Birthday'.")
        print()

if __name__ == "__main__":
    main()