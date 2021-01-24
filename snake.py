import random
from config import Config

class Snake(object):
  
  UP = "up"
  DOWN = "down"
  LEFT = "left"
  RIGHT = "right"
  HEAD = 0

  def __init__(self):
    self.x = random.randint(5, Config.CELLWIDTH-6)
    self.y = random.randint(5, Config.CELLHEIGHT-6)
    self.direction = self.RIGHT
    self.worm_coords = [
        {'x': self.x, 'y': self.y},
        {'x': self.x-1, 'y': self.y},
        {'x': self.x-2, 'y': self.y},
        ]

  def update(self, apple):
    if self.worm_coords[self.HEAD]['x'] == apple.x and self.worm_coords[self.HEAD]['y'] == apple.y:
      apple.set_new_location()
    else:
      del self.worm_coords[-1]

    if self.direction == self.UP:
      new_head = {
          'x': self.worm_coords[self.HEAD]['x'],
          'y': self.worm_coords[self.HEAD]['y'] - 1,
          }
    elif self.direction == self.DOWN:
      new_head = {
          'x': self.worm_coords[self.HEAD]['x'],
          'y': self.worm_coords[self.HEAD]['y'] + 1,
          }
    elif self.direction == self.LEFT:
      new_head = {
          'x': self.worm_coords[self.HEAD]['x'] - 1,
          'y': self.worm_coords[self.HEAD]['y'],
          }
    elif self.direction == self.RIGHT:
      new_head = {
          'x': self.worm_coords[self.HEAD]['x'] + 1,
          'y': self.worm_coords[self.HEAD]['y'],
          }

    self.worm_coords.insert(0, new_head)

