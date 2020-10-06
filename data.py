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


def get_serial(n):
    """Return the random generated serial number.
    Input: numberd of figures
    Return: list cut and full serials
    """
    serial_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    serial_full = serial_cut = ''.join(random.sample(serial_range, n))
    short_range = random.choice([True, False])
    # True = need to cut serial
    if short_range:
        if '1' in serial_cut:
            serial_cut = serial_cut.replace('1', 'A')
        if '9' in serial_cut:
            serial_cut = serial_cut.replace('9', 'N')
        if '0' in serial_cut:
            serial_cut = serial_cut.replace('0', 'T')
    # fix up wrong serial 000
    if int(serial_full) == 0:
        serial_full = "001"
        serial_cut = "TT1"
    return serial_full, serial_cut