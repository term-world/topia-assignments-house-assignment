import os
import narrator

from narrator import Checkpoint
from inventory.Item import BoxSpec

class UltraHeavyBox(BoxSpec):

    def __init__(self):
        super().__init__(__file__)


def main():

    n = narrator.Narrator()
    n.path.change(2)
    n.narrate()
    
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [2.1, 2.8]
    })
    
    n.path.change(q.ask())

    n.narrate()

    if n.path.scene == 9:
        return

    q = narrator.Question({
        "question": "Where will you place the `Couch.py`?",
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

    cwd = Checkpoint.check_flag("cwd")
    location = Checkpoint.check_flag(q.choice)
    
    box = UltraHeavyBox()
    box.use(action="unpack",items="Couch.py")

    os.rename(
        "Couch.py",
        f"{cwd}/{location}/Couch.py"
    )

    Checkpoint.set_flag("ink", f"{cwd}/{location}")

    print(f"🛋️ >-MOVED-> {q.choice}")
    boxes_unpacked = Checkpoint.check_flag("unpacked")
    Checkpoint.set_flag("unpacked", boxes_unpacked + 1)

if __name__ == "__main__":
    main()