import pygame.mixer

MAIN_BGM = "./asset/bgm/MusMus-BGM-163.mp3"
SE_CUR = "./asset/se/決定ボタンを押す31.mp3"
SE_SEL = "./asset/se/決定ボタンを押す38.mp3"
SE_RLT = "./asset/se/カーソル移動12.mp3"


class Sounds:
    def __init__(self) -> None:
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.6)
        self.se_cur = pygame.mixer.Sound(SE_CUR)
        self.se_sel = pygame.mixer.Sound(SE_SEL)

    def mainbgm(self):
        pygame.mixer.music.load(MAIN_BGM)
        pygame.mixer.music.play(-1)

    def play_se_cur(self):
        self.se_cur.play()

    def play_se_sel(self):
        self.se_sel.play()
