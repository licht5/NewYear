import wx
app=wx.App()
win=wx.Frame(None,title="test")
savebtn=wx.Button(win,label="save")
cancelbtn=wx.Button(win,label="cancel")
win.Show()
app.MainLoop()

