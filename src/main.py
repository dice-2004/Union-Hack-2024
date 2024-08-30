import sys

import pygame

from pygame.locals import K_SPACE, KEYDOWN, QUIT, K_r, Rect
import json

import battle
import enemy
import player
import reborn
import roulette
import tile
from game_title import Title

SCR_RECT = Rect(0, 0, 800, 600)

CAPTION = "test"
SAVEFILE = "files/savedata.json"
ERRORLOG = "files/error.log"


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(CAPTION)  # 画面上部に表示するタイトルを設定
        self.screen = pygame.display.set_mode(SCR_RECT.size)

    def make_tiles(self, name, x: int, y: int, pe1: float, name1: str):
        self.tile_effect = []
        self.tileseed = tile.Tiles.genseed(48, (550, 500))
        self.tiles = tile.Tiles(
            name, 48, x, y, self.tileseed, self.tile_effect, pe1, name1
        )

        # for debug
        print(self.tile_effect)

    def make_roulette(self):
        self.roulette = roulette.Roulette(
            "./asset/roulette_000.png", 550, 5, "./asset/roulette_001.png", 550, 0
        )

    def make_player(self, name, x, y):
        self.player = player.Player(name, x, y)

    def make_battle(self, name):
        self.battle = battle.Battle(name, 200, 200)

    def make_enemy(self):
        self.enemies = enemy.Enemies(self.tiles, enemy.default_enemycfgs)

    def make_statusview(self):
        self.statusview = player.StatusView(self.player, 10, 10)

    def make_reborn(self, name: str, x: int, y: int):
        self.is_dead = False
        self.reborn = reborn.Reborn(name, x, y)

    def next(self):
        x = self.roulette.run(self.screen)

        # for debug
        print(x)

        next_tile = (self.player.nowtile + x) % self.tiles.num
        self.player.move(*self.tiles.convert_pos(next_tile))
        self.player.nowtile = next_tile

        match self.tile_effect[self.player.nowtile]:
            case tile.TileEffect.Basic:
                pass
            case tile.TileEffect.Battle:
                print("battle")
                self.is_dead = not self.battle.jamp(
                    self.screen, self.player, self.enemies.enemies[self.player.nowtile]
                )

    def reborngame(self):
        self.is_dead = False
        self.player.reborn()
        self.make_enemy()
        self.make_tiles(
            "./asset/tile_basic.png",
            0,
            100,
            0.5,
            "./asset/tile_battle.png",
        )

    def draw(self):
        self.screen.fill((0, 0, 0))
        if not self.is_dead:
            self.tiles.draw(self.screen)
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
        elif self.is_dead:
            self.reborn.draw(self.screen)
        self.statusview.draw(self.screen)
        self.roulette.draw(self.screen)

        pygame.display.update()  # 画面を更新

    def update(self):
        self.statusview.update(self.player)
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if not self.is_dead:
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.next()
            elif self.is_dead:
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.reborngame()

    @staticmethod
    def FILE_OPE(func):
        def wapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except IOError as e:
                with open(ERRORLOG, "a", encoding="UTF-8") as f:
                    f.write(e)
                return 1

            except json.JSONDecodeError as e:
                with open(ERRORLOG, "a", encoding="UTF-8") as f:
                    f.write(e)
                return 1

            except Exception as e:
                with open(ERRORLOG, "a", encoding="UTF-8") as f:
                    f.write(e)
                return 1

        return wapper

    # 正常終了 -> 0 異常終了 -> 1
    @FILE_OPE
    def save(self):
        XXX = 000
        # プレイヤーレベル・周回回数・転生回数・シード値
        data = {"level": XXX, "lap": XXX, "reincarnation": XXX, "seed": XXX}
        with open(SAVEFILE, "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4)
        return 0

    @FILE_OPE
    def load(self):
        with open(SAVEFILE, "r", encoding="UTF-8") as f:
            data = json.loads(f.read())
            print(data)
        return 0


def main():
    simple = 0
    title = Title()
    game = Game()
    game.make_tiles(
        "./asset/tile_basic.png",
        0,
        100,
        0.5,
        "./asset/tile_battle.png",
    )
    game.make_roulette()
    game.make_player("./asset/pl.png", 0, 100)
    game.make_battle("./asset/battle.png")
    game.make_enemy()
    game.make_statusview()
    game.make_reborn("./asset/reborn.png", 0, 100)

    title = Title()
    while 1:
        if title.pushed_enter == 1:
            title.draw()
            title.update()

        if title.pushed_enter == 0:
            if title.select == 0:
                game.draw()
                game.update()
            elif title.select == 1:
                if simple == 0:
                    game.load()
                    simple = 1

                game.draw()
                game.update()
            else:
                # 終わる
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
