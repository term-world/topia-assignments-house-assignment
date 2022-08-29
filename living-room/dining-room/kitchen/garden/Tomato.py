import sys

from inventory import Acquire
from inventory.Item import ItemSpec

class Tomato(ItemSpec):

  def __init__(self):
    super().__init__(__file__)