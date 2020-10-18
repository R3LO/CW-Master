import wx

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
        if self.count >= 50:
            print('>50')
    def onStop(self, e):
        pass

app = wx.App()
frame = MyFrame(None, 'wxPython')
frame.Show()
app.MainLoop()


