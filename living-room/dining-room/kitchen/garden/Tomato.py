import sys

from inventory import Acquire
from inventory.Item import ItemSpec

class Tomato(ItemSpec):

  def __init__(self):
    super().__init__(__file__)

def main():
  Acquire(sys.argv[0])
  print("You acquired a bright red tomato! 🍅")

if __name__ == "__main__":
  main()