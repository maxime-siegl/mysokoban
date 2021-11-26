import pygame
import sys
from pygame.locals import *
from boardGame import BoardGame
from player import Player


pygame.init()
screen = pygame.display.set_mode((408, 408))
pygame.display.set_caption('My Sokoban RunTrack')

background = pygame.image.load("img/back.png")
background_scale = pygame.transform.scale(background, (408, 408))
screen.blit(background_scale, (0, 0))

boardgame = BoardGame("map/lvl_hard.txt")
boardgame.drawmap(screen)

player = Player(boardgame)
player.drawplayer(screen)

pygame.display.flip()


while not boardgame.is_end():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            player.move(event.key)
    screen.blit(background_scale, (0, 0))
    boardgame.drawmap(screen)
    player.drawplayer(screen)
    pygame.display.flip()