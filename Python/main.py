from ahk import AHK
from ahk.window import Window
ahk = AHK()
win = ahk.win_get(title='Crusader Kings III')  # by title
import time
import re
import os
import sys
import copy
import threading
import win32api
import win32con
import win32gui
import accessible_output2.outputs.auto
ao_output = accessible_output2.outputs.auto.Auto()
import wx
import os
import json
chars = []
selection = []
labels = []
tabs = []
tags = ["consorts", "heirs", "lieges", "family", "courtiers", "vassals"]
def layer_controls(top, bottom):
    result = copy.deepcopy(bottom)
    for mod in top:
        for key in top[mod]:
            result[mod][key] = top[mod][key]
            print(key)
    return result
def read_loop():
    cursor = 0
    prev = ""
    with open(path) as f:
        f.seek(0,2)
        print(f.tell())
        cursor = f.tell()
    updated = os.path.getmtime(path)
    while True:
        time.sleep(.01)
        if updated != os.path.getmtime(path):
            with open(path) as f:
                f.seek(cursor, 0)
                buffer = f.read()
#                if len(prev) == 0: #case where there is no prior starting tag
                if True:
#out tag
                    pattern1 = "(<out>)(.*?)(</out>)(.*?)"
                    match1 = re.search(pattern1, buffer, flags = re.DOTALL)
                    if match1:
                        ao_output.output(match1.group(2), True)
#character window
                    pattern2 = "(<CharacterWindow>)(.*?)(</CharacterWindow>)"
                    match2 = re.search(pattern2, buffer, flags = re.DOTALL)

                    if match2:
                        global chars            
                        chars = []
                        global selection
                        selection = [0,0,0]
                        global labels
                        labels = ["Name", "Age", "Health", "Faith", "Religion", "Culture", "Culture-Group", "Marital Status", "Relationship to selected character", "Opinion of selected character", "Opinion Breakdown", "ID"] 
                        global tabs
                        tabs = []
                        global handler
                        handler = layer_controls(menu_handler, handler)
                        for tag in tags:
                            open_tag = "<"+tag+">"
                            close_tag = "</"+tag+">"
                            tab_pattern = open_tag + "(.*?)" + close_tag
                            tab_match = re.search(tab_pattern, match2.group(2), flags = re.DOTALL)
                            if tab_match:
                                pattern3 = "(<char>)(.*?)(</char>)"
                                matches = re.findall(pattern3, tab_match.group(1), flags = re.DOTALL)
                                if len(matches) > 0:
                                    chars.append([])
                                    tabs.append(tag)
                                    for match in matches:
                                        pattern = "<name>(.*?)</name><age>(.*?)</age><health>(.*?)</health><faith>(.*?)</faith><religion>(.*?)</religion><culture>(.*?)</culture><culture_group>(.*?)</culture_group><marital_status>(.*?)</marital_status><relation>(.*?)</relation><opinion>(.*?)</opinion><opinion_breakdown>(.*?)</opinion_breakdown><id>(.*?)</id>"
                                        char = re.search(pattern, match[1], flags = re.DOTALL)
                                        if char:
                                            chars[-1].append(char)
                                        else:
                                            print(match[1])
                        print("Character Window Found")
                        print(len(chars))
#                        print(chars[0].group(1))
   
#                        print(chars[0][1])


