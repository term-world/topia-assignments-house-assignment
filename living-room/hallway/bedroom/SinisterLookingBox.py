import os
import narrator

from narrator import Checkpoint
from inventory.Item import BoxSpec

class SinisterLookingBox(BoxSpec):

    def __init__(self):
        super().__init__(__file__)

def main():
    
    n = narrator.Narrator()
    n.path.change(4)
    n.narrate()

    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [4.1, 4.8]
    })

    n.path.change(q.ask())

    n.narrate()

    if n.path.scene == 9:
        return
    
    q = narrator.Question({
        "question": "Where will you place the `Toaster.py`?",
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

    cwd = Checkpoint.check_flag("cwd")
    location = Checkpoint.check_flag(q.choice)
    
    box = SinisterLookingBox()
    box.use(action="unpack",items="Toaster.py")

    os.rename(
        "Toaster.py",
        f"{cwd}/{location}/Toaster.py"
    )

    print(f"🍞 >-MOVED-> {q.choice}")
    boxes_unpacked = Checkpoint.check_flag("unpacked")
    Checkpoint.set_flag("unpacked", boxes_unpacked + 1)


if __name__ == "__main__":
    main()