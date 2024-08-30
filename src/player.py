import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y,level,rebornnum,is_load):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = 0
        self.nowtile = 0
        self.exp = 0
        if is_load==1:
            self.rebornnum = rebornnum #ここ
            self.lv = level #ここ
            self.atk = self.lv * 2 + 1
            self.hp = self.lv * 4 + 6
        else:
            self.rebornnum = 0 #ここ
            self.lv = 1 #ここ
            self.hp = 10
            self.atk = 3

    def lvup_check(self):
        if self.lv * self.lv * 3 < self.exp:
            self.lv += 1
            self.exp = 0
        self.atk = self.lv * 2 + 1
        self.hp = self.lv * 4 + 6
        # TODO level up scene

    def move(self, x: int, y: int):
        # TODO animation move_ip
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reborn(self):
        self.lv = 1
        self.exp = 0
        self.lvup_check()
        self.rebornnum += 1
        self.nowtile = 0


class StatusView(pygame.sprite.Sprite):
    def __init__(self, pl: Player, x: int, y: int):
        self.pos = (x, y)
        self.font = pygame.font.SysFont("arial", 16)
        self.update(pl)

    def update(self, pl: Player):
        self.text = self.font.render(
            f"level: {pl.lv}\nexp: {pl.exp}\nhp: {pl.hp}\nreborn: {pl.rebornnum}",
            True,
            (255, 255, 255),
        )

    def draw(self, screen):
        screen.blit(self.text, self.pos)
