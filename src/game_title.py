import pygame
import sys
from pygame.locals import *
from random import randint
import time

import sound
from res import resource_path

SCR_RECT = Rect(0, 0, 800, 600)
CAPTION = "test"
FONT = resource_path("font/x12y16pxMaruMonica.ttf")

# SAMPLE=[左上のｘ座標、左上のｙ座標、横幅、縦の幅]
height = 80
width = 200

STA = [20, 270, width, height]
CON = [STA[0] + STA[2] - 140, STA[1] + STA[3] + 10, width, height]
END = [CON[0] + CON[2] - 140, CON[1] + CON[3] + 10, width, height]

# COLOR
SELECT = [0, 0, 255]
N_SELECT = [255, 0, 0]
COL = [255, 255, 255]


class Title:
    def __init__(self):
        pygame.init()  # 400 x 300の大きさの画面を作る
        pygame.display.set_caption(CAPTION)  # 画面上部に表示するタイトルを設定
        Title.screen = pygame.display.set_mode(SCR_RECT.size)

        self.select = 0
        self.pushed_enter = 0
        self.sounds = sound.Sounds()
        self.character = pygame.transform.scale(pygame.image.load(resource_path("asset/plb.png")),(200,200))
        self.enemy = pygame.transform.scale(pygame.image.load(resource_path("asset/enemy.png")),(130,130))
        self.back1 = pygame.transform.scale(pygame.image.load(resource_path("asset/grass1.bmp")),(40,40))
        self.back2 = pygame.transform.scale(pygame.image.load(resource_path("asset/grass2.bmp")),(40,40))
        self.rand = [[randint(1,3) for _ in range(15)] for _ in range(20)]
        self.start = time.time()

        pygame.font.init()

    def draw(self):
        self.pushed_enter = 0
        rects = [STA, CON, END]
        colors = [N_SELECT, N_SELECT, N_SELECT]
        txts = ["はじめる", "続きから", "おわる"]

        if (time.time()-self.start)>2:
            self.rand = [[randint(1,3) for _ in range(15)] for _ in range(20)]
            self.start = time.time()

        if self.select == 0:
            colors[0] = SELECT
        elif self.select == 1:
            colors[1] = SELECT
        elif self.select == 2:
            colors[2] = SELECT


        for x,i in zip(range(0,800,40),range(0,20)):
            for y,j in zip(range(0,600,40),range(0,15)):

                if not(self.rand[i][j]%3==0):
                    self.screen.blit(self.back1,(x,y))
                else:
                    self.screen.blit(self.back2,(x,y))
        txt_posx=300
        txt_posy=30
        pygame.draw.rect(self.screen,(0,0,0),(txt_posx-20,txt_posy,150,110))
        pygame.draw.rect(self.screen,(0,0,0),(txt_posx+60-20,txt_posy+100,220,90))
        self.draw_text(20, "り", COL, self.screen, txt_posx, txt_posy)
        self.draw_text(20, "ん", COL, self.screen, txt_posx+50, txt_posy)
        self.draw_text(20, "ね", COL, self.screen, txt_posx+100, txt_posy)
        self.draw_text(80, "輪廻", COL, self.screen, txt_posx, txt_posy+20)
        self.draw_text(80, "ループ", COL, self.screen, txt_posx+60, txt_posy+100)
        self.screen.blit(self.character, (340, 370))
        self.screen.blit(self.enemy,(600,280))




        for rect, color, txt in zip(rects, colors, txts):
            pygame.draw.rect(self.screen, color, rect)
            self.draw_text(50, txt, COL, self.screen, rect[0] + 20, rect[1] + 10)
        pygame.display.update()

    def update(self):
        # 画面切り替え
        # 上下、enter
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_KP8:
                    print("up")
                    if self.select != 0:
                        self.select -= 1
                        self.sounds.play_se_cur()
                elif event.key == K_DOWN or event.key == K_KP2:
                    print("dwn")
                    if self.select != 2:
                        self.select += 1
                        self.sounds.play_se_cur()
                elif event.key == K_KP_ENTER or event.key == K_RETURN:
                    print("ent")
                    self.pushed_enter = 1
                    self.sounds.play_se_sel()

    def draw_text(self, siz, txt, col, sc, x, y):
        fnt = pygame.font.Font(FONT, siz)
        sur = fnt.render(txt, True, col)
        self.screen.blit(sur, [x, y])


def main():
    title = Title()
    while 1:
        if title.pushed_enter == 1:
            title.draw()
            title.update()

        if title.pushed_enter == 0:
            if title.select == 0:
                # 始める
                title.screen.fill((255, 0, 0))
                pygame.display.update()
            elif title.select == 1:
                # 続ける
                title.screen.fill((0, 255, 0))
                pygame.display.update()
            else:
                # 終わる
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
