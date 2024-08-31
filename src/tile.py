import copy
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
        image = pygame.image.load(name).convert_alpha()
        self.image = pygame.transform.scale_by(image, 1.5)
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

        if len(elist) == 0:
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
        else:
            for i in range(self.num):
                if elist[i] == TileEffect.Basic:
                    self.tiles.append(Tile(name0, self.xs[i], self.ys[i]))
                    self.effects.append(TileEffect.Basic)
                else:
                    self.tiles.append(Tile(name1, self.xs[i], self.ys[i]))
                    self.effects.append(TileEffect.Battle)

    # TODO pe1の処理

    def draw(self, screen):
        for i in range(self.num):
            self.tiles[i].draw(screen)

    def convert_pos(self, n: int) -> tuple[int, int]:
        return (self.xs[n], self.ys[n])

    def genseed(tilesize: int, area: tuple[int, int]) -> str:
        x, y = area

        res = "d2"
        res_rev = ""
        posx = 2
        posy = 2
        prev = "d"

        while posx + 2 < x // tilesize and posy + 2 < y // tilesize:
            if prev == "d":
                n = max((random.randint(1, (x // tilesize - posx) // 2), 2))
                posx += n
                prev = "r"
                res += f"r{n}"
                res_rev = f"l{n}" + res_rev
            else:
                n = max((random.randint(1, (y // tilesize - posy) // 2), 2))
                posy += n
                prev = "d"
                res += f"d{n}"
                res_rev = f"u{n}" + res_rev
            print(f"{posx=}{posy=}")

        # if posx + 1 < x // tilesize:
        #     res += f"r{}"

        if prev == "r":
            res_rev = res_rev[2:] + res_rev[0:2]
        res += "r2u2" + res_rev + "l1"

        print(f"{res=}")
        return res

    def loadfmt(load: dict) -> list:
        elist = []
        for i in range(50):
            if f"{i}" not in load:
                elist.append(TileEffect.Basic)
            else:
                elist.append(TileEffect.Battle)
        return elist
