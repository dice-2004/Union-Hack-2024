import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = 0
        self.nowtile = 0
        self.restart = 0
        self.lv = 1
        self.exp = 0
        self.hp = 20

    def update(self):
        pass

    def move(self, x: int, y: int):
        # TODO animation move_ip
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
