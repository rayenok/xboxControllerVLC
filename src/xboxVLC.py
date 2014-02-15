
import logging
import pygame
from pygame.locals import *


def buttonsController(nButton, value):
    # A: 0
    # B: 1
    # X: 2
    # Y: 3
    # LB: 4
    # RB: 5
    # RB: 5
    # back: 6
    # start: 7
    if nButton == 0:
        # A controller -> reduce the volume
        print "A"
        pass
    elif nButton == 1:
        # B controller -> play next
        print "B"
        pass
    elif nButton == 2:
        # X controller -> play previous
        print "X"
        pass
    elif nButton == 3:
        # Y controller -> increase the volume
        print "Y"
        pass


pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

while 1:
        # clock.tick(60)
    try:
        for event in pygame.event.get():
                if event.type == JOYBUTTONDOWN:
                    # logging.log(10,"Down: "+str(event.button))
                    buttonsController(event.button,1)
                elif event.type == JOYBUTTONUP:
                    # logging.log(10,"Up: "+str(event.button))
                    # print "Up: "+str(event.button)
                    buttonsController(event.button,0)
    except:
        pass

# pythoncom.PumpMessages()
