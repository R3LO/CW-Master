import data
import play

def audio(message, wpm=35, fs=33, sps=48000, freq=900):
    play.main(message, wpm, fs, sps, freq)

wpm = 35
for i in range(5):
    call_sent = data.get_callsign(1)[0]
    serial_sent = data.get_serial(3)
    msg = call_sent + ' 5NN ' + serial_sent[1]
    wpm += 1
    audio(msg, wpm)
    call_recd, serial_recd = input().split()
    data.check_callsign(call_sent, call_recd.upper())
    data.check_serial(serial_sent[0], serial_recd)


