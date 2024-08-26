import pygame
from pygame.locals import *
import sys
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

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tiles.draw(self.screen)

        pygame.display.update()  # 画面を更新

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()


def main():
    game = Game()
    game.make_tiles("./asset/tile_basic.png", 0, 0, tile.test_proc, 0.1)

    while 1:
        game.draw()
        game.update()


if __name__ == "__main__":
    main()
