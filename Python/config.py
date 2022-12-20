from ahk import AHK
from ahk.window import Window
ahk = AHK()

win = ahk.win_get(title='Crusader Kings III')  # by title
win.send("j")

import accessible_output2.outputs.auto
ao_output = accessible_output2.outputs.auto.Auto()

chars = []
selection = []
labels = []
tabs = []
tags = ["consorts", "heirs", "lieges", "family", "courtiers", "vassals"]
