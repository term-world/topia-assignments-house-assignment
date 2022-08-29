import os
import math
import random
import narrator

from narrator.Checkpoint import exists
from inventory import Acquire
from inventory.Item import FixtureSpec
from inventory.Item import Factory

class Toaster(FixtureSpec):

    def __init__(self):
        super().__init__()

    def use(self):
        seed = math.floor(
            random.random() * 10
        )
        if seed > 5:
            print("🍞 ACQUIRED 1 TOAST 🍞")
            Factory("Toast")
            Acquire("Toast.py")
            os.remove("Toast.py")
        else:
            print("The Toaster.py sparks, but otherwise nothing happens. Maybe try running it again?")

def main():
    n = narrator.Narrator()
    n.path.change(10.0)
    n.narrate()

    t = Toaster()
    t.use()

if __name__ == "__main__":
    main()
