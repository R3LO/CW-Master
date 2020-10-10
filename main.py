import data
import play

def audio(message, wpm=35, fs=33, sps=48000, freq=900):
    play.main(message, wpm, fs, sps, freq)


for i in range(5):
    msg = data.get_callsign(1)[0] + ' 5NN ' + data.get_serial(3)[1]
    print(i+1, msg)
    audio(msg)

