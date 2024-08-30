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

    def __init__(
        self, tag: EnemyTag, path: str, prob: float, exp: int, hp: int, atk: int
    ) -> None:
        if tag in EnemyConfitg.__defined:
            raise ValueError("the enemy tag is already defined")
        else:
            EnemyConfitg.__defined.add(tag)

        self.tag = tag
        self.path = path
        self.prob = prob

        # レベルをもとに補正予定
        self.expbase = exp
        self.hpbase = hp
        self.atkbase = atk


class Enemy(pygame.sprite.Sprite):
    def __init__(self, cfg: EnemyConfitg, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        print(cfg.path)
        self.image = pygame.image.load(cfg.path).convert_alpha()
        self.rect = self.image.get_rect()
        print((x, y))
        self.rect.topleft = (x, y)
        self.direction = 0
        self.lv = 1
        self.cfg = cfg
        self.update()

    def update(self):
        self.exp = int(self.cfg.expbase * (self.lv * self.lv * 0.2))
        self.hp = int(self.cfg.hpbase * (self.lv * self.lv * 0.2))
        self.atk = int(self.cfg.atkbase * (self.lv * self.lv * 0.2))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Enemies:
    def __init__(self, tiles: tile.Tiles, cfgs: List[EnemyConfitg]):
        self.enemies: dict[int:Enemy] = {}
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
                        self.enemies[tile_index] = Enemy(
                            cfgs[j], *tiles.convert_pos(tile_index)
                        )
                        break

    def draw(self, screen):
        for key in self.enemies.keys():
            self.enemies[key].draw(screen)

    def savefmt(self):
        res = {}
        for key in self.enemies.keys():
            res[f"{key}"] = [self.enemies[key].lv, self.enemies[key].cfg.tag.value]
        return res

    def loadfmt(self, load, tiles: tile.Tiles):
        self.enemies = {}
        for key in load.keys():
            match load[key][1]:
                case 1:
                    cfg = ENEMY_CFGS[1]
                case 2:
                    cfg = ENEMY_CFGS[2]
            self.enemies[int(key)] = Enemy(cfg, *tiles.convert_pos(key))


ENEMY_CFGS = [
    EnemyConfitg(EnemyTag.E1, "./asset/enemy.png", 0.1, 20, 25, 5),
    # EnemyConfitg(EnemyTag.E2, "./asset/e2.png", 0.1, 20, 10, 20),
]
