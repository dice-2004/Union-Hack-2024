import sys

import pygame
import json
import time


from pygame.locals import *


import battle
import enemy
import player
import reborn
import roulette
import sound
import tile
from game_title import Title

width = 250
height = 50
CON = [275, 270, width, height]
SAVE = [CON[0], CON[1] + 75, width, height]
N_SAVE = [SAVE[0], SAVE[1] + 75, width, height]

# COLOR
SELECT = [0, 0, 255]
N_SELECT = [255, 0, 0]
COL = [0, 0, 0]

SCR_RECT = Rect(0, 0, 800, 600)

CAPTION = "test"

SAVEFILE = "files/savedata.json"
ERRORLOG = "files/error.log"
FONT = "font/x12y16pxMaruMonica.ttf"


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(CAPTION)  # 画面上部に表示するタイトルを設定
        self.screen = pygame.display.set_mode(SCR_RECT.size)
        self.pushed_enter = 0
        self.select = 0

    def make_tiles(
        self,
        name,
        x: int,
        y: int,
        pe1: float,
        name1: str,
        seed: str,
        tileefect: list[tile.TileEffect] | dict,
        is_load: int,
    ):
        if is_load == 1:
            self.tileseed = seed
            self.tile_effect = tileefect
            print("prevl ", self.tile_effect)
        else:
            self.tileseed = tile.Tiles.genseed(48, (550, 500))
            self.tile_effect = []
            print("prev ", self.tile_effect)
        self.tiles = tile.Tiles(
            name, 48, x, y, self.tileseed, self.tile_effect, pe1, name1
        )

        # for debug
        print("aaa ", self.tile_effect)

    def make_roulette(self):
        self.roulette = roulette.Roulette(
            "./asset/roulette_000.png", 550, 5, "./asset/roulette_001.png", 550, 0
        )

    def make_player(self, name, x, y, level, rebornnum, is_load):
        self.player = player.Player(name, x, y, level, rebornnum, is_load)

    def make_battle(self, name):
        self.battle = battle.Battle(name, 200, 200)

    def make_enemy(self):
        self.enemies = enemy.Enemies(self.tiles, enemy.ENEMY_CFGS)
        print("call makee enemey", self.enemies.enemies.keys())

    def make_statusview(self):
        self.statusview = player.StatusView(self.player, 10, 10)

    def make_reborn(self, name: str, x: int, y: int):
        self.is_dead = False
        self.reborn = reborn.Reborn(name, x, y)

    def make_sound(self):
        self.sounds = sound.Sounds()
        self.sounds.mainbgm()

    def make_backscreen(self):
        self.backscreen = tile.BackScreen("./asset/backscreen.png", 0, 100)

    def next(self):
        x = self.roulette.run(self.screen, self.sounds)

        # for debug
        print(x)

        for _ in range(x):
            next_tile = (self.player.nowtile + 1) % self.tiles.num
            self.player.move(*self.tiles.convert_pos(next_tile))
            self.player.nowtile = next_tile
            self.draw()
            time.sleep(0.2)
        match self.tile_effect[self.player.nowtile]:
            case tile.TileEffect.Basic:
                pass
            case tile.TileEffect.Battle:
                print("battle")
                self.sounds.play_se_btl()
                self.sounds.se_btl.play()
                self.is_dead = not self.battle.jamp(
                    self.screen, self.player, self.enemies.enemies[self.player.nowtile]
                )

    def reborngame(self):
        self.is_dead = False
        self.player.reborn()
        self.make_tiles(
            "./asset/tile_basic.png",
            0,
            100,
            0.5,
            "./asset/tile_battle.png",
            0,
            0,
            0,
        )
        self.make_enemy()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.backscreen.draw(self.screen)
        if not self.is_dead:
            self.tiles.draw(self.screen)
            self.enemies.draw(self.screen)
            self.player.draw(self.screen)
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
                print("esc")
                self.menu()
            if not self.is_dead:
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.next()
                    elif event.key == K_ESCAPE:
                        print("Esc")
                        self.sounds.se_sel.play()
                        self.menu()
            elif self.is_dead:
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.sounds.se_sel.play()
                        self.reborngame()

    @staticmethod
    def FILE_OPE(func):
        def wapper(*args, **kwargs):
            try:
                data = func(*args, **kwargs)
                return data
            except IOError as e:
                with open(ERRORLOG, "a", encoding="UTF-8") as f:
                    f.write(f"{str(e)}\n")
                return 1, 0, 0

            except json.JSONDecodeError as e:
                with open(ERRORLOG, "a", encoding="UTF-8") as f:
                    f.write(f"{str(e)}\n")
                return 1, 0, 0

            except Exception as e:
                with open(ERRORLOG, "a", encoding="UTF-8") as f:
                    f.write(f"{str(e)}\n")
                return 1, 0, 0

        return wapper

    @FILE_OPE
    def save(self):
        # プレイヤーレベル・周回回数・転生回数・シード値
        data = {
            "Player": {
                "level": self.player.lv,
                "reincarnation": self.player.rebornnum,
                "seed": self.tileseed,
                "exp": self.player.exp,
                "plpos": self.player.nowtile,
            },
            "Enemies": self.enemies.savefmt(),
        }
        print(data)
        with open(SAVEFILE, "w", encoding="UTF-8") as f:
            print("save")
            json.dump(data, f, indent=4)

        return 0

    @FILE_OPE
    def load(self):
        with open(SAVEFILE, "r", encoding="UTF-8") as f:
            data = json.loads(f.read())

            print(type(data["Player"]["seed"]))
            return (
                data["Player"]["level"],
                data["Player"]["reincarnation"],
                data["Player"]["seed"],
                data["Player"]["exp"],
                data["Player"]["plpos"],
                data["Enemies"],
            )

    def menu_select(self):
        rects = [CON, SAVE, N_SAVE]
        colors = [N_SELECT, N_SELECT, N_SELECT]
        txts = ["ゲームをつづける", "セーブして終わる", "セーブせず終わる"]
        if self.select == 0:
            colors[0] = SELECT
        elif self.select == 1:
            colors[1] = SELECT
        elif self.select == 2:
            colors[2] = SELECT

        pygame.draw.rect(self.screen, (255, 255, 255), (100, 100, 600, 400))
        self.draw_text(50, "ポーズメニュー", COL, self.screen, 300, 150)
        for rect, color, txt in zip(rects, colors, txts):
            pygame.draw.rect(self.screen, color, rect)
            self.draw_text(
                25, txt, (255, 255, 255), self.screen, rect[0] + 50, rect[1] + 15
            )
        pygame.display.update()

    def menu_update(self):
        # 画面切り替え
        # 上下、enter
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_KP8:
                    print("up_M")
                    if self.select != 0:
                        self.select -= 1
                        self.sounds.play_se_cur()
                elif event.key == K_DOWN or event.key == K_KP2:
                    print("dwn_M")
                    if self.select != 2:
                        self.select += 1
                        self.sounds.play_se_cur()
                elif event.key == K_KP_ENTER or event.key == K_RETURN:
                    print("ent_M")
                    self.pushed_enter = 1
                    self.sounds.play_se_sel()

    def draw_text(self, siz, txt, col, sc, x, y):
        fnt = pygame.font.Font(FONT, siz)
        sur = fnt.render(txt, True, col)
        self.screen.blit(sur, [x, y])

    def menu(self):
        while 1:
            if self.pushed_enter == 0:
                self.menu_select()
                self.menu_update()

            if self.pushed_enter == 1:
                if self.select == 0:
                    self.pushed_enter = 0
                    break
                    pass
                elif self.select == 1:
                    # セーブ終わり
                    self.save()
                    pygame.quit()
                    sys.exit()
                else:
                    # セーブせず終わり
                    pygame.quit()
                    sys.exit()


