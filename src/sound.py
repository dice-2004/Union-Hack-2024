import pygame.mixer

MAIN_BGM = "./asset/bgm/MusMus-BGM-163.mp3"
SE_CUR = "./asset/se/カーソル移動12.mp3"
SE_SEL = "./asset/se/決定ボタンを押す38.mp3"


class Sound:
    def __init__(self) -> None:
        pygame.mixer.init()

    def mainbgm():
        pygame.mixer.music.load(MAIN_BGM)
        pygame.mixer.music.play(-1)

    def se_cur():
        pygame.mixer.music.load(SE_CUR)
        pygame.mixer.music.play(1)

    def se_sel():
        pygame.mixer.music.load(SE_SEL)
        pygame.mixer.music.play(1)
