
#!/usr/bin/python2.7
import logging,os,time,pygame
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
    if nButton == 0:
        # A controller -> reduce the volume
        os.system('amixer -q set Master 5%-')
    elif nButton == 1:
        # B controller -> play next
        os.system('dbus-send --session --type=method_call --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next')
    elif nButton == 2:
        # X controller -> play previous
        os.system('dbus-send --session --type=method_call --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous')
    elif nButton == 3:
        # Y controller -> increase the volume
        os.system('amixer -q set Master 5%+')
    elif nButton == 7:
        # Y controller -> increase the volume
        os.system('dbus-send --session --type=method_call --print-reply --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause')


pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
time.sleep(5)
while 1:
    try:
        for event in pygame.event.get():
                if event.type == JOYBUTTONDOWN:
                    # logging.log(10,"Down: "+str(event.button))
                    buttonsController(event.button)
    except:
        pass
