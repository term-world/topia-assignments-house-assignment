import narrator
from narrator import Checkpoint
import gitit
import os

n = narrator.Narrator()

def main():
    n.path.change(5.0)
    n.narrate()
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [5.1, 5.8]
    })
    n.path.change(q.ask())
    if n.path.scene == 1:
        n.narrate()
        q = narrator.Question({
            "question": "Where will you place the `busted-tv.py`?",
            "responses": [
                {"choice": "living-room", "outcome": 5.2},
                {"choice": "dining-room", "outcome": 5.3},
                {"choice": "kitchen", "outcome": 5.4},
                {"choice": "hallway", "outcome": 5.5},
                {"choice": "bedroom", "outcome": 5.6},
                {"choice": "office", "outcome": 5.7}
            ]
        })
        n.path.change(q.ask())
        n.narrate()
        if n.path.scene == 3:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/busted-tv.py",
            "../../busted-tv.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("beat-up-moving-box.py")
        elif n.path.scene == 4:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/busted-tv.py",
            "../../dining-room/busted-tv.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("beat-up-moving-box.py")
        elif n.path.scene == 5:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/busted-tv.py",
            "../../dining-room/kitchen/busted-tv.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("beat-up-moving-box.py")
        elif n.path.scene == 6:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/busted-tv.py",
            "../busted-tv.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("beat-up-moving-box.py")
        elif n.path.scene == 7:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/busted-tv.py",
            "../bedroom/busted-tv.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("beat-up-moving-box.py")
        elif n.path.scene == 8:
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-0-additions/busted-tv.py",
            "busted-tv.py")
            unpacked = Checkpoint.check_flag("boxes_unpacked")
            unpacked += 1
            Checkpoint.set_flag("boxes_unpacked", unpacked)
            os.remove("beat-up-moving-box.py")
    else:
        n.narrate()


if __name__ == "__main__":
    main()