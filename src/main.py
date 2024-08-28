import sys

import pygame
from pygame.locals import K_SPACE, KEYDOWN, QUIT, Rect

import battle
import enemy
import player
import roulette
import tile

SCR_RECT = Rect(0, 0, 640, 480)
SCREEN_SIZE = (400, 300)
CAPTION = "test"


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            SCREEN_SIZE
        )  # 400 x 300の大きさの画面を作る
        pygame.display.set_caption(CAPTION)  # 画面上部に表示するタイトルを設定
        self.screen = pygame.display.set_mode(SCR_RECT.size)

    def make_tiles(self, name, x: int, y: int, procs: str, pe1: float, name1: str):
        self.tile_effect = []
        self.tiles = tile.Tiles(name, 32, x, y, procs, self.tile_effect, pe1, name1)

        # for debug
        print(self.tile_effect)

    def make_roulette(self):
        self.roulette = roulette.Roulette()

    def make_player(self, name):
        self.player = player.Player(name, 0, 0)

    def make_battle(self, name):
        self.battle = battle.Battle(name, 200, 200)

    def make_enemy(self):
        self.enemies = enemy.Enemies(self.tiles, enemy.default_enemycfgs)

    def make_statusview(self):
        self.statusview = player.StatusView(self.player, 300, 300)

    def next(self):
        x = self.roulette.run()

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
                self.battle.jamp(
                    self.screen, self.player, self.enemies.enemies[self.player.nowtile]
                )

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tiles.draw(self.screen)
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        self.statusview.draw(self.screen)

        pygame.display.update()  # 画面を更新

    def update(self):
        self.statusview.update(self.player)
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.next()


def main():
    game = Game()
    game.make_tiles(
        "./asset/tile_basic.png", 0, 0, tile.test_proc, 0.5, "./asset/tile_battle.png"
    )
    game.make_roulette()
    game.make_player("./asset/pl.png")
    game.make_battle("./asset/battle.png")
    game.make_enemy()
    game.make_statusview()

    while 1:
        game.draw()
        game.update()


if __name__ == "__main__":
    main()
