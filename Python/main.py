import config
win = config.win
import time
import re
import os
import sys
import copy
import threading
import win32api
import win32con
import win32gui
import wx
import os
import json

def build_table(buffer, interface):
    result = []
    open_tag = "<"+interface["tag"]+">"
    close_tag = "</"+interface["tag"]+">"
    pattern1 = open_tag + "(.*?)" + close_tag
    match1 = re.search(pattern1, buffer, flags = re.DOTALL)
    if match1:
        rows = []
        rows.append([interface["row_title"]])
        for col in interface["columns"]:
            rows[0].append(col["name"])
        if "categories" in interface and len(interface["categories"]) > 0:
            for category in interface["categories"]:
                open_tag = "<"+ category["tag"] +">"
                close_tag = "</"+ category["tag"]+">"
                pattern2 = open_tag + "(.*?)" + close_tag
                match2 = re.search(pattern2, match1.group(1), flags = re.DOTALL)
                if match2:
                    open_tag = "<"+ interface["rows"] +">"
                    close_tag = "</"+ interface["rows"] +">"
                    pattern3 = open_tag + "(.*?)" + close_tag
                    matches = re.findall(pattern3, match2.group(1), flags = re.DOTALL)
                    for match in matches:
                        rows.append([])
                        open_tag = "<"+ interface["row_title"] +">"
                        close_tag = "</"+ interface["row_title"] +">"
                        pattern4 = open_tag + "(.*?)" + close_tag
                        match4 = re.search(pattern4, match, flags = re.DOTALL)
                        rows[-1].append(category["name"] + ", " +match4.group(1))

                        for col in interface["columns"]:
                            open_tag = "<"+ col["tag"] +">"
                            close_tag = "</"+ col["tag"] +">"
                            pattern4 = open_tag + "(.*?)" + close_tag
                            match4 = re.search(pattern4, match, flags = re.DOTALL)
                            rows[-1].append(match4.group(1))
        else:
            open_tag = "<"+ interface["rows"] +">"
            close_tag = "</"+ interface["rows"] +">"
            pattern3 = open_tag + "(.*?)" + close_tag
            matches = re.findall(pattern3, match1.group(1), flags = re.DOTALL)
            for match in matches:
                rows.append([])
                open_tag = "<"+ interface["row_title"] +">"
                close_tag = "</"+ interface["row_title"] +">"
                pattern4 = open_tag + "(.*?)" + close_tag
                match4 = re.search(pattern4, match, flags = re.DOTALL)
                rows[-1].append(match4.group(1))
                for col in interface["columns"]:
                    open_tag = "<"+ col["tag"] +">"
                    close_tag = "</"+ col["tag"] +">"
                    pattern4 = open_tag + "(.*?)" + close_tag
                    match4 = re.search(pattern4, match, flags = re.DOTALL)
                    rows[-1].append(match4.group(1))
        if len(rows) > 1:
            result = rows
    return result
    
def layer_controls(top, bottom):
    result = copy.deepcopy(bottom)
    for mod in top:
        for key in top[mod]:
            result[mod][key] = top[mod][key]
            print(key)
    return result
def read_loop():
    interface = []
    with open('interface.json', 'r') as openfile: 
        interface = json.load(openfile)
    ao_output = config.ao_output
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
            with open(path, encoding='latin-1') as f:
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
                    for i in interface:    
                        open_tag = "<"+i["tag"]+">"
                        close_tag = "</"+i["tag"]+">"
                        pattern2 = open_tag + "(.*?)" + close_tag
                        match2 = re.search(pattern2, buffer, flags = re.DOTALL)

                        if match2:
                            chars = config.chars = []
                            selection = config.selection = [0,0,0]
                            labels = config.labels = ["Name", "gender", "Age", "Health", "Faith", "Religion", "Culture", "Culture-Group", "Marital Status", "relationship to player character", "opnion of player character", "opinion breakdown of player character", "Relationship to selected character", "Opinion of selected character", "Opinion Breakdown of selected character", "ID"] 
                            tabs = config.tabs = []
                            tags = config.tags
                            for i1 in i["tabs"]:
                                print(i1)
                                table = build_table(buffer, i1)
                                if len(table) > 0:
                                    chars.append({"name": i1["name"], "table": table})
                            global handler
                            new_module = __import__("character_window")
                            handler = layer_controls(new_module.menu_handler, handler)

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
sys.path.append(os.path.join(cwd, "handlers"))
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
ptactions[32] = lambda: win.send("{SPACE}")
ptactions[49] = lambda: win.send("1")
ptactions[50] = lambda: win.send("2")
ptactions[51] = lambda: win.send("3")
ptactions[52] = lambda: win.send("4")
ptactions[53] = lambda: win.send("5")
ptactions[67] = lambda: win.send("c")
ptactions[69] = lambda: win.send("e")
ptactions[73] = lambda: win.send("i")
ptactions[79] = lambda: win.send("o")
ptactions[82] = lambda: win.send("r")
ptactions[84] = lambda: win.send("t")
ptactions[85] = lambda: win.send("u")
ptactions[86] = lambda: win.send("v")
ptactions[88] = lambda: win.send("x")
ptactions[89] = lambda: win.send("y")
ptactions[90] = lambda: win.send("z")
#Army ptactions
ptactions[70] = lambda: win.send("f")
ptactions[71] = lambda: win.send("g")
ptactions[72] = lambda: win.send("h")
ptactions[74] = lambda: win.send("j")
#Camera ptactions
ptactions[wx.WXK_LEFT] = lambda: win.send("{LEFT}")
ptactions[wx.WXK_UP] = lambda: win.send("{UP}")
ptactions[wx.WXK_DOWN] = lambda: win.send("{DOWN}")
ptactions[wx.WXK_RIGHT] = lambda: win.send("{RIGHT}")
ptactions[65] = lambda: win.send("a")
ptactions[87] = lambda: win.send("w")
ptactions[83] = lambda: win.send("s")
ptactions[68] = lambda: win.send("d")
shift_ptactions = {}
control_ptactions = {}
pthandler = {}
pthandler[wx.MOD_NONE] = ptactions
pthandler[wx.MOD_CONTROL] = control_ptactions
pthandler[wx.MOD_SHIFT] = shift_ptactions

handler = copy.deepcopy(pthandler)
handler[wx.MOD_NONE][84] = lambda: win.send("hhf")
#menu input handler

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
        config.ao_output.output("Hello Crusaders!", True)
        app.MainLoop()
