import pygame

class Key(pygame.sprite.Sprite):
    def __init__(self, pos, mode):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("assets/"+mode+".png")
        self.rect=self.image.get_rect(topleft=pos)
        self.initpos=pos
        self.used=False
    def update(self):
        pass
    def use(self):
        self.used=not self.used
        if self.used:
            self.rect[1]=self.initpos[1]+2
        else:
            self.rect[1]=self.initpos[1]