import pygame
import sys
import random

ROWS = 6
COLS = 5
CELL_SIZE = 100
# PLAYERS = ["blue", "red"]

# active_player = 0

class Cell:

    def __init__(self, x, y, sz):
        self.x = x * sz
        self.y = y * sz
        self.sz = sz
        # self.contents = ""
        self.contents = random.choice(["red", "blue", ""])
        self.rect = pygame.Rect(self.x, self.y, sz, sz)

    def show(self):
        if self.contents:
            pygame.draw.rect(screen, pygame.Color(self.contents), self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 5)

    # def fill(self):
    #     if self.contents == "":
    #         self.contents = PLAYERS[active_player]
    #         if active_player == 0:
    #             active_player = 1
    #         else:
    #             active_player = 0

    def __repr__(self):
        return f"<{self.x},{self.y}>"

w, h = COLS * CELL_SIZE, ROWS * CELL_SIZE

grid = []


for y in range(ROWS):
    row = []
    for x in range(COLS):
        row.append(Cell(x, y, CELL_SIZE))
    grid.append(row)

screen = pygame.display.set_mode( (w, h) )
print(grid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    for row in grid:
        for cell in row:
            cell.show()
    
    pygame.display.flip()
