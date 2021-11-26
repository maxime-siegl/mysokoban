import pygame
from initialisation import *


class BoardGame:
    def __init__(self, matrice):
        self.ref_img = {
            WALL: pygame.image.load("img/mur.jpg"),
            BOX: pygame.image.load("img/caisse.jpg"),
            TARGET: pygame.image.load("img/objectif.png"),
            GOAL: pygame.image.load("img/caisse_ok.jpg")
        }

        self.size_transform = (SIZE, SIZE)
        self.ref_img[WALL] = pygame.transform.scale(self.ref_img[WALL], self.size_transform)
        self.ref_img[BOX] = pygame.transform.scale(self.ref_img[BOX], self.size_transform)
        self.ref_img[TARGET] = pygame.transform.scale(self.ref_img[TARGET], self.size_transform)
        self.ref_img[GOAL] = pygame.transform.scale(self.ref_img[GOAL], self.size_transform)

        with open(matrice, 'r') as fichier:
            self.lvl_default = [[int(number) for number in line.strip()] for line in fichier]

        self.coord_object = []
        for y in range(len(self.lvl_default)):
            for x in range(len(self.lvl_default[y])):
                if self.lvl_default[y][x] == TARGET:
                    self.coord_object.append((x, y))

    def drawmap(self, screen):
        for y in range(len(self.lvl_default)):
            for x in range(len(self.lvl_default[y])):
                img = self.lvl_default[y][x]
                if img in (FREE, PLAYER):
                    x += 1
                else:
                    screen.blit(self.ref_img[img], (x*SIZE, y*SIZE))

    def getplayerposition(self):
        for y in range(len(self.lvl_default)):
            for x in range(len(self.lvl_default[y])):
                if self.lvl_default[y][x] == PLAYER:
                    return x*SIZE, y*SIZE

    # déplacement des caisses sur le plateau
    def movebox(self, x, y, location):
        self.is_end()
        if location == 'haut':
            if self.lvl_default[y-2][x] not in (WALL, BOX, GOAL):
                if self.lvl_default[y-1][x] == GOAL:
                    self.lvl_default[y-1][x] = TARGET
                else:
                    self.lvl_default[y-1][x] = FREE
                if self.lvl_default[y-2][x] == TARGET:
                    self.lvl_default[y-2][x] = GOAL
                    return True
                else:
                    self.lvl_default[y - 2][x] = BOX
                    return True

        if location == 'bas':
            if self.lvl_default[y+2][x] not in (WALL, BOX, GOAL):
                if self.lvl_default[y+1][x] == GOAL:
                    self.lvl_default[y+1][x] = TARGET
                else:
                    self.lvl_default[y+1][x] = FREE
                if self.lvl_default[y+2][x] == TARGET:
                    self.lvl_default[y+2][x] = GOAL
                    return True
                else:
                    self.lvl_default[y+2][x] = BOX
                    return True

        if location == 'gauche':
            if self.lvl_default[y][x-2] not in (WALL, BOX, GOAL):
                if self.lvl_default[y][x-1] == GOAL:
                    self.lvl_default[y][x-1] = TARGET
                else:
                    self.lvl_default[y][x-1] = FREE
                if self.lvl_default[y][x-2] == TARGET:
                    self.lvl_default[y][x-2] = GOAL
                    return True
                else:
                    self.lvl_default[y][x-2] = BOX
                    return True

        if location == 'droite':
            if self.lvl_default[y][x+2] not in (WALL, BOX, GOAL):
                if self.lvl_default[y][x+1] == GOAL:
                    self.lvl_default[y][x+1] = TARGET
                else:
                    self.lvl_default[y][x+1] = FREE
                if self.lvl_default[y][x+2] == TARGET:
                    self.lvl_default[y][x+2] = GOAL
                    return True
                else:
                    self.lvl_default[y][x+2] = BOX
                    return True
        return False

    def is_end(self):
        result = [self.lvl_default[y][x] for (x, y) in self.coord_object]

        return result.count(GOAL) == len(self.coord_object)


if __name__=="__main__":
    g = BoardGame()
    g.drawmap()