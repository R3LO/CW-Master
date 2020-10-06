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
    serial = ''.join(random.sample(serial_range, 1) + random.sample(serial_range, 1) + random.sample(serial_range, 1))
    return serial