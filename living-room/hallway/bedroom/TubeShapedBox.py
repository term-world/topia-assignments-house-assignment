import os
import narrator

from narrator import Checkpoint
from inventory.Item import BoxSpec

class TubeShapedBox(BoxSpec):

    pass

def main():

    n = narrator.Narrator()
    n.path.change(3)
    n.narrate()
    
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [3.1, 3.8]
    })

    n.path.change(q.ask())

    n.narrate()

    if n.path.scene == 9:
        return

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

    n.path.change(q.ask())

    n.narrate()

    cwd = Checkpoint.check_flag("cwd")
    location = Checkpoint.check_flag(q.choice)
    
    box = TubeShapedBox()
    box.use(action="unpack",items="GameCylinder.py")

    os.rename(
        "GameCylinder.py",
        f"{cwd}/{location}/GameCylinder.py"
    )

    print(f"🎮 >-MOVED-> {q.choice}")
    boxes_unpacked = Checkpoint.check_flag("unpacked")
    Checkpoint.set_flag("unpacked", boxes_unpacked + 1)


if __name__ == "__main__":
    main()