import pygame, pygbutton, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 380
WINDOWHEIGHT = 350

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


def main():
    windowBgColor = WHITE

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PygButton Test 1')

    # buttons that change the window background color
    buttonWhiteWinBg = pygbutton.PygButton((50, 50, 60, 30), 'White')
    buttonRedWinBg = pygbutton.PygButton((50, 100, 60, 30), 'Red')
    buttonGreenWinBg = pygbutton.PygButton((50, 150, 60, 30), 'Green')
    buttonBlueWinBg = pygbutton.PygButton((50, 200, 60, 30), 'Blue')
    buttonBlackWinBg = pygbutton.PygButton((50, 250, 60, 30), 'Black')
    winBgButtons = (buttonWhiteWinBg, buttonRedWinBg, buttonGreenWinBg, buttonBlueWinBg, buttonBlackWinBg)

    # buttons that change the button background color
    buttonWhiteBg = pygbutton.PygButton((150, 50, 60, 30), 'White')
    buttonRedBg = pygbutton.PygButton((150, 100, 60, 30), 'Red')
    buttonGreenBg = pygbutton.PygButton((150, 150, 60, 30), 'Green')
    buttonBlueBg = pygbutton.PygButton((150, 200, 60, 30), 'Blue')
    buttonBlackBg = pygbutton.PygButton((150, 250, 60, 30), 'Black')
    BgButtons = (buttonWhiteBg, buttonRedBg, buttonGreenBg, buttonBlueBg, buttonBlackBg)

    # buttons that change the button text color
    buttonWhiteFg = pygbutton.PygButton((250, 50, 60, 30), 'White')
    buttonRedFg = pygbutton.PygButton((250, 100, 60, 30), 'Red')
    buttonGreenFg = pygbutton.PygButton((250, 150, 60, 30), 'Green')
    buttonBlueFg = pygbutton.PygButton((250, 200, 60, 30), 'Blue')
    buttonBlackFg = pygbutton.PygButton((250, 250, 60, 30), 'Black')
    FgButtons = (buttonWhiteFg, buttonRedFg, buttonGreenFg, buttonBlueFg, buttonBlackFg)

    allButtons = winBgButtons + BgButtons + FgButtons

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if 'click' in buttonWhiteWinBg.handleEvent(event):
                windowBgColor = WHITE
            if 'click' in buttonRedWinBg.handleEvent(event):
                windowBgColor = RED
            if 'click' in buttonGreenWinBg.handleEvent(event):
                windowBgColor = GREEN
            if 'click' in buttonBlueWinBg.handleEvent(event):
                windowBgColor = BLUE
            if 'click' in buttonBlackWinBg.handleEvent(event):
                windowBgColor = BLACK

            buttonBgColor = None
            if 'click' in buttonWhiteBg.handleEvent(event):
                buttonBgColor = WHITE
            if 'click' in buttonRedBg.handleEvent(event):
                buttonBgColor = RED
            if 'click' in buttonGreenBg.handleEvent(event):
                buttonBgColor = GREEN
            if 'click' in buttonBlueBg.handleEvent(event):
                buttonBgColor = BLUE
            if 'click' in buttonBlackBg.handleEvent(event):
                buttonBgColor = BLACK

            if buttonBgColor is not None:
                for b in BgButtons:
                    b.bgcolor = buttonBgColor

            buttonFgColor = None
            if 'click' in buttonWhiteFg.handleEvent(event):
                buttonFgColor = WHITE
            if 'click' in buttonRedFg.handleEvent(event):
                buttonFgColor = RED
            if 'click' in buttonGreenFg.handleEvent(event):
                buttonFgColor = GREEN
            if 'click' in buttonBlueFg.handleEvent(event):
                buttonFgColor = BLUE
            if 'click' in buttonBlackFg.handleEvent(event):
                buttonFgColor = BLACK

            if buttonFgColor is not None:
                for b in FgButtons:
                    b.fgcolor = buttonFgColor

        DISPLAYSURFACE.fill(windowBgColor)

        for b in allButtons:
            b.draw(DISPLAYSURFACE)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
