import inputs
import time
from ppadb.client import Client

lastrun = 0
lastturn = 0

def horizontal(device, state):
    global lastturn
    if abs(state) > 23000 and time.time() - lastturn >= 1.2:
        if state < -1:
            print('Turning Left')
            roll(device, 'left')
        if state > 1:
            print('Turning Right')
            roll(device, 'right')
        lastwalk = time.time()

def vertical(device, state):
    global lastturn
    if abs(state) > 23000 and time.time() - lastturn >= 1.2:
        if state < -1:
            print('Turning up')
            roll(device, 'up')
        if state > 1:
            print('Turning down')
            roll(device, 'down')
        lastwalk = time.time()

def triggerR(device, state):
    print('trigger R S1')

def triggerL(device, state):
    print('trigger L S2')

def bumperL(device, state):
    print('bumper L S3')

def bumperR(device, state):
    print('bumper L S4')

def kick_right(device, state):
    print('kick R')

def kick_left(device, state):
    print('kick L')


def roll(device, direction):
    if direction == 'left':
        device.shell('input touchscreen swipe 500 800 250 800 100')
    elif direction == 'right':
        device.shell('input touchscreen swipe 500 800 750 800 100')
    if direction == 'up':
        device.shell('input touchscreen swipe 500 800 500 500 100')
    elif direction == 'down':
        device.shell('input touchscreen swipe 500 800 500 1100 100')

def attack(device, state):
    device.shell('input touchscreen tap 500 800')

lastCharge = 0
def chargeForceStrike(device, state):
    device.shell('input touchscreen swipe 500 800 500 1100 10000')

def auto_repeat_settings(device, start):
    device.shell('input touchscreen tap 800 1200')

def start(device, start):
    device.shell('input touchscreen tap 800 1500')


def back(device, state):
    device.shell('input keyevent 4')

# add prefer team button
# handle the out of resource i.e. tap + for using honey or wings

def sidestep(device, state):
    print('side step')


#lambda z: wave(z, 'right')
'''
Button mapping:
'''
event_mapping = {
    'BTN_MODE': None,
    'BTN_START' : auto_repeat_settings,
    'BTN_SELECT' : start,
    'BTN_NORTH' : None ,
    'BTN_SOUTH' : attack,
    'BTN_EAST' : back,
    'BTN_WEST' : chargeForceStrike,
    'BTN_TR' : bumperR,
    'BTN_TL' : bumperL,
    'BTN_THUMBR' : kick_right,
    'BTN_THUMBL' : kick_left,
    'ABS_Z' : None,
    'ABS_RZ' : None,
    'ABS_X' : horizontal,
    'ABS_Y' : vertical,
    'ABS_RX' : triggerR,
    'ABS_RY' : triggerL,
    'ABS_HAT0X': sidestep,
    'ABS_HAT0Y': None, #lambda x: walk(x, 0.5),
}

def get_android_device():
    adb = Client(host="127.0.0.1", port=5037)
    print(adb.version())
    devices = adb.devices()
    
    if len(devices) == 0:
        print('no device attached')
        quit()

    return devices[0]

def event_loop(device, events):
    '''
    This function is called in a loop, and will get the events from the
    controller and send them to the functions we specify in the `event_mapping`
    dictionary
    '''
    for event in events:
        print('\t', event.ev_type, event.code, event.state)
        call = event_mapping.get(event.code)
        if callable(call):
            call(device, event.state)

if __name__ == '__main__':
    pads = inputs.devices.gamepads

    device = get_android_device()

    if len(pads) == 0:
        raise Exception("Could not find any gamepad plugged in")
    
    try:
        while True:
            event_loop(device, inputs.get_gamepad())
    except KeyboardInterrupt:
        print("Exit!")


