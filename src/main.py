import sys

import pygame
from pygame.locals import K_SPACE, KEYDOWN, QUIT, Rect
import json

import battle
import player
import roulette
import tile
from game_title import Title

SCR_RECT = Rect(0, 0, 640, 480)
SCREEN_SIZE = (400, 300)
CAPTION = "test"
SAVEFILE="files/savedata.json"
ERRORLOG="files/error.log"



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
                self.battle.jamp(self.screen)

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
                if event.key == K_SPACE:
                    self.next()

    #正常終了 -> 0 異常終了 -> 1
    def save(self):
        XXX=000

        #プレイヤーレベル・周回回数・転生回数・シード値
        data={"level":XXX,"lap":XXX,"reincarnation":XXX,"seed":XXX}
        try:
            with open(SAVEFILE,"w",encoding="UTF-8") as f:
                json.dump(data,f,indent=4)
            return 0

        except IOError as e:
            with open(ERRORLOG,"a",encoding="UTF-8") as f:
                f.write(e)
            return 1

        except json.JSONDecodeError as e:
            with open(ERRORLOG,"a",encoding="UTF-8") as f:
                f.write(e)
            return 1

        except Exception as e:
            with open(ERRORLOG,"a",encoding="UTF-8") as f:
                f.write(e)
            return 1





def main():
    title=Title()
    game = Game()
    game.make_tiles(
        "./asset/tile_basic.png", 0, 0, tile.test_proc, 0.5, "./asset/tile_battle.png"
    )
    game.make_roulette()
    game.make_player("./asset/pl.png")
    game.make_battle("./asset/battle.png")

    title=Title()
    while 1:
        if title.pushed_enter == 1:
            title.draw()
            title.update()

        if title.pushed_enter == 0:
            if title.select==0:
                game.draw()
                game.update()
            elif title.select==1:
                game.draw()
                game.update()
            else :
                #終わる
                pygame.quit()
                sys.exit()





if __name__ == "__main__":
    main()
