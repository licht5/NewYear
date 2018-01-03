# anthor:tianfeihan
import wx
def load(event):
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()


def save(event):
    file=open(filename.GetValue(),"w")
    file.write(contents.GetValue())
    file.close()

app=wx.App()
win=wx.Frame(None,title="修改文件",size=(410,335))

bkg=wx.Panel(win)

loadbtn=wx.Button(bkg,label="打开")
loadbtn.Bind(wx.EVT_BUTTON,load)

savelbtn=wx.Button(bkg,label="保存")
savelbtn.Bind(wx.EVT_BUTTON,save)

filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadbtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(savelbtn,proportion=0,flag=wx.LEFT,border=5)
vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()

