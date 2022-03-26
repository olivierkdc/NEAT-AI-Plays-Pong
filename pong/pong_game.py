import pygame
from .player import Player
from .ball import Ball
pygame.init()


class Game_Info: 
    def __init__(self, p1_hits, p2_hits, p1_score, p2_score, rally):
        self.p1_hits = p1_hits
        self.p2_hits = p2_hits
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.rally = rally

class Game:

    '''COLORS'''
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    '''FONTS'''
    POINT_FONT = pygame.font.SysFont("Segoe UI", 26)
    ROUND_START_FONT = pygame.font.SysFont("Segoe UI", 50)

    def __init__(self, window, winWidth, winHeight):
        '''Score Initiation'''
        self.p1_hits = 0
        self.p2_hits = 0
        self.p1_score = 0
        self.p2_score = 0
        self.rally = 0

        '''Window Initiation'''
        self.window = window
        self.winWidth = winWidth
        self.winHeight = winHeight

        '''Player and Ball Initiation'''
        self.player1 = Player(10, self.winHeight // 2 - Player.HEIGHT // 2)
        self.player2 = Player(self.winWidth - 10 - Player.WIDTH, self.winHeight // 2 - Player.HEIGHT // 2)
        self.ball = Ball(self.winWidth // 2, self.winHeight // 2)

    def _draw_middle(self):
        pygame.draw.rect(self.window, self.WHITE, (self.winWidth//2 - 2, 0, 4, self.winHeight))

    def _draw_score(self):
        p1_score_text = self.POINT_FONT.render(f"{self.p1_score}", 1, self.WHITE)
        p2_score_text = self.POINT_FONT.render(f"{self.p2_score}", 1, self.WHITE)
        self.window.blit(p1_score_text, (self.winWidth // 4 - p1_score_text.get_width()//2, 20))
        self.window.blit(p2_score_text, (self.winWidth * (3/4) - p2_score_text.get_width()//2, 20))

    def _draw_rally(self):
        rally_text = self.POINT_FONT.render(f"{self.rally}", 1, self.WHITE)
        self.window.blit(rally_text, (self.winWidth // 2 - rally_text.get_width() // 2, 10))

    def _draw_total_hits(self):
        total_hits_text = self.POINT_FONT.render(f"{self.p1_hits + self.p2_hits}", 1, self.WHITE)
        self.window.blit(total_hits_text, (self.winWidth // 2 - total_hits_text.get_width() // 2, 10))
    
    def _ball_collision(self):
        ball = self.ball
        player1 = self.player1
        player2 = self.player2

        '''Vertical collisions (ceiling/floor of window)'''
        if ball.y + ball.R >= self.winHeight:
            ball.dy *= -1
        elif ball.y - ball.R <= 0:
            ball.dy *= -1

        '''player collisions:'''
        # ball is going to the left (towards player1)
        if ball.dx < 0: # verify ball is going left (towards player1)    
            if ball.y >= player1.y and ball.y <= player1.y + player1.HEIGHT:
                if ball.x - ball.R <= player1.x + player1.WIDTH:
                    ball.dx *= -1

                    # determine ball.dy based on collision position on player1:  
                    player_middle = player1.y + player1.HEIGHT//2
                    height_differential = player_middle - ball.y
                    reduct = (player1.HEIGHT //2 ) / ball.VELOCITY
                    ball.dy = -height_differential / reduct
                    self.p1_hits += 1
                    self.rally += 1

        # ball is going right (towards player2)        
        else: 
            if ball.y >= player2.y and ball.y <= player2.y + player2.HEIGHT:
                if ball.x + ball.R >= player2.x:
                    ball.dx *= -1

                    # determine ball.dy based on collision position on player2:
                    player_middle = player2.y + player2.HEIGHT//2
                    height_differential = player_middle - ball.y
                    reduct = (player2.HEIGHT //2 ) / ball.VELOCITY
                    ball.dy = -height_differential / reduct
                    self.p2_hits += 1
                    self.rally += 1

    # Draw game window (default show score, not rally)
    def draw(self, draw_score = True, draw_rally = False, draw_total_hits = False):
        #fill window black and draw middle
        self.window.fill(self.BLACK)
        self._draw_middle()

        #Boolean flips for score and rally texts
        if draw_score == True:
            self._draw_score()
        if draw_rally == True:
            self._draw_rally()
        if draw_total_hits == True:
            self._draw_total_hits()

        #Draw player1 and player2
        for player in [self.player1, self.player2]:
            player.draw(self.window)
        #Draw ball
        self.ball.draw(self.window)

    def player_movement(self, left=True, up=True):

        if left:
            if up and self.player1.y - Player.VEL < 0:
                return False
            if not up and self.player1.y + Player.HEIGHT > self.winHeight:
                return False
            self.player1.move(up)
        else:
            if up and self.player2.y - Player.VEL < 0:
                return False
            if not up and self.player2.y + Player.HEIGHT > self.winHeight:
                return False
            self.player2.move(up)

        return True

    def loop(self):
        """
        Executes a single game loop.

        :returns: GameInformation instance stating score 
                  and hits of each paddle.
        """
        self.ball.move()
        self._ball_collision()

        if self.ball.x < 0:
            self.ball.initialize()
            self.p2_score += 1
            self.rally = 0
        elif self.ball.x > self.winWidth:
            self.ball.initialize()
            self.p1_score += 1
            self.rally = 0 


        game_info = Game_Info(
            self.p1_hits, self.p2_hits, self.p1_score, self.p2_score, self.rally)

        return game_info

    def reset(self):
        """Resets the entire game."""
        self.ball.initialize()
        self.player1.initialize()
        self.player2.initialize()
        self.p1_score = 0
        self.p2_score = 0
        self.p1_hits = 0
        self.p2_hits = 0