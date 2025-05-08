import pygame
import time

pygame.init()

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

Blue = (0, 0, 255)
White = (255, 255, 255)
Pink = (255, 192, 203)

screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Enter effect in pygame")

grid = []
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not running:
        break  # This will exit the main loop safely

    screen.fill(White)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)

    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
            pygame.draw.rect(screen, Blue, rect)
    grid = new_grid

    pygame.draw.rect(screen, Pink, eraser)
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
