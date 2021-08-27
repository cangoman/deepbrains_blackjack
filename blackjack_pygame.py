import pygame
import sys

from blackjack_oop import Game, Button

BLACK = (0,0,0)
GREEN = (0,120,10)
WHITE = (255, 255, 255)
WIDTH = 700
HEIGHT = 700



pygame.init()
pygame.display.set_caption('BlackJack')
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
bg_image = pygame.image.load('img/background.jpg')

game = Game() 
deal_button = Button('Deal', (50,50), (150,30), game.deal) 
hit_button = Button('Hit', (50,150), (150,30), game.hit)
stand_button = Button('Stand', (50, 200), (150, 30), game.check_blackjack)


# game.deal() 
game.print()
game_started = False
while True:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if deal_button.isOver():
                if not game_started:
                    deal_button.action()
                    game_started = True
            elif hit_button.isOver():
                hit_button.action()
            elif stand_button.isOver():
                stand_button.action()


            
        
    # Fill screen you bg color
    canvas.fill(GREEN)

    deal_button.draw(canvas)
    hit_button.draw(canvas)
    stand_button.draw(canvas)

    if game_started:
        game.dealer.display(canvas, (300, 100))
        game.player.display(canvas, (300, 400))

    

    # The logic of your game
    # Draws things, moves things etc.

    # 'flip' kind of 'freezing'
    pygame.display.flip()




