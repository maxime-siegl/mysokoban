import pygame
from pygame.locals import *

from initialisation import *


class Player:
    def __init__(self, boardgame):
        self.gauche = pygame.image.load("img/mario_gauche.gif")
        self.droite = pygame.image.load("img/mario_droite.gif")
        self.bas = pygame.image.load("img/mario_bas.gif")
        self.haut = pygame.image.load("img/mario_haut.gif")

        self.size_transform = (SIZE, SIZE)

        self.gauche_scale = pygame.transform.scale(self.gauche, self.size_transform)
        self.droite_scale = pygame.transform.scale(self.droite, self.size_transform)
        self.bas_scale = pygame.transform.scale(self.bas, self.size_transform)
        self.haut_scale = pygame.transform.scale(self.haut, self.size_transform)

        self.position = self.bas_scale

        self.boardgame = boardgame
        self.locationPlayer = self.boardgame.getplayerposition()

        self.x = int(self.locationPlayer[0]/SIZE)
        self.y = int(self.locationPlayer[1]/SIZE)

    def drawplayer(self, screen):
        screen.blit(self.position, (self.x * SIZE, self.y * SIZE))

    def move(self, key):
        if key == K_LEFT:
            self.position = self.gauche_scale
            if not self.checkcollision():
                self.x -= 1
        elif key == K_RIGHT:
            self.position = self.droite_scale
            if not self.checkcollision():
                self.x += 1
        elif key == K_UP:
            self.position = self.haut_scale
            if not self.checkcollision():
                self.y -= 1
        elif key == K_DOWN:
            self.position = self.bas_scale
            if not self.checkcollision():
                self.y += 1

    def checkcollision(self):
        self.hauty = self.y - 1
        self.basy = self.y + 1
        self.droitex = self.x + 1
        self.gauchex = self.x - 1

        # Parcourir les coordonnées
        for y in range(len(self.boardgame.lvl_default)):
            for x in range(len(self.boardgame.lvl_default[y])):
                # MOVE UP
                if self.position == self.haut_scale:
                    # voir quel number est retourné lorsqu'on va dans cette direction [0, 1, 2, 3]
                    location_boardgame = self.boardgame.lvl_default[self.hauty][self.x]
                    if location_boardgame == BOX or location_boardgame == GOAL:
                        is_box = self.boardgame.movebox(self.x, self.y, "haut")
                        if is_box:
                            self.y = self.hauty
                    return location_boardgame == WALL or location_boardgame == BOX or location_boardgame == GOAL
                # MOVE DOWN
                elif self.position == self.bas_scale:
                    location_boardgame = self.boardgame.lvl_default[self.basy][self.x]
                    if location_boardgame == BOX or location_boardgame == GOAL:
                        is_box = self.boardgame.movebox(self.x, self.y, "bas")
                        if is_box:
                            self.y = self.basy
                    return location_boardgame == WALL or location_boardgame == BOX or location_boardgame == GOAL
                # MOVE LEFT
                elif self.position == self.gauche_scale:
                    location_boardgame = self.boardgame.lvl_default[self.y][self.gauchex]
                    if location_boardgame == BOX or location_boardgame == GOAL:
                        is_box = self.boardgame.movebox(self.x, self.y, "gauche")
                        if is_box:
                            self.x = self.gauchex
                    return location_boardgame == WALL or location_boardgame == BOX or location_boardgame == GOAL
                # MOVE RIGHT
                elif self.position == self.droite_scale:
                    location_boardgame = self.boardgame.lvl_default[self.y][self.droitex]
                    if location_boardgame == BOX or location_boardgame == GOAL:
                        is_box = self.boardgame.movebox(self.x, self.y, "droite")
                        if is_box:
                            self.x = self.droitex
                    return location_boardgame == WALL or location_boardgame == BOX or location_boardgame == GOAL
