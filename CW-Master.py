import wx
import data
import play


def audio(message, wpm=35, fs=33, sps=48000, freq=900):
    play.main(message, wpm, fs, sps, freq)

class MyFrame(wx.Frame):
    count = 0
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 450))

        # Status bar
        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("CW Master by R3LO")

        # BoxSizer
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(vbox)



        # Buttons
        bStart = wx.Button(panel, label="Старт")
        bStop = wx.Button(panel, label="Стоп")
        hb3 = wx.BoxSizer()
        hb3.AddMany([(bStart, 0, wx.LEFT|wx.RIGHT, 10), (bStop, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 10)])
        vbox.Add(hb3, flag=wx.ALIGN_CENTRE)

        # Gauge
        self.gauge = wx.Gauge(panel, range=50)
        vbox.Add(self.gauge, flag=wx.EXPAND|wx.ALL, border=10)

        # Bind
        bStart.Bind(wx.EVT_BUTTON, self.onStart)
        bStop.Bind(wx.EVT_BUTTON, self.onStop)


    def onStart(self, e):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)
        wpm = 35
        call_sent = data.get_callsign(1)[0]
        serial_sent = data.get_serial(3)
        msg = call_sent + ' 5NN ' + serial_sent[1]
        audio(msg, wpm)
        #     call_recd, serial_recd = input().split()
        #     data.check_callsign(call_sent, call_recd.upper())
        #     data.check_serial(serial_sent[0], serial_recd)
        if self.count >= 50:
            print('>50')
    def onStop(self, e):
        pass



app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()


