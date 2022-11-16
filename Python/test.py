import accessible_output2.outputs.auto
ao_output = accessible_output2.outputs.auto.Auto()
import threading
event = threading.Event()
lock = threading.Lock()
from pynput import keyboard
lock.acquire()
modifiers = {}
modifiers["test"] = True
del modifiers['test']
print(len(modifiers))
lock.release()
def on_press(key):
   lock.acquire()
   if type(key) == keyboard.Key:
      if key == keyboard.Key.ctrl_l:
#         print(key)
         modifiers["control"] = True
   elif type(key) == keyboard.KeyCode:
      print(key.canonical)
#      print(modifiers.get("control"))
      if key.char == "b" and modifiers.get('control')  == True:
         ao_output.output("Hello Crusaders!", True)
         event.set()
   lock.release()
def on_release(key):
   lock.acquire()
   if key == keyboard.Key.ctrl_l:
      modifiers.pop("control", None)
   lock.release()
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

event.clear()
listener.start()

while event.is_set() == False:
   pass