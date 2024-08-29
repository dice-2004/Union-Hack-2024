import pygame


class Reborn(pygame.sprite.Sprite):
    def __init__(self, name: str, x: int, y: int) -> None:
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
