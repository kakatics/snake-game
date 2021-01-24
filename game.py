from config import Config
from snake import Snake
from apple import Apple
import pygame, sys

class Game(object):
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
    self.clock = pygame.time.Clock()
    self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')
    self.apple = Apple()
    self.snake = Snake()
  
  def draw_grid(self):
    for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY, (x, 0), (x, Config.WINDOW_HEIGHT))

    for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY, (0, y), (Config.WINDOW_WIDTH, y))

  def draw(self):
    self.screen.fill(Config.BG_COLOR)
    self.draw_grid()
    pygame.display.update()
    self.clock.tick(Config.FPS)

  def handle_key_events(self, event):
    if event.key == pygame.K_ESCAPE:
      pygame.quit()

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          self.handle_key_events(event)

      #self.snake.update(self.apple)
      self.draw()
      #if self.is_game_over():
       # break
    
