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

  def draw_press_key_msg(self):
    press_key_surface = self.BASICFONT.render('Press a key to play.', True, Config.DARKGRAY)
    press_key_rect = press_key_surface.get_rect()
    press_key_rect.topleft = (Config.WINDOW_WIDTH -200, Config.WINDOW_HEIGHT -30)
    self.screen.blit(press_key_surface, press_key_rect)
  
  def draw_grid(self):
    for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY, (x, 0), (x, Config.WINDOW_HEIGHT))

    for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
      pygame.draw.line(self.screen, Config.DARKGRAY, (0, y), (Config.WINDOW_WIDTH, y))

  def draw_worm(self):
    for coord in self.snake.worm_coords:
      x = coord['x'] * Config.CELLSIZE
      y = coord['y'] * Config.CELLSIZE
      worm_segment_rect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
      pygame.draw.rect(self.screen, Config.DARKGREEN, worm_segment_rect)
      worm_inner_segment_rect = pygame.Rect(x+4, y+4, Config.CELLSIZE-8, Config.CELLSIZE-8)
      pygame.draw.rect(self.screen, Config.GREEN, worm_inner_segment_rect)

  def draw_apple(self):
    x = self.apple.x * Config.CELLSIZE
    y = self.apple.y * Config.CELLSIZE
    apple_segment_rect = pygame.Rect(x, y, Config.CELLSIZE, Config.CELLSIZE)
    pygame.draw.rect(self.screen, Config.RED, apple_segment_rect)

  def draw_score(self, score):
    score_surface = self.BASICFONT.render('Score: %s' % (score), True, Config.WHITE)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (Config.WINDOW_WIDTH - 120, 10)
    self.screen.blit(score_surface, score_rect)

  def draw(self):
    self.screen.fill(Config.BG_COLOR)
    self.draw_grid()
    self.draw_worm()
    self.draw_apple()
    self.draw_score(score = len(self.snake.worm_coords) - 3)
    pygame.display.update()
    self.clock.tick(Config.FPS)

  def handle_key_events(self, event):
    if event.key == pygame.K_ESCAPE:
      pygame.quit()
    elif event.key == pygame.K_LEFT and self.snake.direction != self.snake.RIGHT:
      self.snake.direction = self.snake.LEFT
    elif event.key == pygame.K_RIGHT and self.snake.direction != self.snake.LEFT:
      self.snake.direction = self.snake.RIGHT
    elif event.key == pygame.K_UP and self.snake.direction != self.snake.DOWN:
      self.snake.direction = self.snake.UP
    elif event.key == pygame.K_DOWN and self.snake.direction != self.snake.UP:
      self.snake.direction = self.snake.DOWN

  def is_game_over(self):
    if (self.snake.worm_coords[self.snake.HEAD]['x'] == -1 or
       self.snake.worm_coords[self.snake.HEAD]['x'] == Config.CELLWIDTH or
       self.snake.worm_coords[self.snake.HEAD]['y'] == -1 or
       self.snake.worm_coords[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
      return self.reset_game()
    
    for worm_body in self.snake.worm_coords[1:]:
      if (worm_body['x'] == self.snake.worm_coords[self.snake.HEAD]['x'] and
         worm_body['y'] == self.snake.worm_coords[self.snake.HEAD]['y']):
        return self.reset_game()
       
  def reset_game(self):
    del self.snake
    del self.apple
    self.snake = Snake()
    self.apple = Apple()
    return True

  def game_loop(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
        elif event.type == pygame.KEYDOWN:
          self.handle_key_events(event)

      self.snake.update(self.apple)
      self.draw()
      if self.is_game_over():
        break

  def check_for_key_press(self):
    if len(pygame.event.get(pygame.QUIT)) > 0:
      pygame.quit()

    key_up_events = pygame.event.get(pygame.KEYUP)

    if len(key_up_events) == 0:
      return None

    if key_up_events[0].key == pygame.K_ESCAPE:
      pygame.quit()
      quit()

    return key_up_events[0].key

  def display_game_over(self):
    game_over_font = pygame.font.Font('freesansbold.ttf', 150)
    game_surface = game_over_font.render('Game', True, Config.WHITE)
    over_surface = game_over_font.render('Over', True, Config.WHITE)
    game_rect = game_surface.get_rect()
    over_rect = over_surface.get_rect()
    game_rect.midtop = (Config.WINDOW_WIDTH / 2, 10)
    over_rect.midtop = (Config.WINDOW_WIDTH / 2, game_rect.height + 10 + 25)
    self.screen.blit(game_surface, game_rect)
    self.screen.blit(over_surface, over_rect)

    self.draw_press_key_msg()
    pygame.display.update()
    pygame.time.wait(500)

    self.check_for_key_press()

    while True:
      if self.check_for_key_press():
        pygame.event.get()
        return

  def show_start_screen(self):


  def run(self):
    #self.show_start_screen()

    while True:
      self.game_loop()
      self.display_game_over()
    
