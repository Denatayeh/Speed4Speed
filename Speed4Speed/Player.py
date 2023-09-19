# imports
import pygame
from pygame import K_LEFT, K_RIGHT, K_s, K_SPACE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/Player.png"), (53, 96))
        # players image
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(400, 530))
        # player's surface and rectangle

    def move(self, SPEED, SCREEN_WIDTH, SCORE, ):
        # function to move player according to pressed keys returns score as it is because a function of the super class
        # is used  for enemy class and player class , where enemy needs to return this parameter , you can ask me to
        # explain this point if it doesn't make sense in comments :)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_s]:
            pygame.mixer.Sound('audio/horn.wav').play()  # using horn

        if pressed_keys[K_SPACE]:
            return SCORE


        if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0) # moving left without getting out of road boundaries

        if pressed_keys[K_RIGHT]: # moving right without getting out of road boundaries
                self.rect.move_ip(5, 0)
        return SCORE
