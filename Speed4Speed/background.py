import pygame

class Background():
    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        self.bgimage=pygame.transform.scale(pygame.image.load('images/Background.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rectBGimg = self.bgimage.get_rect()
        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = self.rectBGimg.height
        self.bgX2 = 0

        self.moving_speed = 5

        # defining background with initial coordinates

    def update(self):    # updating background so it loops continuously
        self.bgY1 -= self.moving_speed
        self.bgY2 -= self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height

    def render(self,DISPLAYSURF): #updating the background
        DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
        DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))

