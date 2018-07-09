import pygame
from snake import snake
from snack import snack
import time
import random
import variables

# <--- pygame init settings --->
pygame.init()
display = pygame.display.set_mode((variables.screenWidth,variables.screenHeight))
pygame.display.set_caption('Snake')
snakeMgr = snake()
snackMgr = snack()
font = pygame.font.SysFont("monospace", 20)
resetMsg = font.render("Game over - press R to reset", 1, variables.text_color)
# <------>
# <--- Create snake and snack --->
snakeMgr.new_part(variables.size * random.randint(2,variables.screenWidth/variables.size-2),variables.size * random.randint(2,variables.screenHeight/variables.size-2))
snackMgr.new_snack(snakeMgr.body)
# <------>
# <--- Game loop, will execute until player quits the game with ESC key --->
while not snakeMgr.player_exit:

    for event in pygame.event.get():
        snakeMgr.steering(event, snackMgr)

    if snakeMgr.game_is_on:
        snakeMgr.update(snackMgr)
        display.fill(variables.background_color)
        snakeMgr.draw(display, variables.snake_color)
        snackMgr.draw(display, variables.snack_color)
        pygame.display.update()
        time.sleep(variables.game_speed)

    else:
        scoreMsg = font.render("Your score: " + str(snakeMgr.score), 1, variables.text_color)
        snakeMgr.clear(snackMgr)
        display.fill(variables.background_color)
        display.blit(scoreMsg, (variables.screenWidth/4, variables.screenHeight/4))
        display.blit(resetMsg, (variables.screenWidth/4, variables.screenHeight/2))
        pygame.display.update()
# <------>