import pygame
import variables
import random

class snake():
    def __init__(self):
        self.body = []
        self.score = -1
        self.moveUp = False
        self.moveDown = False
        self.moveRight = False
        self.moveLeft = False
        self.player_exit = False
        self.bodyMove = 0
        self.game_is_on = True

    def new_part(self,x,y):
        self.body.insert(1,[x,y])

    def draw(self, display, color):
        for part in self.body:
            pygame.draw.rect(display, color, [part[0]+2, part[1]+2, variables.size-2, variables.size-2])

    def collision(self, gameobj1, gameobj2):
        if gameobj1[0] == gameobj2[0] and gameobj1[1] == gameobj2[1]:
            return True
        else:
            return False

    def steering(self, event, snackMgr):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.moveLeft == False:
                self.moveUp = False
                self.moveDown = False
                self.moveRight = True
                self.moveLeft = False
            if event.key == pygame.K_LEFT and self.moveRight == False:
                self.moveUp = False
                self.moveDown = False
                self.moveRight = False
                self.moveLeft = True
            if event.key == pygame.K_UP and self.moveDown == False:
                self.moveUp = True
                self.moveDown = False
                self.moveRight = False
                self.moveLeft = False
            if event.key == pygame.K_DOWN and self.moveUp == False:
                self.moveUp = False
                self.moveDown = True
                self.moveRight = False
                self.moveLeft = False
            if event.key == pygame.K_ESCAPE:
                self.player_exit = True
            if event.key == pygame.K_r and self.game_is_on == False:
                self.game_is_on = True
                self.moveUp = False
                self.moveDown = False
                self.moveRight = False
                self.moveLeft = False
                self.score = 0
                self.new_part(variables.size * random.randint(2, variables.screenWidth / variables.size - 2), variables.size * random.randint(2, variables.screenHeight / variables.size - 2))
                snackMgr.new_snack(self.body)

    def clear(self, snack):
        self.body = []
        snack.snack = None

    def update(self, snack):
        if self.bodyMove == 0:
            for i in range(len(self.body), 1, -1):
                self.body[i-1][0] = self.body[i-2][0]
                self.body[i-1][1] = self.body[i-2][1]
        else:
            self.new_part(self.body[0][0], self.body[0][1])
            self.bodyMove -= 1

        if self.body[0][0] < variables.screenWidth+1-variables.size and self.body[0][0] > -1 and self.body[0][1] > -1 and self.body[0][1] < variables.screenHeight+1-variables.size:
            if self.moveDown:
                self.body[0][1] += variables.size
            if self.moveUp:
                self.body[0][1] -= variables.size
            if self.moveRight:
                self.body[0][0] += variables.size
            if self.moveLeft:
                self.body[0][0] -= variables.size
        else:
            self.game_is_on = False

        for i in range(1, len(self.body)):
            if self.collision(self.body[i], self.body[0]):
                self.game_is_on = False
        if self.collision(self.body[0], snack.snack):
            self.bodyMove += variables.body_increase_on_snack
            snack.new_snack(self.body)
            self.score += 1