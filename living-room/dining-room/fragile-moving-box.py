import os
import narrator

from narrator import Checkpoint
from inventory.Item import FixtureSpec

class FragileBox(FixtureSpec):

    import gitit

    def __init__(self):
        super().__init__()
    
    def use():
        gitit.grab_file(
            "https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/printer.py",
            "../printer.py"
        )

def main():
    n = narrator.Narrator()
    
    n.path.change(1.0)
    
    n.narrate()
    
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [1.1, 1.8]
    })
    
    n.path.change(q.ask())
    
    if n.path.scene == 1:
        n.narrate()
        q = narrator.Question({
            "question": "Where will you place the `printer.py`?",
            "responses": [
                {"choice": "living-room", "outcome": 1.2},
                {"choice": "dining-room", "outcome": 1.3},
                {"choice": "kitchen", "outcome": 1.4},
                {"choice": "hallway", "outcome": 1.5},
                {"choice": "bedroom", "outcome": 1.6},
                {"choice": "office", "outcome": 1.7}
            ]
        })
        n.path.change(q.ask())
        n.narrate()
        if n.path.scene == 3:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/printer.py",
            "../printer.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("fragile-moving-box.py")
        elif n.path.scene == 4:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/printer.py",
            "printer.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("fragile-moving-box.py")
        elif n.path.scene == 5:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/printer.py",
            "kitchen/printer.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("fragile-moving-box.py")
        elif n.path.scene == 6:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/printer.py",
            "../hallway/printer.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("fragile-moving-box.py")
        elif n.path.scene == 7:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/printer.py",
            "../hallway/bedroom/printer.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("fragile-moving-box.py")
        elif n.path.scene == 8:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/printer.py",
            "../hallway/office/printer.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("fragile-moving-box.py")
    else:
        n.narrate()


if __name__ == "__main__":
    main()