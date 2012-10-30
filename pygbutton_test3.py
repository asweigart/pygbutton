import pygame, pygbutton, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

WHITE = (255, 255, 255)

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PygButton Test 3')

    catButt = pygbutton.PygButton((50, 100, 200, 30), normal='catbutton_normal.png', down='catbutton_down.png', highlight='catbutton_highlight.png')

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            buttonEvents = catButt.handleEvent(event)
            if 'click' in buttonEvents:
                catButt.rect = pygame.Rect((catButt.rect.left, catButt.rect.top, catButt.rect.width + 10, catButt.rect.height + 10))

        DISPLAYSURFACE.fill(WHITE)

        catButt.draw(DISPLAYSURFACE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
