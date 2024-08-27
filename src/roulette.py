import random

import pygame


class Roulette(pygame.sprite.Sprite):
    def run(self) -> int:
        r = random.randrange(1, 4)
        # TODO animation
        return r
