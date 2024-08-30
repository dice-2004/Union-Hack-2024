import random
import time

import pygame


class Roulette(pygame.sprite.Sprite):
    def __init__(self, rltname: str, xr: int, yr: int, backname: str, xb: int, yb: int):
        pygame.sprite.Sprite.__init__(self)
        self.imagerltbase = pygame.image.load(rltname).convert_alpha()
        self.rectrlt = self.imagerltbase.get_rect()
        self.rectrlt.topleft = (xr, yr)
        self.xr, self.yr = self.rectrlt.center
        self.rotate(28)
        self.ang = 28

        self.imagebak = pygame.image.load(backname).convert_alpha()
        self.rectbak = self.imagerlt.get_rect()
        self.rectbak.topleft = (xb, yb)

    def draw(self, screen):
        screen.blit(self.imagebak, self.rectbak)
        screen.blit(self.imagerlt, self.rectrlt)
        pygame.display.update()  # 画面を更新

    def run(self, screen) -> int:
        r = random.randrange(1, 5)
        now = self.ang // 45 + 1
        times = r - now + 8
        for _ in range(times):
            time.sleep(0.3)
            self.ang = (45 + self.ang) % 180
            self.rotate(self.ang)
            self.draw(screen)

        return r

    def rotate(self, ang: float):
        self.imagerlt = pygame.transform.rotate(self.imagerltbase, ang)
        self.rectrlt = self.imagerlt.get_rect()
        self.rectrlt.center = (self.xr, self.yr)
