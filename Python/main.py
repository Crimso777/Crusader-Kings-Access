PATH = "C:/Users/Tomrio/Documents/Paradox Interactive/Crusader Kings III/logs/debug.log"
from ahk import AHK
from ahk.window import Window
ahk = AHK()
import pygame
import time
import re
import os
import sys
import win32api
import win32con
import win32gui
import autoit
import accessible_output2.outputs.auto

window_id = win32gui.FindWindow("SDL_app", "Crusader Kings")
win = ahk.find_window(title=b'Crusader Kings III') # Find the opened window#
#win = Window.from_pid(ahk, pid=window_id)                 # by process IDprint(window_id)
print(win.title)
#autoit.mouse_move(50,50,0)
#win.send("{F1}")

ao_output = accessible_output2.outputs.auto.Auto()

pygame.init()
pygame.display.set_caption("Crusader Kings 3 Access")
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w , infoObject.current_h ), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
#done = False
fuchsia = (255, 0, 128)  # Transparency color

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 100, win32con.LWA_ALPHA )

screen.fill(fuchsia)  # Transparent background
pygame.display.update()
#pause = input("Press enter to continue")
num_lines = 0
cursor = 0
with open(PATH) as f:
   for i, line in enumerate(f):
      num_lines = num_lines + 1  # process line i
   f.seek(0,2)
#   print(f.tell())
   cursor = f.tell()
ao_output.output("Hello Crusaders!", True)
updated = os.path.getmtime(PATH)
while True:
   if updated != os.path.getmtime(PATH):
      count = 0
      with open(PATH) as f:
         f.seek(cursor, 0)
#         cursor = f.tell()
         buffer = f.read()
         pattern = "(<out>)(..*)(</out>)"
         match = re.search(pattern, buffer)
         if match:
            ao_output.output(match.group(2), True)
         f.seek(cursor, 0)
         for i, line in enumerate(f):
            count = count + 1
         f.seek(0,2)
         cursor = f.tell()


      updated = os.path.getmtime(PATH)
      num_lines = num_lines + count
#      print(cursor)
#      print(count)
#      print(num_lines)

       
    # creating a loop to check events that
    # are occurring
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_F1 and pygame.key.get_mods() == 0 :
            win.send("{F1}")
         elif event.key == pygame.K_F2 and pygame.key.get_mods() == 0 :
            win.send("{F2}")
         elif event.key == pygame.K_F3 and pygame.key.get_mods() == 0 :
            win.send("{F3}")
         elif event.key == pygame.K_F4 and pygame.key.get_mods() == 0 :
            win.send("{F4}")
         elif event.key == pygame.K_F5 and pygame.key.get_mods() == 0 :
            win.send("{F5}")
         elif event.key == pygame.K_F6 and pygame.key.get_mods() == 0 :
            win.send("{F6}")
         elif event.key == pygame.K_F7 and pygame.key.get_mods() == 0 :
            win.send("{F7}")
         elif event.key == pygame.K_F8 and pygame.key.get_mods() == 0 :
            win.send("{F8}")
         elif event.key == pygame.K_F9 and pygame.key.get_mods() == 0 :
            win.send("{F9}")
         elif event.key == pygame.K_c and pygame.key.get_mods() == 0 :
            win.send("c")
         elif event.key == pygame.K_v and pygame.key.get_mods() == 0 :
            win.send("v")
         elif event.key == pygame.K_BACKQUOTE and pygame.key.get_mods() == 0 :
            win.send("`")
         elif event.key == pygame.K_ESCAPE and pygame.key.get_mods() == 0 :
            win.send("{ESC}")
         elif event.key == pygame.K_b and pygame.key.get_mods() == 0 :
            win.send("b")
         elif event.key == pygame.K_F9 and pygame.key.get_mods() & pygame.KMOD_CTRL:
            win.send("{CTRLDOWN}{F9}{CTRLUP}")

         elif event.key == pygame.K_e and pygame.key.get_mods() == 0 :
            win.send("e")
         elif event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_CTRL:
            win.send("{CTRLDOWN}a{CTRLUP}")
         elif event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_CTRL:
            win.send("{CTRLDOWN}a{CTRLUP}")

         elif (event.key == pygame.K_u and pygame.key.get_mods() == 0) or (event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_SHIFT):
            win.send("u")
         elif (event.key == pygame.K_i and pygame.key.get_mods() == 0) or (event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_SHIFT):
            win.send("i")
         elif (event.key == pygame.K_o and pygame.key.get_mods() == 0) or (event.key == pygame.K_e and pygame.key.get_mods() & pygame.KMOD_SHIFT):
            win.send("o")
         elif event.key == pygame.K_r and pygame.key.get_mods() == 0 :
            win.send("r")
         elif event.key == pygame.K_t and pygame.key.get_mods() == 0 :
            win.send("t")
         elif event.key == pygame.K_y and pygame.key.get_mods() == 0 :
            win.send("y")
         elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
            win.send("{CTRLDOWN}s{CTRLUP}")
         elif event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
            win.send("{CTRLDOWN}q{CTRLUP}")
         elif event.key == pygame.K_e and pygame.key.get_mods() & pygame.KMOD_CTRL:
            win.send("{CTRLDOWN}e{CTRLUP}")
         elif event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
            win.send("{CTRLDOWN}w{CTRLUP}")
