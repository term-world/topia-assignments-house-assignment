import os
import requests

def main():
    print()
    print("A stainless steel fridge that feels a little out of place given the otherwise modest trappings of your home.")
    print()
    file_exists = os.path.exists("note-from-fridge.md")
    if file_exists == True:
        print("You open the door. Do you only eat condiments?")
        print()
        print("Nothing more to see here.")
        print()
    else:
        print("It looks like someone left a note on the fridge door...")
        print("The note kinda' looks like...a to-do list?")
        print()
        note = requests.get("https://raw.githubusercontent.com/term-world/world-flavor/main/fridge-to-do-list.md")
        note_stringified = str(note.text)
        new_file = open("fridge-to-do-list.md", "x")
        new_file.write(note_stringified)
        new_file.close()
        print("~You should see a file called 'fridge-to-list.md' in the File Explorer on the left~")
        print("~Click that file and you can read (and edit) the note~")
        print()



if __name__ == "__main__":
    main()
