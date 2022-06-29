import os
import requests
import gitit

def main():
    print()
    fridge_file_exists = os.path.exists("../../dining-room/kitchen/fridge-to-do-list.md")
    if fridge_file_exists == True:
        print("The key making kit the Landlord mentioned in his note!")
        print("You don't know much about key making, but the kit looks...broken?")
        print()
        key_file_exists = os.path.exists("key-making-kit-note.md")
        if key_file_exists == True:
            print("The kit's definitely busted. The handiwork of TCTC, whoever that is.")
            print()
        else:
            print("Attached to the kit is another note.")
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/key-making-kit-note.md", "key-making-kit-note.md")
            print("~You should now find another Markdown file (that's a file that ends with .md) in your File Explorer~")
            print("~Click on the file key-making-kit-note.md to see how to go about making this 'key' you need~")
            print()

    else:
        print("Uh, what's this doing here?")
        print()
        print("It looks kinda' complicated. You decide to leave it alone for now.")
        print()


if __name__ == "__main__":
    main()