#tme7ex4
import pygame

pygame.init()
SCREEN_WIDTH = 920 # window width
SCREEN_HEIGHT = 920 # window height
MARGIN = 10 # margin around the board
BOARD = 900 # Real size of the board

LIGHT_GRAY = (224,224,224)
BLACK = (0, 0, 0)
WHITE = (255,255,255)

#tme7ex5
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Refresh the screen
    screen.fill(BLACK)
    pygame.display.flip()
# deactivates the pygame library
pygame.quit()
# quit the program
quit()

#tme7ex6
CASE = BOARD//len(board)
pygame.draw.rect(screen,YOUR_COLOR,[x, y, tile_size-2, tile_size-2])