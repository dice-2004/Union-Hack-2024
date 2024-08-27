import sys
import time

import pygame
from pygame.locals import KEYDOWN, QUIT, K_a, K_d


class Battle(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = 0

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def jamp(self, screen):
        basetime = time.time()
        while basetime + 10 > time.time():
            self.draw(screen)
            pygame.display.update()  # 画面を更新
            for event in pygame.event.get():
                if event.type == QUIT:  # 閉じるボタンが押されたら終了
                    pygame.quit()  # Pygameの終了(画面閉じられる)
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        print("escape")
                        return
                    elif event.key == K_d:
                        print("attack")
                        return
        print("timeout-battle")
        return
