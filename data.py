import random

def get_callsign(n):
    """Return the random generated сallsign.
    Input: numbers of callgin
    Return: List of numbers callsign
    """
    f = open('master.txt')
    callsigns = list(f.read().split('\n')) # callsign list
    # shuffle list
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


def check_callsign(call_sent, call_recd):
    """Check out difrance between sent and receoved calls
    Input: both callsign
    Return: none
    """
    if call_sent == call_recd:
        print('[+] ', call_sent, '\t = ', call_recd, '\t\t\tWrong symbols: ---', end='')
    else:

        if call_recd in call_sent: # part of received call present in sent call
            wrongs = call_sent.replace(call_recd, '')
            print('[-] ', call_sent, '\t ~ ', call_recd, '\t\t\tWrong symbols: ', wrongs, end='')
        else: # check symbol by symbol
            print('[-] ', call_sent, '\t ~ ', call_recd, '\t\t\tWrong symbols: ', end='')
            for i in range(len(call_sent)):
                try:
                    if call_sent[i] == call_recd[i]:
                        pass
                        # print(call1[i], ' You are right ', call_recd[i])
                    else:
                        print(call_sent[i], end=' ')
                except IndexError:
                    print(call_sent[i], end=' ')
    print('')

def check_serial(serial_sent, serial_recd):
    pass