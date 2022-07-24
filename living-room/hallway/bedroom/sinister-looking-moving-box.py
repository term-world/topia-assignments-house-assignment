import narrator
from narrator import Checkpoint
import gitit
import os

n = narrator.Narrator()

def main():
    n.path.change(4.0)
    n.narrate()
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [4.1, 4.8]
    })
    n.path.change(q.ask())
    if n.path.scene == 1:
        n.narrate()
        q = narrator.Question({
            "question": "Where will you place the `toaster.py`?",
            "responses": [
                {"choice": "living-room", "outcome": 4.2},
                {"choice": "dining-room", "outcome": 4.3},
                {"choice": "kitchen", "outcome": 4.4},
                {"choice": "hallway", "outcome": 4.5},
                {"choice": "bedroom", "outcome": 4.6},
                {"choice": "office", "outcome": 4.7}
            ]
        })
        n.path.change(q.ask())
        n.narrate()
        if n.path.scene == 3:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/toaster.py",
            "../../toaster.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("sinister-looking-moving-box.py")
        elif n.path.scene == 4:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/toaster.py",
            "../../dining-room/toaster.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("sinister-looking-moving-box.py")
        elif n.path.scene == 5:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/toaster.py",
            "../../dining-room/kitchen/toaster.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("sinister-looking-moving-box.py")
        elif n.path.scene == 6:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/toaster.py",
            "../toaster.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("sinister-looking-moving-box.py")
        elif n.path.scene == 7:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/toaster.py",
            "toaster.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("sinister-looking-moving-box.py")
        elif n.path.scene == 8:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/toaster.py",
            "../office/toaster.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("sinister-looking-moving-box.py")
    else:
        n.narrate()


if __name__ == "__main__":
    main()