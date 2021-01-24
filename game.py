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

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
      self.screen.fill((255, 255, 255))
      pygame.display.update()
      self.clock.tick(60)

    
