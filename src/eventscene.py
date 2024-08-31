import pygame

import enemy

FONT = "font/x12y16pxMaruMonica.ttf"


class EventScene:
    def __init__(self, x: int, y: int):
        self.pos = (x, y)
        self.font = pygame.font.Font(FONT, 32)
        self.mode_enemystat = False

    def enemy_stat_upd(self, en: enemy.Enemy, enhp: int):
        self.mode_enemystat = True
        self.text = self.font.render(
            f"level: {en.lv} hp: {enhp} atk: {en.atk}",
            True,
            (255, 255, 255),
        )

    def disable(self):
        self.mode_enemystat = False

    def draw(self, screen):
        if self.mode_enemystat:
            screen.blit(self.text, self.pos)
