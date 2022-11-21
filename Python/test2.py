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
actions[wx.WXK_ESCAPE] = lambda: frame.Close()
#actions[wx.WXK_TAB] = lambda: ao_output.output("Hi!", True)
#actions[wx.WXK_TAB] = labda: ao_output.output("Hi!")
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
shift_actions[32] = lambda: ao_output.output("Hello Space-Key!", True)


########################################################################
# Shane's test code
#actions[9] = lambda: ao_output.output("Tab key works!", True)
alt_actions = {}
#handler[wx.MOD_NONE] = test_actions
ao_output.output("Welcome to crusader kings")
alt_actions[wx.WXK_SPACE] = lambda: ao_output.output("Space key works!", True)
alt_actions[32] = lambda: ao_output.output("Space key works!", True)
alt_actions[wx.WXK_SPACE] = lambda: print("Space key pressed!", True)
alt_actions[82] = lambda: ao_output.output("Faiths shown.", True)
alt_actions[67] = lambda: ao_output.output("Character finder.", True)
alt_actions[9] = lambda: ao_output.output("Issues.", True)
alt_actions[66] = lambda: ao_output.output("Back.", True)
alt_actions[wx.WXK_F1] = lambda: ao_output.output("Player character guide.", True)
alt_actions[wx.WXK_F2] = lambda: ao_output.output("Realm.", True)
alt_actions[wx.WXK_F3] = lambda: ao_output.output("Military (Warfare, Army, Hired Forces).", True)
alt_actions[wx.WXK_F4] = lambda: ao_output.output("Council.", True)
alt_actions[wx.WXK_F5] = lambda: ao_output.output("Court (Prisoners)", True)
alt_actions[wx.WXK_F6] = lambda: ao_output.output("Intruige (Schemes, Hooks, Secrets)", True)
alt_actions[wx.WXK_F7] = lambda: ao_output.output("Factions", True)
alt_actions[wx.WXK_F8] = lambda: ao_output.output("Decisions", True)
alt_actions[84] = lambda: ao_output.output("Cultures shown.", True)
alt_actions[89] = lambda: ao_output.output("Houses shown.", True)
#TODO: Find out how the EVT_KEY_DOWN key events work so I can
# bind keys such as ones you need to hold one key and press another such as
# Cntrl S for governments etc. Maybe we use MOD_CONTROL for these keys?
# Need to figure out how to the key presses to work first without requiring a control, shift, alt etc.

# Army keybinds
alt_actions[70] = lambda: ao_output.output("Split in half", True)
alt_actions[71] = lambda: ao_output.output("Merge.", True)
alt_actions[72] = lambda: ao_output.output("Split off new Army.", True)
alt_actions[73] = lambda: ao_output.output("Disband.", True)

# How to have keys able to pressed without CONTROL,SHIFT, ALT etc?
# Doesn't seem to work when I use MOD_ALL or MOD_NONE
# - Shane
handler = {}
handler[wx.MOD_NONE] = actions
handler[wx.MOD_CONTROL] = control_actions
handler[wx.MOD_SHIFT] = shift_actions
handler[wx.MOD_ALT] = alt_actions

#########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        
        self.Bind(wx.EVT_KEY_DOWN, self.onKey)
#       button = wx.Button(self, label="Test Shift")
#       button.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
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
        wx.Frame.__init__(self, None, title="Mod screen test")
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
