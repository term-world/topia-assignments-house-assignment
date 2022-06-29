import os
import requests

def grab_file(raw_path: str, file_name: str):
    raw = requests.get(raw_path)
    text = str(raw.text)
    file = open(file_name, "x")
    file.write(text)
    file.close()

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
        grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/fridge-to-do-list.md", "fridge-to-do-list.md")
        print("~You should see a file called 'fridge-to-list.md' in the File Explorer on the left~")
        print("~Click that file and you can read (and edit) the note~")
        print()



if __name__ == "__main__":
    main()
