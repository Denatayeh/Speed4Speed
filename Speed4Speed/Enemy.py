import random
import pygame


class Enemy1(pygame.sprite.Sprite):
    def __init__(self):  # the orange car class attributes
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Enemy_1.png"), (56.4, 101.3))
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(random.randint(293, 475), 100))
        # parameter 100 so it is always below green cars to avoid them overlaping

    def move(self, SPEED, SCREEN_WIDTH, SCORE):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 800:
            SCORE += 10
            self.rect.top = 0
            self.rect.center = (random.randint(293, 475), 0)
        return SCORE
    # function to move entity and updating score


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):  # the green car class attributes
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Enemy_2.png"), (56.4, 101.3))
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(random.randint(280, 518), -150))

    def move(self, SPEED, SCREEN_WIDTH, SCORE):  # function overloaded between entities inheriting the same sprite class
        # function to move entity and updating score
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 800:
            SCORE += 10
            self.rect.top = 0
            self.rect.center = (random.randint(280, 518), 0)
        return SCORE
