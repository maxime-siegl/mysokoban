import pygame
from pygame import mixer

pygame.init()
mixer.init()

screen = pygame.display.set_mode((500, 500))
done = False
x = 60
y = 60

image = pygame.image.load(r'C:\Users\maxii\Pictures\map_sokoban.png')
screen.blit(image, (0, 0))

# pour ajouter de la musique dans le jeu
# pygame.mixer.music.load(r'C:\Users\Tanishq\Desktop\song.mp3')
# pygame.mixer.music.play(-1)

is_red = True

while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= 10
        if pressed[pygame.K_DOWN]:
            y += 10
        if pressed[pygame.K_LEFT]:
            x -= 10
        if pressed[pygame.K_RIGHT]:
            x += 10
        if is_red:
            color = (255, 0, 0)
        else:
            color = (102, 0, 0)

        if x <= 0:
            x = 0
        elif x >= 400:
            x = 400
        if y >= 400:
            y = 400
        elif y <= 0:
            y = 0
        screen.blit(image, (0, 0))

        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 90, 90))

    pygame.display.flip()
