import wolframalpha
import wikipedia
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,size
        pos=wx.DefaultPosition, size=wx.Size(450, 100),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
        wx.CLOSE_BOX | wx.CLIP_CHILDREN,
        title="PyDa")

        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="This is PyDa, Python virtual Assistant. Write a Question.")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER, size=(400, 30))

while(True):
    inp = input("Question: ")
    try:
        #wolframalpha
        app_id = "XJ3PJW-WJHQH7UTQG"
        client = wolframalpha.Client(app_id)
        res = client.query(inp)
        answer = next(res.results).text
        print (answer)
    except:
        #wikipedia
        try:
            print(wikipedia.summary(inp))
        except:
            print("Could not find anything related, Sorry, i am not that powerful.")
