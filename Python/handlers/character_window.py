import wx
import config
ao_output = config.ao_output
win = config.win

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

#input handler for character window:
#dir represents a direction to navigate.  0 = up, 1 = right, 2 = down, 3 = left
def character_window_navigate(dir):
    selection = config.selection
    chars = config.chars
    labels = config.labels
    tabs = config.tabs

    result = ""
    if selection[1] == 0 or selection[2] == 0:
        selection[1] = 1
        selection[2] = 1
        print(len(chars[selection[0]]))
        result = result + chars[selection[0]]["table"][selection[1]][0] + ", "
        result = result + chars[selection[0]]["table"][0][selection[2]]+ ": "
        result = result + chars[selection[0]]["table"][selection[1]][selection[2]]
        print(str(selection[0]) + ", " + str(selection[1]) + ", " + str(selection[2]))
        ao_output.output(result, True)
        return
       
    elif dir == 0 and selection[1] > 1:
        selection[1] = selection[1] - 1
    elif dir == 1 and selection[2] < len(chars[selection[0]]["table"][selection[1]])-1:
        selection[2] = selection[2] + 1
    elif dir == 2 and selection[1] < len(chars[selection[0]]["table"])-1:
        selection[1] = selection[1] + 1
    elif dir == 3 and selection[2] > 1:
        selection[2] = selection[2] - 1
    if dir%2 == 0:
        result = result + chars[selection[0]]["table"][selection[1]][0] + ", "
    result = result + chars[selection[0]]["table"][0][selection[2]] + ": "
    result = result + chars[selection[0]]["table"][selection[1]][selection[2]]
    print(str(selection[0]) + ", " + str(selection[1]) + ", " + str(selection[2]))
        
    ao_output.output(result, True)

#menu navigation tab switch
#reverse means shift is held down, and the tabs will run in reverse
def character_window_tab(reverse = False):
    selection = config.selection
    chars = config.chars
    labels = config.labels
    tabs = config.tabs
    selection[1] = 0
    selection[2] = 0
    if reverse == False:
        selection[0] = selection[0] + 1
        if selection[0] >= len(chars):
            selection[0] = 0
    else:
        selection[0] = selection[0] - 1
        if selection[0] < 0:
            selection[0] = len(chars) - 1
    ao_output.output(chars[selection[0]]["name"], True)
def character_window_click():
    selection = config.selection
    chars = config.chars
    labels = config.labels
    tabs = config.tabs
    if selection[1] == 0 or selection[2] == 0:
        return
    id = chars[selection[0]]["table"][selection[1]][-1]
    id = str(bin(int(id)))
    id = id[2:]
    id = id.replace('0', 'g')
    id = id.replace('1', 'h')
    command = "hf" + id + "f"
    win.send(command)
