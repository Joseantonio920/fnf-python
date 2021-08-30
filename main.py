import sys, os

dirpath=os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame, json
from pygame.locals import *
from scr.player import Player
from scr.key import Key

pygame.init()
window=pygame.display.set_mode((240, 160), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("fnf python")
clock=pygame.time.Clock()
sprites=pygame.sprite.Group()

keys_right=[]
keys_right.append(Key((168, 0), "down"))
keys_right.append(Key((192, 0), "up"))
keys_right.append(Key((144, 0), "left"))
keys_right.append(Key((216, 0), "right"))

for i in range(0, len(keys_right)):
    sprites.add(keys_right[i])

player=Player((160, 120))
player.keys_set(keys_right)
sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN or event.type==pygame.KEYUP:
            player.key(event.key)
    window.fill("gray")

    sprites.draw(window)
    sprites.update()

    pygame.display.flip()
    clock.tick(60)
