import random
import typing
from enum import Enum
import pygame
from pygame.locals import *


class Roulette(pygame.sprite.Sprite):
    def run(self) -> int:
        r = random.randrange(1, 4)
        # TODO animation
        return r
