import narrator
from narrator import Checkpoint

n = narrator.Narrator()
#ref: n.path.change()


def binary_ask(question: str, yes_path: float):
    q = narrator.Question({
        "question": question,
        "responses": [
            {"choice": "yes", "outcome": yes_path},
            {"choice": "no", "outcome": 0.5}
        ]})
    while True:
        ask = input(q.prompt)
        if ask in q.responses:
            path = q.responses[ask].outcome
            n.path.change(path)
            break
        print("Not a valid option; try again.")

def main():
    if Checkpoint.check_flag("boxes_unpacked") == 5 and bool(Checkpoint.check_flag("lease_printed")):
        # TO-DO: Narrate the prompt to delete the note, and delete the note
    if bool(Checkpoint.check_flag("note_read")):
        print("yo")
    else:
        n.narrate()
        binary_ask("Read the note?", 0.1)
        n.narrate()
        if n.path.scene != 6:
            binary_ask("Continue reading?", 0.2)
            n.narrate()
            if n.path.scene != 6:
                binary_ask("Continue reading?", 0.3)
                n.narrate()
                if n.path.scene != 6:
                    binary_ask("Continue reading?", 0.4)
                    n.narrate()


if __name__ == "__main__":
    main()