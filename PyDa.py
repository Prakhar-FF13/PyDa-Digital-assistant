import wolframalpha
import wikipedia
import wx
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
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
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha
            app_id = ""
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print (answer)
            engine.say(answer)
            engine.runAndWait()
        except:
            #wikipedia
            try:
                answer = wikipedia.summary(input)
                print(answer)
                engine.say(answer)
                engine.runAndWait()
            except:
                print("Sorry, could not find anything. I am not that powerful.")
                engine.say("Sorry")
                engine.runAndWait()

if(__name__ == '__main__'):
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
