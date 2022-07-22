import narrator
from narrator import Checkpoint
import os

n = narrator.Narrator()
#ref: n.path.change()


def binary_ask(question: str, yes_path: float, no_path: float):
    q = narrator.Question({
        "question": question,
        "responses": [
            {"choice": "yes", "outcome": yes_path},
            {"choice": "no", "outcome": no_path}
        ]
    })
    while True:
        ask = input(q.prompt)
        if ask in q.responses:
            path = q.responses[ask].outcome
            n.path.change(path)
            break
        print("Not a valid option; try again.")

def main():
    if Checkpoint.check_flag("boxes_unpacked") == 5 and bool(Checkpoint.check_flag("lease_printed")):
        n.path.change(0.6)
        n.narrate()
        binary_ask("Throw away the note?", 0.8, 0.7)
        if n.path.scene == 0.8:
            n.narrate()
            os.remove("note-from-landlord.py")
        else:
            n.narrate()
    else:
        if bool(Checkpoint.check_flag("note_read")):
            n.path.change(0.9)
            n.narrate()
            q = narrator.Question({
                "question": "Is there a certain section you want to read?",
                "responses": [
                    {"choice": "unpacking", "outcome": 0.1},
                    {"choice": "lease", "outcome": 0.2},
                    {"choice": "file-download", "outcome": 0.3},
                    {"choice": "conclusion", "outcome": 0.4},
                    {"choice": "don't read", "outcome": 0.5}
                ]
            })
            while True:
                ask = input(q.prompt)
                if ask in q.responses:
                    path = q.responses[ask].outcome
                    n.path.change(path)
                    break
                print("Not a valid option; try again.")
            n.narrate()
        else:
            n.narrate()
            binary_ask("Read the note?", 0.1, 0.5)
            n.narrate()
            if n.path.scene != 6:
                binary_ask("Continue reading?", 0.2, 0.5)
                n.narrate()
                if n.path.scene != 6:
                    binary_ask("Continue reading?", 0.3, 0.5)
                    n.narrate()
                    if n.path.scene != 6:
                        binary_ask("Continue reading?", 0.4, 0.5)
                        n.narrate()


if __name__ == "__main__":
    main()