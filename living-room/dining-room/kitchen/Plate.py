import os
import sys
import inventory

from inventory import items
from inventory import FixtureSpec

class Plate(FixtureSpec):

  def __init__(self):
    super().__init__()

  def use(self):
    ingredients = {
      "Tomato": 1,
      "Lettuce": 1,
      "Toast": 2
    }
    complete = True
    for item in ingredients:
      try:
        if ingredients[item] > items.list[item]["quantity"]: raise
      except:
        print(f"It looks like you're missing some {item}!")
        complete = False
    if complete:
      print("🥪🥪🥪  SANDWICH ACHIEVED! 🥪🥪🥪")
      for item in ingredients:
        used = ingredients[item] * -1
        inventory.list.remove(item, used)
      os.rename("Plate.py", "Sandwich.py")

def main():
  obj = Plate()
  obj.use()

if __name__ == "__main__":
  if sys.argv[0] == "Sandwich.py":
    print("🥪🥪🥪 NOM 🥪🥪 NOM 🥪 NOM")
    os.rename("Sandwich.py", "Plate.py")
    exit()
  main()