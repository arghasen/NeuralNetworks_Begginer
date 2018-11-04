import random
from enum import Enum

# add the actions possible in game 
class Action(Enum):
    Add3 = 3
    Add2 = 2
    Add1 = 1
    Sub1 = -1
    Sub2 = -2
    Sub3 = -3

# Basic Game API
class Game():
  def __init__(self):
    self.reset()

  def reset(self):
    self.current_number = random.randrange(1, 12)
    if (self.current_number == 5):
      self.reset()
    self.turns = 0

  def has_lost(self):
    return self.turns >= 3 and self.current_number != 5

  def has_won(self):
    return self.turns <= 3 and self.current_number == 5

  def is_active(self):
    return not self.has_lost() and not self.has_won()

  def play(self, action:Action):

    if (self.turns >=3):
      raise Exception('Max number of turns reached. Call reset.')

    self.turns += 1;
    self.current_number += int(action)

    return self.has_won()

