import random
from enum import Enum, auto
from typing import List

import pygame

import tile


class EnemyTag(Enum):
    E1 = auto()
    E2 = auto()


class EnemyConfitg:
    __defined = set()

    def __init__(self, tag: EnemyTag, path: str, prob: float) -> None:
        if tag in EnemyConfitg.__defined:
            raise ValueError("the enemy tag is already defined")
        else:
            EnemyConfitg.__defined.add(tag)

        self.tag = tag
        self.path = path
        self.prob = prob

        # レベルをもとに自動計算予定
        # self.exp = exp
        # self.hp = hp
        # self.atk = atk


class Enemy(pygame.sprite.Sprite):
    def __init__(self, cfg: EnemyConfitg, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        print(cfg.path)
        self.image = pygame.image.load(cfg.path).convert_alpha()
        self.rect = self.image.get_rect()
        print((x, y))
        self.rect.topleft = (x, y)
        self.direction = 0

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Enemies:
    def __init__(self, tiles: tile.Tiles, cfgs: List[EnemyConfitg]):
        self.enemies: List[Enemy] = []
        probs = []

        for i in range(len(cfgs)):
            prob = 0
            for cfg in cfgs[0 : i + 1]:
                prob += cfg.prob
            probs.append(prob)

        # print(probs[len(probs) - 1])

        for tile_index in range(tiles.num):
            if tiles.effects[tile_index] == tile.TileEffect.Battle:
                seed = random.uniform(0, probs[len(probs) - 1])
                for j in range(len(probs)):
                    if seed <= probs[j]:
                        self.enemies.append(
                            Enemy(cfgs[j], *tiles.convert_pos(tile_index))
                        )
                        break

    def draw(self, screen):
        for enem in self.enemies:
            enem.draw(screen)


default_enemycfgs = [
    EnemyConfitg(
        EnemyTag.E1,
        "./asset/e1.png",
        0.1,
    ),
    EnemyConfitg(
        EnemyTag.E2,
        "./asset/e2.png",
        0.1,
    ),
]
