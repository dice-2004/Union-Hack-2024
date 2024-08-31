import pygame

import enemy

FONT = "font/x12y16pxMaruMonica.ttf"


class EventScene:
    def __init__(self, x: int, y: int):
        self.pos = (x, y)
        self.font = pygame.font.Font(FONT, 32)

    def enemy_stat_upd(self, en: enemy.Enemy):
        self.text = self.font.render(
            f"level: {en.lv} hp: {en.hp} atk: {en.atk}",
            True,
            (255, 255, 255),
        )

    def draw(self, screen):
        screen.blit(self.text, self.pos)