#partial match with opening tag but no closing tag
#                    else: 
#                        pattern = "(<out>)(.*)"
#                        match = re.search(pattern, buffer)
#                        if match:
#                            prev = match.group(2)
                f.seek(0,2)
                cursor = f.tell()

            updated = os.path.getmtime(path)


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
actions[wx.WXK_TAB] = lambda: ao_output.output("Current Situation", True)
actions[32] = lambda: ao_output.output("Pause or Unpause", True)
actions[49] = lambda: ao_output.output("Slowest", True)
actions[50] = lambda: ao_output.output("Slow", True)
actions[51] = lambda: ao_output.output("Normal", True)
actions[52] = lambda: ao_output.output("Fast", True)
actions[53] = lambda: ao_output.output("Fastest", True)
actions[67] = lambda: ao_output.output("Character finder", True)
actions[69] = lambda: ao_output.output("Realms view", True)
actions[73] = lambda: ao_output.output("Kingdom titles", True)
actions[79] = lambda: ao_output.output("Empire titles", True)
actions[82] = lambda: ao_output.output("Faiths view", True)
actions[84] = lambda: ao_output.output("Cultures", True)
actions[85] = lambda: ao_output.output("Duchy titles", True)
actions[86] = lambda: ao_output.output("Find title", True)
actions[88] = lambda: ao_output.output("Game speed faster", True)
actions[89] = lambda: ao_output.output("Houses", True)
actions[90] = lambda: ao_output.output("Game speed slower", True)
actions[wx.WXK_F1] = lambda: ao_output.output("Open Character window", True)
actions[wx.WXK_F2] = lambda: ao_output.output("Open domain window", True)
actions[wx.WXK_F3] = lambda: ao_output.output("Open military window", True)
actions[wx.WXK_F4] = lambda: ao_output.output("Open council window", True)
actions[wx.WXK_F5] = lambda: ao_output.output("Open courtiers window", True)
actions[wx.WXK_F6] = lambda: ao_output.output("Open intrigues window", True)
actions[wx.WXK_F7] = lambda: ao_output.output("Open decisions window", True)
actions[wx.WXK_ESCAPE] = lambda: frame.Close()
# Army keybinds
actions[70] = lambda: ao_output.output("Split in half", True)
actions[71] = lambda: ao_output.output("Merge.", True)
actions[72] = lambda: ao_output.output("Split off new Army.", True)
actions[74] = lambda: ao_output.output("Disband.", True)
#Camera controls
actions[wx.WXK_LEFT] = lambda: ao_output.output("Move Camera Left", True)
actions[wx.WXK_UP] = lambda: ao_output.output("Move Camera Up", True)
actions[wx.WXK_DOWN] = lambda: ao_output.output("Move Camera Down", True)
actions[wx.WXK_RIGHT] = lambda: ao_output.output("Move Camera Right", True)
actions[65] = lambda: ao_output.output("Move Camera Left", True)
actions[87] = lambda: ao_output.output("Move Camera Up", True)
actions[83] = lambda: ao_output.output("Move Camera Down", True)
actions[68] = lambda: ao_output.output("Move Camera Right", True)

control_actions = {}
control_actions[65] = lambda: ao_output.output("Counties", True)
control_actions[69] = lambda: ao_output.output("Terrain", True)
control_actions[81] = lambda: ao_output.output("Governments", True)
control_actions[83] = lambda: ao_output.output("Players", True)
control_actions[87] = lambda: ao_output.output("Developments", True)
control_actions[wx.WXK_F9] = lambda: ao_output.output("Hide User Interface", True)
shift_actions = {}
shift_actions[69] = lambda: ao_output.output("Empire Titles", True)
shift_actions[81] = lambda: ao_output.output("Duchy titles", True)
shift_actions[87] = lambda: ao_output.output("Kingdom Titles", True)

help_handler = {}
help_handler[wx.MOD_NONE] = actions
help_handler[wx.MOD_CONTROL] = control_actions
help_handler[wx.MOD_SHIFT] = shift_actions
ptactions = {}
ptactions[wx.WXK_F1] = lambda: win.send("{F1}")
ptactions[wx.WXK_F2] = lambda: win.send("{F2}")
ptactions[wx.WXK_F3] = lambda: win.send("{F3}")
ptactions[wx.WXK_F4] = lambda: win.send("{F4}")
ptactions[wx.WXK_F5] = lambda: win.send("{F5}")
ptactions[wx.WXK_F6] = lambda: win.send("{F6}")
ptactions[wx.WXK_F7] = lambda: win.send("{F7}")
ptactions[wx.WXK_TAB] = lambda: win.send("{TAB}")
#ASCII Keybinds
#For these do we need syntax win.send('A') or win.send("{A}") works?
#Not sure if win.send supports ASCII values, can't find online
ptactions[32] = lambda: win.send("{SPACE}")
ptactions[49] = lambda: win.send("{1}")
ptactions[50] = lambda: win.send("{2}")
ptactions[51] = lambda: win.send("{3}")
ptactions[52] = lambda: win.send("{4}")
ptactions[53] = lambda: win.send("{5}")
ptactions[67] = lambda: win.send("{C}")
ptactions[69] = lambda: win.send("{E}")
ptactions[73] = lambda: win.send("{I}")
ptactions[79] = lambda: win.send("{O}")
ptactions[82] = lambda: win.send("{R}")
ptactions[84] = lambda: win.send("{T}")
ptactions[85] = lambda: win.send("{U}")
ptactions[86] = lambda: win.send("{V}")
ptactions[88] = lambda: win.send("{X}")
ptactions[89] = lambda: win.send("{Y}")
ptactions[90] = lambda: win.send("{Z}")
#Army ptactions
ptactions[70] = lambda: win.send("{F}")
ptactions[71] = lambda: win.send("{G}")
ptactions[72] = lambda: win.send("{H}")
ptactions[74] = lambda: win.send("{J}")
#Camera ptactions
ptactions[wx.WXK_LEFT] = lambda: win.send("{LEFT}")
ptactions[wx.WXK_UP] = lambda: win.send("{UP}")
ptactions[wx.WXK_DOWN] = lambda: win.send("{DOWN}")
ptactions[wx.WXK_RIGHT] = lambda: win.send("{RIGHT}")
ptactions[65] = lambda: win.send("{A}")
ptactions[87] = lambda: win.send("{W}")
ptactions[83] = lambda: win.send("{S}")
ptactions[68] = lambda: win.send("{D}")

