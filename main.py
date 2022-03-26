import pygame
from pong import Game


width, height = 800, 500
window = pygame.display.set_mode((width,height))

my_game = Game(window, width, height)

run = True
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    my_game.loop()
    my_game.draw(True, True, False)
    pygame.display.update()

pygame.quit()