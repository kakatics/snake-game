import pygame, sys

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
CLOCK = pygame.time.Clock()
pygame.display.set_caption('Wormy')

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  DISPLAYSURF.fill((255, 255, 255))
  pygame.display.update()
  CLOCK.tick(60)