#Map movement controls
         elif event.key == pygame.K_UP and pygame.key.get_mods() == 0 :
            win.send("{UP}")
         elif event.key == pygame.K_DOWN and pygame.key.get_mods() == 0 :
            win.send('hhf')  # Send keys, as if typed (performs ahk string escapes)

#            win.send("{DOWN}")
         elif event.key == pygame.K_LEFT and pygame.key.get_mods() == 0 :
#            win.send("{LEFT}")
            win.send("h")
            time.sleep(.1)
            win.send("f")
            time.sleep(.1)
            win.send("hgggghhhhghhhg")
            time.sleep(.1)
            win.send("f")

         elif event.key == pygame.K_RIGHT and pygame.key.get_mods() == 0 :
#            win.send("hgggghgghgghgg")
            win.send("hg")
            time.sleep(.1)
            win.send("f")
            time.sleep(.1)

            win.send("hgggghgghgghgg")
            time.sleep(.1)
            win.send("f")

#            win.send("{RIGHT}")
         elif event.key == pygame.K_HOME and pygame.key.get_mods() == 0 :
            win.send("{HOME}")
         elif event.key == pygame.K_PAGEUP and pygame.key.get_mods() == 0 :
            win.send("{PGUP}")
         elif event.key == pygame.K_PAGEDOWN and pygame.key.get_mods() == 0 :
            win.send("{PGDN}")
         elif event.key == pygame.K_f and pygame.key.get_mods() == 0 :
            win.send("f")
         elif event.key == pygame.K_g and pygame.key.get_mods() == 0 :
            win.send("g")
         elif event.key == pygame.K_h and pygame.key.get_mods() == 0 :
            win.send("h")
         elif event.key == pygame.K_j and pygame.key.get_mods() == 0 :
            win.send("j")
         elif event.key == pygame.K_1 and pygame.key.get_mods() == 0 :
            win.send("1")
         elif event.key == pygame.K_2 and pygame.key.get_mods() == 0 :
            win.send("2")
         elif event.key == pygame.K_3 and pygame.key.get_mods() == 0 :
            win.send("3")
         elif event.key == pygame.K_4 and pygame.key.get_mods() == 0 :
            win.send("4")
         elif event.key == pygame.K_5 and pygame.key.get_mods() == 0 :
            win.send("5")
         elif event.key == pygame.K_z and pygame.key.get_mods() == 0 :
            win.send("z")
         elif event.key == pygame.K_x and pygame.key.get_mods() == 0 :
            win.send("x")
         elif event.key == pygame.K_MINUS and pygame.key.get_mods() == 0 :
            win.send("-")
         elif event.key == pygame.K_KP_MINUS and (pygame.key.get_mods()  == 0 or (pygame.key.get_mods() & pygame.KMOD_NUM	)):
            win.send("{NUMPADSUB}")
         elif event.key == pygame.K_KP_PLUS and (pygame.key.get_mods()  == 0 or (pygame.key.get_mods() & pygame.KMOD_NUM	)):
            win.send("{NUMPADADD}")
         elif event.key == pygame.K_SPACE and pygame.key.get_mods() == 0 :
            win.send("{SPACE}")
         elif event.key == pygame.K_F11 and pygame.key.get_mods() == 0 :
            win.send("{F11}")
         elif event.key == pygame.K_F11 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
            win.send("{SHIFTDOWN}{F11}{SHIFTUP}")
         elif event.key == pygame.K_F12 and pygame.key.get_mods() == 0 :
            win.send("{F12}")

      elif event.type == pygame.MOUSEBUTTONDOWN :
         if event.button == 1:
#            autoit.control_click_by_handle(window_id, window_id, button = 'left')
         elif event.button == 3:
#            autoit.control_click_by_handle(window_id, window_id, button = 'right')
            
      elif event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()