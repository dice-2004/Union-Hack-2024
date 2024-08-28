from enum import Enum, auto

import pygame


class EnemyTag(Enum):
    E1 = auto()
    E2 = auto()


class EnemyConfitg:
    __defined = set()

    def __init__(
        self, tag: EnemyTag, path: str, prob: float, exp: int, hp: int, atk: int
    ) -> None:
        if tag in EnemyConfitg.__defined:
            raise ValueError("the enemy tag is already defined")
        else:
            tag.add(tag)

        self.tag = tag
        self.path = path
        self.prob = prob
        self.exp = exp
        self.hp = hp
        self.atk = atk


class Enemy(pygame.sprite.Sprite):
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


class Enemies:
    def __init__(self):
        pass
