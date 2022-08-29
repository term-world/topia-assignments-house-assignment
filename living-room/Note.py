import narrator
from narrator import Checkpoint
import os

n = narrator.Narrator()

def main():
    unpacked = Checkpoint.check_flag("boxes_unpacked")
    lease_printed = bool(Checkpoint.check_flag("lease_printed"))
    
    if unpacked == 5 and lease_printed:
        n.path.change(0.6)
        n.narrate()
        q = narrator.YesNoQuestion({
            "prompt":"Throw away the note", 
            "outcomes":[0.8, 0.7]
        })
        n.path.change(q.ask())
        if n.path.scene == 0.8:
            os.remove("note.py")
        n.narrate()
        return

    if bool(Checkpoint.check_flag("note_read")):
        n.path.change(0.9)
        n.narrate()
        q = narrator.Question({
            "question": "Is there a certain section you want to read",
            "responses": [
                {"choice": "unpacking", "outcome": 0.1},
                {"choice": "lease", "outcome": 0.2},
                {"choice": "file-download", "outcome": 0.3},
                {"choice": "conclusion", "outcome": 0.4},
                {"choice": "don't read", "outcome": 0.5}
            ]
        })
        n.path.change(q.ask())
        n.narrate()
        return
    
    n.narrate()
    q = narrator.YesNoQuestion({
        "question": "Read the note",
        "outcomes": [0.1, 0.5]
    })
    n.path.change(q.ask())
    n.narrate()
    while n.path.scene < 6:
        q = narrator.YesNoQuestion({
            "question": "Continue reading",
            "outcomes": [f"0.{n.path.scene}", 0.5]
        })
        n.path.change(q.ask())
        n.narrate()
    Checkpoint.set_flag("note_read", True)

if __name__ == "__main__":
    main()