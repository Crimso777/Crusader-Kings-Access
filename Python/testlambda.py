import accessible_output2.outputs.auto
ao_output = accessible_output2.outputs.auto.Auto()
import wx
import os
import json

cwd = os.getcwd()
settings_path = os.path.join(cwd, "settings.json")
if not (os.path.isfile(settings_path)):
    dict = {"path": ""}
    json_object = json.dumps(dict, indent=4)
    with open("settings.json", "w") as outfile:
        outfile.write(json_object)

with open('settings.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    path = json_object["path"]
actions = {}
actions[65] = lambda: ao_output.output("Hello A-Key!", True)
actions[66] = lambda: ao_output.output("Hello B-Key!", True)
actions[67] = lambda: ao_output.output("Hello C-Key!", True)
actions[68] = lambda: ao_output.output("Hello D-Key!", True)
actions[69] = lambda: ao_output.output("Hello E-Key!", True)
actions[70] = lambda: ao_output.output("Hello F-Key!", True)
actions[71] = lambda: ao_output.output("Hello G-Key!", True)
actions[72] = lambda: ao_output.output("Hello H-Key!", True)
actions[73] = lambda: ao_output.output("Hello I-Key!", True)
actions[74] = lambda: ao_output.output("Hello J-Key!", True)
actions[75] = lambda: ao_output.output("Hello K-Key!", True)
actions[76] = lambda: ao_output.output("Hello L-Key!", True)
actions[77] = lambda: ao_output.output("Hello M-Key!", True)
actions[78] = lambda: ao_output.output("Hello N-Key!", True)
actions[79] = lambda: ao_output.output("Hello O-Key!", True)
actions[80] = lambda: ao_output.output("Hello P-Key!", True)
actions[81] = lambda: ao_output.output("Hello Q-Key!", True)
actions[82] = lambda: ao_output.output("Hello R-Key!", True)
actions[83] = lambda: ao_output.output("Hello S-Key!", True)
actions[84] = lambda: ao_output.output("Hello T-Key!", True)
actions[85] = lambda: ao_output.output("Hello U-Key!", True)
actions[86] = lambda: ao_output.output("Hello V-Key!", True)
actions[87] = lambda: ao_output.output("Hello W-Key!", True)
actions[88] = lambda: ao_output.output("Hello X-Key!", True)
actions[89] = lambda: ao_output.output("Hello Y-Key!", True)
actions[90] = lambda: ao_output.output("Hello Y-Key!", True)
actions[wx.WXK_ESCAPE] = lambda: frame.Close()
control_actions = {}
control_actions[65] = lambda: ao_output.output("Hello A-Key!", True)
control_actions[69] = lambda: ao_output.output("Hello E-Key!", True)
control_actions[81] = lambda: ao_output.output("Hello Q-Key!", True)
control_actions[83] = lambda: ao_output.output("Hello S-Key!", True)
control_actions[87] = lambda: ao_output.output("Hello W-Key!", True)
control_actions[wx.WXK_F9] = lambda: ao_output.output("Hello F9!", True)
shift_actions = {}
shift_actions[69] = lambda: ao_output.output("Hello E-Key!", True)
shift_actions[81] = lambda: ao_output.output("Hello Q-Key!", True)
shift_actions[87] = lambda: ao_output.output("Hello W-Key!", True)

handler = {}
handler[wx.MOD_NONE] = actions
handler[wx.MOD_CONTROL] = control_actions
handler[wx.MOD_SHIFT] = shift_actions
########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
#        self.Bind(wx.EVT_CHAR, self.onKey)

    #----------------------------------------------------------------------
    def onKey(self, event):
        """
        Check for ESC key press and exit is ESC is pressed
        """
        key_code = event.GetKeyCode()
        mods = event.GetModifiers()
        if mods in handler and key_code in handler[mods]:
            handler[mods][key_code]()
#        if not(event.HasAnyModifiers()):
#            try:
#                actions[key_code](self)
#            except:
#                pass
##            self.GetParent().Close()
#        elif event.GetModifiers() == wx.MOD_CONTROL:
#            try:
#                control_actions[key_code]()
#            except:
#                pass
#        elif event.GetModifiers() == wx.MOD_SHIFT:
#            try:
#                shift_actions[key_code]()
#            except:
#                pass

        else:
            event.Skip()


########################################################################
class MyFrame(wx.Frame):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Test FullScreen")
        panel = MyPanel(self)
        self.ShowFullScreen(True)
        self.SetTransparent(1)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    if not(os.path.isfile(path) and os.path.basename(path) == "debug.log"):
# Create open file dialog
        openFileDialog = wx.FileDialog(frame, "Open", "", "",
          "Log files (*.log)|*.log",
           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        path = openFileDialog.GetPath()
        openFileDialog.Destroy()
    if os.path.isfile(path) and os.path.basename(path) == "debug.log":
        with open('settings.json', 'r') as openfile:
            settings = json.load(openfile)
        settings["path"] = path
        json_object = json.dumps(settings, indent=4)

        with open("settings.json", "w") as outfile:
            outfile.write(json_object)
        app.MainLoop()
