import random
import typing
from enum import Enum, auto

import pygame

# from pygame.locals import Rect


class TileEffect(Enum):
    Basic = auto()
    Battle = auto()


test_proc = "d4r6u4l5"


class Tile(pygame.sprite.Sprite):
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


class Tiles:
    size: int = 0
    num: int = 0
    xs: typing.List[int] = []
    ys: typing.List[int] = []
    effects: typing.List[TileEffect] = []
    tiles: typing.List[Tile] = []

    def __init__(
        self,
        name0: str,
        size: int,
        x: int,
        y: int,
        procs: str,
        elist: list[TileEffect],
        pe1: float,
        name1: str,
    ) -> None:
        """
        size: TileSize 廃止したい
        origin: 起点座標
        proc: 起点からのマップ作成手順
        pe1:  preparation of effect 1
        """

        # TODO バリデーション
        self.size = size
        self.num = 1
        self.xs.append(x)
        self.ys.append(y)

        for i in range(0, len(procs), 2):
            proc = procs[i : i + 2]
            # print(len(procs) // 2)
            # print(proc)
            for _ in range(int(proc[1])):
                match proc[0]:
                    case "u":
                        y -= self.size  # 画面と逆なため
                    case "d":
                        y += self.size
                    case "r":
                        x += self.size
                    case "l":
                        x -= self.size
                self.xs.append(x)
                self.ys.append(y)
                self.num += 1

        for i in range(self.num):
            seed = random.uniform(0, 1 + pe1)
            if seed <= 1:
                self.tiles.append(Tile(name0, self.xs[i], self.ys[i]))
                elist.append(TileEffect.Basic)
                self.effects.append(TileEffect.Basic)
            elif seed <= 1 + pe1:
                self.tiles.append(Tile(name1, self.xs[i], self.ys[i]))
                elist.append(TileEffect.Battle)
                self.effects.append(TileEffect.Battle)

    # TODO pe1の処理

    def draw(self, screen):
        for i in range(self.num):
            self.tiles[i].draw(screen)

    def convert_pos(self, n: int) -> tuple[int, int]:
        return (self.xs[n], self.ys[n])