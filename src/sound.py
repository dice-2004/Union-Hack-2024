import pygame.mixer

MAIN_BGM = "./asset/bgm/MusMus-BGM-163.mp3"
SE_CUR = "./asset/se/決定ボタンを押す31.mp3"
SE_SEL = "./asset/se/決定ボタンを押す38.mp3"
SE_RLT = "./asset/se/カーソル移動12.mp3"
SE_BTL = "./asset/se/高速移動.mp3"
SE_ATK = "./asset/se/剣で斬る2.mp3"
SE_DEF = "./asset/se/盾で防御.mp3"


class Sounds:
    def __init__(self) -> None:
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.6)
        self.se_cur = pygame.mixer.Sound(SE_CUR)
        self.se_sel = pygame.mixer.Sound(SE_SEL)
        self.se_rlt = pygame.mixer.Sound(SE_RLT)
        self.se_btl = pygame.mixer.Sound(SE_BTL)
        self.se_atk = pygame.mixer.Sound(SE_ATK)
        self.se_def = pygame.mixer.Sound(SE_DEF)

    def mainbgm(self):
        pygame.mixer.music.load(MAIN_BGM)
        pygame.mixer.music.play(-1)

    def play_se_cur(self):
        self.se_cur.play()

    def play_se_sel(self):
        self.se_sel.play()

    def play_se_rlt(self):
        self.se_rlt.play()

    def play_se_btl(self):
        self.se_btl.play()
