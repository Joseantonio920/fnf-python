import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load("assets/boyfriend.png")
        self.rect=self.image.get_rect(topleft=pos)

        self.keys=None
    def update(self):
        pass
    def key(self, key):
        if key==pygame.K_DOWN:
            self.keys[0].use()
        if key==pygame.K_UP:
            self.keys[1].use()
        if key==pygame.K_LEFT:
            self.keys[2].use()
        if key==pygame.K_RIGHT:
            self.keys[3].use()
    def keys_set(self, keys):
        self.keys=keys