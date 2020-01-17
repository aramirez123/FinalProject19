import pygame
import sys

w, h = 800, 600
sz = 20

screen = pygame.display.set_mode( (w, h) )

class Thing:

    def __init__(self, x, y):
        self.image = pygame.image.load('snowflake.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        # self.width = width
        # self.height = height
    
    def show(self):
        screen.blit(self.image, self.rect)

    def follow_mouse(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]
    
    def check_hit(self, other_thing):
        # check if this item's image rectangle hit's the other item's image rectangle        
        if self.rect.colliderect(other_thing.rect):
            print("HIT!")

t = Thing(50, 50)
t2 = Thing(100, 100)

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    t.show()
    t2.show()
    t2.follow_mouse()
    t.check_hit(t2)

    pygame.display.flip()
