from turtle import left
import pygame
from pong import Game

class PongGame:
    def __init__(self, window, width, height):
        self.game = Game(window,width,height)
        self.player1 = self.game.player1
        self.player2 = self.game.player2
        self.ball = self.game.ball

    def AI_test(self):
        run = True
        clock = pygame.time.Clock()
        FPS = 60
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            '''Allow for player input'''
            keys_pressed = pygame.key.get_pressed()
            #player 1
            if keys_pressed[pygame.K_w]:
                my_game.player_movement(left = True, up = True)
            if keys_pressed[pygame.K_s]:
                my_game.player_movement(left = True, up = False)
            #player 2
            if keys_pressed[pygame.K_UP]:
                my_game.player_movement(left = False, up = True)
            if keys_pressed[pygame.K_DOWN]:
                my_game.player_movement(left = False, up = False)


            my_game.loop()
            my_game.draw(True, True, False)
            pygame.display.update()

        pygame.quit()

# width, height = 800, 500
# window = pygame.display.set_mode((width,height))
# my_game = Game(window, width, height)



# run = True
# clock = pygame.time.Clock()
# FPS = 60
# while run:
#     clock.tick(FPS)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#             break

#     '''Allow for player input'''
#     keys_pressed = pygame.key.get_pressed()
#     #player 1
#     if keys_pressed[pygame.K_w]:
#         my_game.player_movement(left = True, up = True)
#     if keys_pressed[pygame.K_s]:
#         my_game.player_movement(left = True, up = False)
#     #player 2
#     if keys_pressed[pygame.K_UP]:
#         my_game.player_movement(left = False, up = True)
#     if keys_pressed[pygame.K_DOWN]:
#         my_game.player_movement(left = False, up = False)


#     my_game.loop()
#     my_game.draw(True, True, False)
#     pygame.display.update()

# pygame.quit()