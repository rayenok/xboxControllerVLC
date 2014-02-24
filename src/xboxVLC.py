#!/usr/bin/python2.7
import os
import time
import pygame
import subprocess
from pygame.locals import *


def buttonsController(nButton):
    # A: 0
    # B: 1
    # X: 2
    # Y: 3
    # LB: 4
    # RB: 5
    # RB: 5
    # back: 6
    # start: 7

    try:
        if nButton == 0:
            # A controller -> reduce the volume
            os.system('amixer -q set Master 5%-')
        elif nButton == 1:
            # B controller -> play next
            with open(os.devnull, 'wb') as devnull:
                subprocess.check_call(['dbus-send',
                                       '--session',
                                       '--type=method_call',
                                       '--print-reply',
                                       '--dest=org.mpris.MediaPlayer2.vlc',
                                       '/org/mpris/MediaPlayer2',
                                       'org.mpris.MediaPlayer2.Player.Next'],
                                       stdout=devnull,
                                       stderr=devnull)
        elif nButton == 2:
            # X controller -> play previous
            with open(os.devnull, 'wb') as devnull:
                subprocess.check_call(['dbus-send',
                                        '--session',
                                        '--type=method_call',
                                        '--print-reply',
                                        '--dest=org.mpris.MediaPlayer2.vlc',
                                        '/org/mpris/MediaPlayer2',
                                        'org.mpris.MediaPlayer2.Player.Previous'],
                                        stdout=devnull,
                                        stderr=devnull)
        elif nButton == 3:
            # Y controller -> increase the volume
            os.system('amixer -q set Master 5%+')
        elif nButton == 7:
            # Y controller -> increase the volume
            with open(os.devnull, 'wb') as devnull:
                print "start"
                subprocess.check_call(['dbus-send',
                                        '--session',
                                        '--type=method_call',
                                        '--print-reply',
                                        '--dest=org.mpris.MediaPlayer2.vlc',
                                        '/org/mpris/MediaPlayer2',
                                        'org.mpris.MediaPlayer2.Player.PlayPause'],
                                        stdout=devnull,
                                        stderr=devnull)
    except:
        pass

# pygame.init()
# joystick = pygame.joystick.Joystick(0)
# joystick.init()
# time.sleep(5)
pygame.init()
while 1:
    try:
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

            for event in pygame.event.get():
                    if event.type == JOYBUTTONDOWN:
                        buttonsController(event.button)
    except:
        pass
