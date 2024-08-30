import random
import time

import pygame


class Roulette(pygame.sprite.Sprite):
    def __init__(self, rltname: str, xr: int, yr: int, backname: str, xb: int, yb: int):
        pygame.sprite.Sprite.__init__(self)
        self.imagerlt = pygame.image.load(rltname).convert_alpha()
        self.rectrlt = self.imagerlt.get_rect()
        self.rectrlt.topleft = (xr, yr)
        self.xr, self.yr = self.rectrlt.center
        self.imagerlt = pygame.transform.rotate(self.imagerlt, 28)
        self.rectrlt = self.imagerlt.get_rect()
        self.rectrlt.center = (self.xr, self.yr)

        self.imagebak = pygame.image.load(backname).convert_alpha()
        self.rectbak = self.imagerlt.get_rect()
        self.rectbak.topleft = (xb, yb)

    def draw(self, screen):
        screen.blit(self.imagebak, self.rectbak)
        screen.blit(self.imagerlt, self.rectrlt)

    def run(self, screen) -> int:
        r = random.randrange(1, 5)

        for _ in range(r):
            time.sleep(0.5)
            self.imagerlt = pygame.transform.rotate(self.imagerlt, 45)
            self.rectrlt = self.imagerlt.get_rect()
            self.rectrlt.center = (self.xr, self.yr)
            self.draw(screen)

        return r
