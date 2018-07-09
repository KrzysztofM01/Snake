import pygame
import random
import variables

class snack():
    def __init__(self):
        self.snack = None

    def new_snack(self, snake):
        loop_break = True
        while loop_break:
            random_x = variables.size * random.randint(0, variables.screenWidth/variables.size-1)
            random_y = variables.size * random.randint(0, variables.screenHeight/variables.size-1)
            loop_break = False
            for i in range(0, len(snake)):
                if random_x == snake[i][0] or random_y == snake[i][1]:
                    loop_break = True
                    break
        self.snack = [random_x, random_y]

    def draw(self, display, color):
        pygame.draw.rect(display, color, [self.snack[0]+2, self.snack[1]+2, variables.size-2, variables.size-2])