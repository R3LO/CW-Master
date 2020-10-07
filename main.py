import data

# for i in range(5):
#     print(data.get_callsign(1), data.get_serial(3))
# print(int(data.get_serial(5)[0]))

call1 = 'R3LO'.upper().strip()
call2 = ' R3lo'.upper().strip()

data.check_callsign('sp4ae', 'as4d')
data.check_callsign(call1, call2)
data.check_callsign('ua3lpf', 'va3lpf')
data.check_callsign('g5ll   ', 'g5ff')
data.check_callsign('hj4f', '5j4d')






