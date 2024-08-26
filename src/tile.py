import typing
from enum import Enum
import pygame
from pygame.locals import *


Effect = Enum("Effect", ["None", "Buttle"])

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
    effects: typing.List[Effect] = []
    tiles: typing.List[Tile] = []

    def __init__(
        self, name: str, size: int, x: int, y: int, procs: str, pe1: float
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
            for j in range(int(proc[1])):
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
            self.tiles.append(Tile(name, self.xs[i], self.ys[i]))

    # TODO pe1の処理

    def draw(self, screen):
        for i in range(self.num):
            self.tiles[i].draw(screen)

    def convert_pos(self, n: int) -> tuple[int, int]:
        return (self.xs[n], self.ys[n])
