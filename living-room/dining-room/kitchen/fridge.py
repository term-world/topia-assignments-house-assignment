import os
import requests

def main():
    print()
    print("A stainless steel fridge that feels a little out of place given the otherwise modest trappings of your home.")
    print()
    file_exist = os.path.exists("note-from-fridge.md")
    if file_exist == True:
        print("You open the door. Do you only eat condiments?")
        print()
        print("Nothing more to see here.")
        print()
    else:
        print("It looks like someone left a note on the fridge door...")
        print()
        note = requests.get("https://raw.githubusercontent.com/term-world/world-flavor/main/note-on-fridge.md")
        note_stringified = str(note.text)
        new_file = open("note-from-fridge.md", "x")
        new_file.write(note_stringified)
        new_file.close()
        print("You take the note off the fridge.")
        print()
        print("~You should see a file called 'note-on-fridge.md' in the File Explorer on the left~")
        print("~Click that file and you can read (and edit) the note~")
        print()



if __name__ == "__main__":
    main()
