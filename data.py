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
    print('test')