def main():
    simple = 0
    title = Title()
    game = Game()
    game.make_roulette()
    game.make_battle("./asset/battle.png")
    game.make_reborn("./asset/reborn.png", 0, 100)
    game.make_sound()
    game.make_backscreen()
    while 1:
        if title.pushed_enter == 0:
            title.draw()
            title.update()

        if title.pushed_enter == 1:
            if title.select == 0:
                if simple == 0:
                    game.make_tiles(
                        "./asset/tile_basic.png",
                        0,
                        100,
                        0.5,
                        "./asset/tile_battle.png",
                        0,
                        0,
                        0,
                    )
                    game.make_enemy()
                    game.make_player("./asset/pl.png", 0, 100, 0, 0, 0)
                    game.make_statusview()
                    simple = 1
                game.draw()
                game.update()
            elif title.select == 1:
                if simple == 0:
                    level, reburn, seed, exp, plpos, tileeff = game.load()
                    print(type(seed), tileeff)
                    game.make_tiles(
                        "./asset/tile_basic.png",
                        0,
                        100,
                        0.5,
                        "./asset/tile_battle.png",
                        seed,
                        tile.Tiles.loadfmt(tileeff),
                        1,
                    )
                    game.make_enemy()
                    game.enemies.loadfmt(tileeff, game.tiles)
                    game.make_player("./asset/pl.png", 0, 100, level, reburn, 1)
                    game.player.exp = exp
                    game.player.move(*game.tiles.convert_pos(plpos))
                    game.player.nowtile = plpos
                    game.make_statusview()
                    simple = 1

                game.draw()
                game.update()
            else:
                # 終わる
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