shift_ptactions = {}
#Shift ptactions
#What's syntax for SHIFT and CONTROL actions with win API?

control_ptactions = {}
#Control ptactions

pthandler = {}
pthandler[wx.MOD_NONE] = ptactions
pthandler[wx.MOD_CONTROL] = control_ptactions
pthandler[wx.MOD_SHIFT] = shift_ptactions

handler = copy.deepcopy(pthandler)
handler[wx.MOD_NONE][84] = lambda: win.send("hhf")
#menu input handler
menu_actions = {}
menu_actions[65] = lambda: character_window_navigate(3)
menu_actions[87] = lambda: character_window_navigate(0)
menu_actions[83] = lambda: character_window_navigate(2)
menu_actions[68] = lambda: character_window_navigate(1)
menu_actions[wx.WXK_TAB] = lambda: character_window_tab()
menu_actions[91] = lambda: character_window_click()

menu_shift_actions = {}
menu_shift_actions[wx.WXK_TAB] = lambda: character_window_tab(reverse = True)

menu_handler = {}
menu_handler[wx.MOD_NONE] = menu_actions
menu_handler[wx.MOD_CONTROL] = {}
menu_handler[wx.MOD_SHIFT] = menu_shift_actions

#handler = copy.deepcopy(help_handler)
#input handler for character window:
#dir represents a direction to navigate.  0 = up, 1 = right, 2 = down, 3 = left
def character_window_navigate(dir):
    result = ""
    global selection
    global chars
    global labels
    if selection[1] == 0 or selection[2] == 0:
        selection[1] = 1
        selection[2] = 1
        result = result + chars[selection[0]][selection[1]-1].group(1) + ", "
        result = result + labels[selection[2]] + ": "
        result = result + chars[selection[0]][selection[1]-1].group(selection[2]+1)
        
        ao_output.output(result, True)
        return
       
    elif dir == 0 and selection[1] > 1:
        selection[1] = selection[1] - 1
    elif dir == 1 and selection[2] < len(chars[selection[0]][selection[1]-1].groups())-1:
        selection[2] = selection[2] + 1
    elif dir == 2 and selection[1] < len(chars[selection[0]]):
        selection[1] = selection[1] + 1
    elif dir == 3 and selection[2] > 1:
        selection[2] = selection[2] - 1
    if dir%2 == 0:
        result = result + chars[selection[0]][selection[1]-1].group(1) + ", "
    result = result + labels[selection[2]] + ": "
    result = result + chars[selection[0]][selection[1]-1].group(selection[2]+1)
        
    ao_output.output(result, True)

#menu navigation tab switch
#reverse means shift is held down, and the tabs will run in reverse
def character_window_tab(reverse = False):
    global selection
    global tabs
    selection[1] = 0
    selection[2] = 0
    if reverse == False:
        selection[0] = selection[0] + 1
        if selection[0] >= len(tabs):
            selection[0] = 0
    else:
        selection[0] = selection[0] - 1
        if selection[0] < 0:
            selection[0] = len(tabs) - 1
    ao_output.output(tabs[selection[0]], True)
def character_window_click():
    global chars
    global selection
    if selection[1] == 0 or selection[2] == 0:
        return
    id = chars[selection[0]][selection[1]-1].group(12)
    id = str(bin(int(id)))
    id = id[2:]
    id = id.replace('0', 'g')
    id = id.replace('1', 'h')
    command = "hf" + id + "f"
    win.send(command)

#########################################################################
class MyPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent, style = wx.WANTS_CHARS)
        
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
        t1 = threading.Thread(target=read_loop, args=())
        t1.daemon = True  # thread dies with the program
        t1.start()
        ao_output.output("Hello Crusaders!", True)
        app.MainLoop()
