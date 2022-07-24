import narrator
from narrator import Checkpoint
import gitit
import os

n = narrator.Narrator()

def main():
    n.path.change(2.0)
    n.narrate()
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [2.1, 2.8]
    })
    n.path.change(q.ask())
    if n.path.scene == 1:
        n.narrate()
        q = narrator.Question({
            "question": "Where will you place the `couch.py`?",
            "responses": [
                {"choice": "living-room", "outcome": 2.2},
                {"choice": "dining-room", "outcome": 2.3},
                {"choice": "kitchen", "outcome": 2.4},
                {"choice": "hallway", "outcome": 2.5},
                {"choice": "bedroom", "outcome": 2.6},
                {"choice": "office", "outcome": 2.7}
            ]
        })
        n.path.change(q.ask())
        n.narrate()
        if n.path.scene == 3:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/couch.py",
            "../../couch.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("ultra-heavy-moving-box.py")
        elif n.path.scene == 4:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/couch.py",
            "../couch.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("ultra-heavy-moving-box.py")
        elif n.path.scene == 5:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/couch.py",
            "couch.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("ultra-heavy-moving-box.py")
        elif n.path.scene == 6:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/couch.py",
            "../../hallway/couch.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("ultra-heavy-moving-box.py")
        elif n.path.scene == 7:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/couch.py",
            "../../hallway/bedroom/couch.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("ultra-heavy-moving-box.py")
        elif n.path.scene == 8:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/couch.py",
            "../../hallway/office/couch.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("ultra-heavy-moving-box.py")
    else:
        n.narrate()


if __name__ == "__main__":
    main()