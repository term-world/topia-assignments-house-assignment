import narrator
from narrator import Checkpoint
import gitit
import os

n = narrator.Narrator()

def main():
    n.path.change(3.0)
    n.narrate()
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [3.1, 3.8]
    })
    n.path.change(q.ask())
    if n.path.scene == 1:
        n.narrate()
        q = narrator.Question({
            "question": "Where will you place the `gamecylinder.py`?",
            "responses": [
                {"choice": "living-room", "outcome": 3.2},
                {"choice": "dining-room", "outcome": 3.3},
                {"choice": "kitchen", "outcome": 3.4},
                {"choice": "hallway", "outcome": 3.5},
                {"choice": "bedroom", "outcome": 3.6},
                {"choice": "office", "outcome": 3.7}
            ]
        })
        n.path.change(q.ask())
        n.narrate()
        if n.path.scene == 3:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/gamecylinder.py",
            "../../gamecylinder.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("tube-shaped-moving-box.py")
        elif n.path.scene == 4:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/gamecylinder.py",
            "../../dining-room/gameclyinder.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("tube-shaped-moving-box.py")
        elif n.path.scene == 5:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/gamecylinder.py",
            "../../dining-room/kitchen/gamecylinder.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("tube-shaped-moving-box.py")
        elif n.path.scene == 6:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/gamecylinder.py",
            "../gamecylinder.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("tube-shaped-moving-box.py")
        elif n.path.scene == 7:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/gamecylinder.py",
            "gamecylinder.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("tube-shaped-moving-box.py")
        elif n.path.scene == 8:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/gamecylinder.py",
            "../office/gamecylinder.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("tube-shaped-moving-box.py")
    else:
        n.narrate()


if __name__ == "__main__":
    main()