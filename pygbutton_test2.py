import pygame, pygbutton, sys
from pygame.locals import *
import platform

FPS = 30
WINDOWWIDTH = 300
WINDOWHEIGHT = 200

WHITE = (255, 255, 255)

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PygButton Test 2')

    buttonHello = pygbutton.PygButton((50, 100, 200, 30), 'Hello')
    buttonToggleVis = pygbutton.PygButton((50, 50, 200, 30), 'Toggle Button Visibility')

    if platform.system() == 'Windows':
        buttonHello.font = pygame.font.SysFont('comicsansms', 20) # Unfortunately, this line will only work on Windows machines.

    visMode = True

    while True: # main game loop

        buttonHello.visible = visMode

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            events = buttonToggleVis.handleEvent(event)
            if 'click' in events:
                visMode = not visMode

            buttonHello.handleEvent(event)

        DISPLAYSURFACE.fill(WHITE)

        buttonToggleVis.draw(DISPLAYSURFACE)
        buttonHello.draw(DISPLAYSURFACE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
