import random

def get_callsign(n):
    """Return the random generated сallsign.
    Input: numbers of callgin
    Return: List of numbers callsign
    """
    f = open('master.txt')
    callsigns = list(f.read().split('\n')) # callsign list
    # shuffle list
    for i in range(5):
        random.shuffle(callsigns)
    return random.sample(callsigns, n) #return n-list


def get_serial():
    """Return the random generated serial number."""
    serial_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'N', 'T']
    serial_short = ''.join(random.sample(serial_range, 1) + random.sample(serial_range, 1) + random.sample(serial_range, 1))
    serial_full = serial_short
    if 'A' in serial_short or 'N' in serial_short or 'T' in serial_short:
        serial_full =  serial_full.replace('A', '1')
        serial_full = serial_full.replace('N', '9')
        serial_full = serial_full.replace('T', '0')
    if int(serial_full) == 0:
        serial_short = 'TT1'
        serial_full = '001'
    return serial_short, serial_full