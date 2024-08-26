import sys
import time

import pygame
from pygame.locals import K_LEFT, KEYDOWN, QUIT, Rect

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

    def make_tiles(self, name, x: int, y: int, procs: str, pe1: float):
        self.tiles = tile.Tiles(name, 32, x, y, procs, pe1)

    def make_roulette(self):
        self.roulette = roulette.Roulette()

    def make_player(self, name):
        self.player = player.Player(name, 0, 0)

    def next(self):
        x = self.roulette.run()

        # for debug
        print(x)

        self.player.move(
            *self.tiles.convert_pos((self.player.nowtile + x) % self.tiles.num)
        )
        self.player.nowtile += x

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tiles.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.update()  # 画面を更新

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.next()
                    time.sleep(1)


def main():
    game = Game()
    game.make_tiles("./asset/tile_basic.png", 0, 0, tile.test_proc, 0.1)
    game.make_roulette()
    game.make_player("./asset/pl.png")

    while 1:
        game.draw()
        game.update()


if __name__ == "__main__":
    main()
