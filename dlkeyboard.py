import time
import threading
from ppadb.client import Client

def left(device):
    roll(device, 'left')

def right(device):
    roll(device, 'right')

def up(device):
    roll(device, 'up')

def down(device):
    chargeForceStrike(device, 'down')

def fs_left(device):
    chargeForceStrike(device, 'left')

def fs_right(device):
    chargeForceStrike(device, 'right')

def fs_up(device):
    chargeForceStrike(device, 'up')

def fs_down(device):
    chargeForceStrike(device, 'down')

def roll(device, direction):
    if direction == 'left':
        device.shell('input touchscreen swipe 500 800 250 800 100')
    elif direction == 'right':
        device.shell('input touchscreen swipe 500 800 750 800 100')
    if direction == 'up':
        device.shell('input touchscreen swipe 500 800 500 500 100')
    elif direction == 'down':
        device.shell('input touchscreen swipe 500 800 500 1100 100')

def attack(device):
    device.shell('input touchscreen tap 500 800')

def chargeForceStrike(device, direction):
    if direction == 'right':
        device.shell('input touchscreen swipe 500 800 250 800 1800')
    elif direction == 'left':
        device.shell('input touchscreen swipe 500 800 750 800 1800')
    if direction == 'down':
        device.shell('input touchscreen swipe 500 800 500 500 1800')
    elif direction == 'up':
        device.shell('input touchscreen swipe 500 800 600 1100 1800')

def auto_repeat_settings(device):
    device.shell('input touchscreen tap 800 1200')

def start(device):
    device.shell('input touchscreen tap 800 1500')

def back(device):
    device.shell('input keyevent 4')

def wait(device):
    time.sleep(1)

def s1(device):
    tap(device, 's1')

def s2(device):
    tap(device, 's2')

def s3(device):
    tap(device, 's3')

def s4(device):
    tap(device, 's4')

def ss(device):
    tap(device, 'd')

def t1(device):
    tap(device, 'j')

def tap(device, key):
    print(key)
    position = action_mapping[key]
    print(position)
    device.shell('input touchscreen tap ' + position )

action_mapping = { 
    '1'  : '400 2020',
    '2'  : '575 2020',
    '3'  : '760 2020',
    '4'  : '961 2020',
    'd'  : '180 1720',
    'j'  : '983 1313',
    'k'  : '983 1500',
    'p1' : '82 195',
    'p2' : '82 300',
    'p3' : '82 415',
    'p4' : '82 550',
    'pause'          : '1014 150',
    'retry'          : '318 1702',
    'give_up'        : '800 1700',
    'confirm'        : '776 1400',
    'begin'          : '860 1817',
    'preferred_team' : '712 1475',
    'close_modal'    : '560 1675',
    'next'           : '800 2070',
    'repeat'         : '170 2070'
}


# add prefer team button
# handle the out of resource i.e. tap + for using honey or wings

'''
Button mapping:
'''
event_mapping = {
    'autosetting' : auto_repeat_settings,
    'go' : start,
    'x' : attack,
    'b' : back,
    'c' : lambda x: chargeForceStrike(x, 'right'),
    'a' : left,
    'd' : right,
    'w' : up,
    'S' : fs_down,
    'A' : fs_left,
    'D' : fs_right,
    'W' : fs_up,
    's' : down,
    't' : wait,
    '1' : lambda x: tap(x, '1'),
    '2' : lambda x: tap(x, '2'),
    '3' : lambda x: tap(x, '3'),
    '4' : lambda x: tap(x, '4'),
    '~' : ss,
    'j' : lambda x: tap(x, 'j'),
    'k' : lambda x: tap(x, 'k'),
    '?' : help
}

# standard lilith speed run average time is 1 minute
# mitsuba standard lilith wait after start goes away and when the corrosion message shows up
# j w d 2 t t t 3 t 4 t W t 2 t t 3 t t 4 4 ~ ~ ~ ~ ~ 1 1 x x x x x x 2 t t 3 t 4 x x x x x x ~ ~ ~ ~ 1 t x x x x
# euden
# w w d 1 t t t 3 t 4 t t 2 w x x ~ ~ ~ ~ 1 1 x x x x x x x x x x x x 1 t t 4 t t 3 t 2 t ~ ~ 1 x x x x x x x x x

# standard jalda
# ezilith wand seimei nobu dagger sd, crit doub, prep 100, stren doub, cor, sword psalm ss kar xan, dragon: konohana sakuya
# w w d 2 t t t t t 1 t x x x x 4 t 3 t
# mitsuba bunny, joker, buff time, bow, ss shawu and yuya, ccc, prep 100, low hp def grace print, buff time
# w j 3 t 2 t t t 4 t W 2 t t 3 t 4 x ~ x 1 x x x
# w j 2 t t 3 t 4 t W t 2 t t 3 t 4 x ~ x 1 x x x

# standard asura
# mitsuba
# j d d d d w w w w w t t t t a a a a 2 t t 3 t 4 t t t A 2 t t 3 t 4 t x x x  ~ ~ 1 1 x x x  
# natalie crit db, ccc, blade sd, str db, crit, cor, flash  ss: xander, shawu,dagger, wand, g.lief dragon: arsene 
# W x x x x x x S x x x x x x x x x S W 2 t W x x A t t t t 1 t 4 t t 3 t ~ t 1 1 1 x x x x x

# standard iblis
# 2x hope and v.melody crit db, prep 100%, poison, strength db, skill 40%, ss xander and s. cleo, wand, mona cat, blade, dragon: g.volk
# v: x x 2 t 1 t t 4 t 1 t t t 1 t x x x x 
# mitsuba ccc prep100, buff time, buff time, dragon resur, bow psalm, ss yuya, s.dagger, joker, bow, buff time
# w j 2 t t 3 t 4 t W t 2 t t 3 t 4 x ~ x 1 x x x

def get_android_device():
    adb = Client(host="127.0.0.1", port=5037)
    print(adb.version())
    devices = adb.devices()
    
    if len(devices) == 0:
        print('no device attached')
        quit()

    return devices

def event_loop(devices, commands):
    '''
    This function is called in a loop, and will get the events from the
    controller and send them to the functions we specify in the `event_mapping`
    dictionary
    '''
    if commands:
        for command in commands:
            call = event_mapping.get(command)
            if callable(call):
                thread_list = []
                for device in devices:
                    thread = threading.Thread(target=call, args=(device,))
                    thread_list.append(thread)
                for thread in thread_list:
                    thread.start()
                for thread in thread_list:
                    thread.join()

if __name__ == '__main__':

    devices = get_android_device()
    print(f'there is currently {len(devices)} device(s) connected')
    
    try:
        while True:
            event_loop(devices, input('command: '))
    except KeyboardInterrupt:
        print("Exit!")


