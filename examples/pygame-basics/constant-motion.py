import pygame
import sys

width, height = 800, 600
sz = 20
# x, y = 0, 0
x = 0
y = 0
xvel = 0
yvel = 0
sz = 20
move_distance = 1

screen = pygame.display.set_mode( (width, height) )

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yvel = -move_distance
                xvel = 0
            if event.key == pygame.K_DOWN:
                yvel = move_distance
                xvel = 0
    
    x += xvel
    y += yvel
    pygame.draw.rect(screen, (200, 180, 255), (x, y, sz, sz))
    
    pygame.display.flip()
