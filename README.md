Pygbutton - A Button UI Element for Pygame

http://inventwithpython.com/blog/2012/10/30/creating-a-button-ui-module-for-pygame/

Pygbutton is a simple button UI that you can add to your Pygame programs.

You can download a few example programs here: http://inventwithpython.com/pygbutton_src.zip

The code to implement it is fairly basic:

import pygbutton
buttonObj = pygbutton.PygButton((50, 50, 60, 30), 'Button Caption')
while True: # main game loop
    for event in pygame.event.get(): # event handling loop
        if 'click' in buttonObj.handleEvent(event):
            pass # Do stuff in response to button click here.
buttonObj.draw(DISPLAYSURFACE) # where DISPLAYSURFACE was the Surface object returned from pygame.display.set_mode()

The full explanation of the code and how it was written can be found in the aboved linked blog post.