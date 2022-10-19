PATH = input("Enter absolute path to your debug.log file:   ")
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

window_id = win32gui.FindWindow("SDL_app", "Crusader Kings III")
print(window_id)
#autoit.mouse_move(50,50,0)
#autoit.control_send_by_handle(window_id, window_id, "{F1}")

ao_output = accessible_output2.outputs.auto.Auto()

pygame.init()
pygame.display.set_caption("Crusader Kings 3 Access")
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w , infoObject.current_h ), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 1, win32con.LWA_ALPHA )

screen.fill(fuchsia)  # Transparent background
pygame.display.update()
#pause = input("Press enter to continue")
num_lines = 0
with open(PATH) as f:
   for i, line in enumerate(f):
      num_lines = num_lines + 1  # process line i
   f.seek(0,2)
   print(f.tell())
   cursor = f.tell()
ao_output.output("Hello Crusaders!", True)
updated = os.path.getmtime(PATH)
while True:
   if updated != os.path.getmtime(PATH):
      count = 0
      with open(PATH) as f:
         f.seek(cursor, 0)
         buffer = f.read()
         pattern = "(<out>)(..*)(</out>)"
         match = re.search(pattern, buffer)
         if match:
            ao_output.output(match.group(2), True)
         f.seek(cursor, 0)
         for i, line in enumerate(f):
            count = count + 1
         f.seek(0,2)

      updated = os.path.getmtime(PATH)
      num_lines = num_lines + count
      print(count)
      print(num_lines)




       
    # creating a loop to check events that
    # are occurring
   for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_F1 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F1}")
         elif event.key == pygame.K_F2 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F2}")
         elif event.key == pygame.K_F3 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F3}")
         elif event.key == pygame.K_F4 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F4}")
         elif event.key == pygame.K_F5 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F5}")
         elif event.key == pygame.K_F6 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F6}")
         elif event.key == pygame.K_F7 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F7}")
         elif event.key == pygame.K_F8 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F8}")
         elif event.key == pygame.K_F9 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F9}")
         elif event.key == pygame.K_c and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "c")
         elif event.key == pygame.K_v and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "v")
         elif event.key == pygame.K_BACKQUOTE and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "`")
         elif event.key == pygame.K_ESCAPE and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{ESC}")
         elif event.key == pygame.K_b and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "b")
         elif event.key == pygame.K_F9 and pygame.key.get_mods() & pygame.KMOD_CTRL:
            autoit.control_send_by_handle(window_id, window_id, "{CTRLDOWN}{F9}{CTRLUP}")

         elif event.key == pygame.K_e and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "e")
         elif event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_CTRL:
            autoit.control_send_by_handle(window_id, window_id, "{CTRLDOWN}a{CTRLUP}")
         elif event.key == pygame.K_a and pygame.key.get_mods() & pygame.KMOD_CTRL:
            autoit.control_send_by_handle(window_id, window_id, "{CTRLDOWN}a{CTRLUP}")

         elif (event.key == pygame.K_u and pygame.key.get_mods() == 0) or (event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_SHIFT):
            autoit.control_send_by_handle(window_id, window_id, "u")
         elif (event.key == pygame.K_i and pygame.key.get_mods() == 0) or (event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_SHIFT):
            autoit.control_send_by_handle(window_id, window_id, "i")
         elif (event.key == pygame.K_o and pygame.key.get_mods() == 0) or (event.key == pygame.K_e and pygame.key.get_mods() & pygame.KMOD_SHIFT):
            autoit.control_send_by_handle(window_id, window_id, "o")
         elif event.key == pygame.K_r and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "r")
         elif event.key == pygame.K_t and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "t")
         elif event.key == pygame.K_y and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "y")
         elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
            autoit.control_send_by_handle(window_id, window_id, "{CTRLDOWN}s{CTRLUP}")
         elif event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL:
            autoit.control_send_by_handle(window_id, window_id, "{CTRLDOWN}q{CTRLUP}")
         elif event.key == pygame.K_e and pygame.key.get_mods() & pygame.KMOD_CTRL:
            autoit.control_send_by_handle(window_id, window_id, "{CTRLDOWN}e{CTRLUP}")
         elif event.key == pygame.K_w and pygame.key.get_mods() & pygame.KMOD_CTRL:
            autoit.control_send_by_handle(window_id, window_id, "{CTRLDOWN}w{CTRLUP}")
#Map movement controls
         elif event.key == pygame.K_UP and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{UP}")
         elif event.key == pygame.K_DOWN and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{DOWN}")
         elif event.key == pygame.K_LEFT and pygame.key.get_mods() == 0 :
#            autoit.control_send_by_handle(window_id, window_id, "{LEFT}")
            autoit.control_send_by_handle(window_id, window_id, "hgggghhhhghhhg")
            time.sleep(.01)
#            autoit.control_send_by_handle(window_id, window_id, "j")

         elif event.key == pygame.K_RIGHT and pygame.key.get_mods() == 0 :
#            autoit.control_send_by_handle(window_id, window_id, "hgggghgghgghggj")
            autoit.control_send_by_handle(window_id, window_id, "hgggghgghgghgg")
            time.sleep(.01)
            autoit.control_send_by_handle(window_id, window_id, "f")

#            autoit.control_send_by_handle(window_id, window_id, "{RIGHT}")
         elif event.key == pygame.K_HOME and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{HOME}")
         elif event.key == pygame.K_PAGEUP and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{PGUP}")
         elif event.key == pygame.K_PAGEDOWN and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{PGDN}")
         elif event.key == pygame.K_f and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "f")
         elif event.key == pygame.K_g and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "g")
         elif event.key == pygame.K_h and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "h")
         elif event.key == pygame.K_j and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "j")
         elif event.key == pygame.K_1 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "1")
         elif event.key == pygame.K_2 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "2")
         elif event.key == pygame.K_3 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "3")
         elif event.key == pygame.K_4 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "4")
         elif event.key == pygame.K_5 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "5")
         elif event.key == pygame.K_z and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "z")
         elif event.key == pygame.K_x and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "x")
         elif event.key == pygame.K_MINUS and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "-")
         elif event.key == pygame.K_KP_MINUS and (pygame.key.get_mods()  == 0 or (pygame.key.get_mods() & pygame.KMOD_NUM	)):
            autoit.control_send_by_handle(window_id, window_id, "{NUMPADSUB}")
         elif event.key == pygame.K_KP_PLUS and (pygame.key.get_mods()  == 0 or (pygame.key.get_mods() & pygame.KMOD_NUM	)):
            autoit.control_send_by_handle(window_id, window_id, "{NUMPADADD}")
         elif event.key == pygame.K_SPACE and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{SPACE}")
         elif event.key == pygame.K_F11 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F11}")
         elif event.key == pygame.K_F11 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
            autoit.control_send_by_handle(window_id, window_id, "{SHIFTDOWN}{F11}{SHIFTUP}")
         elif event.key == pygame.K_F12 and pygame.key.get_mods() == 0 :
            autoit.control_send_by_handle(window_id, window_id, "{F12}")

      elif event.type == pygame.MOUSEBUTTONDOWN :
         if event.button == 1:
            autoit.control_click_by_handle(window_id, window_id, button = 'left')
         elif event.button == 3:
            autoit.control_click_by_handle(window_id, window_id, button = 'right')
            
      elif event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
         
