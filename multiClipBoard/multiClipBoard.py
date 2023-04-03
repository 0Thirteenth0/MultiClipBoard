import json
import clipboard
from pynput import keyboard
import os

def __main__():
    global currClip
    currClip = int(0)

def save_items(fp, data):
    with open(fp, "w") as f:
        json.dump(data, f)


def load_json(fn):
    with open(fn, "r") as f:
        data = json.load(f)
        return data


def on_press(key):
    pass
    # try:
    #     print('Key {0} pressed'.format(key.char))
    #     #Add your code to drive motor
    # except AttributeError:
    #     print('Key {0} pressed'.format(key))
        #Add Code

def on_release(key):
    print("\u001b[2J")
    os.system('cls' if os.name == 'nt' else 'clear')
    global currClip
    #Add your code to stop motor
    if key == keyboard.Key.esc:
        # Stop listener
        # Stop the Robot Code
        return False
    
    if not os.path.exists(fname):
        open(fname, "x")
        save_items(fname, {"key": "Value"})

    data = load_json(fname)
    
    if key == keyboard.Key.down:
        if len(data) > 1:
            if currClip <= 1:
                currClip = len(data)
            currClip -= 1
            print("\u001b[32m["+ str(currClip) + "] \u001b[34m- " + data[str(currClip)] + "\u001b[0m")
        else:
            print("\u001b[31mError: List is Currently Empty!\u001b[0m")

    if key == keyboard.Key.up:
        if len(data) > 1:
            if currClip >= len(data) - 1:
                currClip = 0
            currClip += 1
            print("\u001b[32m["+ str(currClip) + "] \u001b[34m- " + data[str(currClip)] + "\u001b[0m")
        else:
            print("\u001b[31mError: List is Currently Empty!\u001b[0m")
    
    if 'char' in dir(key) and key.char == '`':
        data = dict()
        data["Key"] = "Value"
        save_items(fname, data)
    
    if 'char' in dir(key) and key.char == 'c':
        key = str(len(data))
        data[key] = clipboard.paste()
        save_items(fname, data)
    
    if 'char' in dir(key) and key.char == 'v':
        if currClip > 0:
            clipboard.copy(data[str(currClip)])
        else:
            print("\u001b[31mError: Nothing Was Selected to be Saved into Clipboard\u001b[0m")
    if 'char' in dir(key) and key.char == 'l':
        if len(data) > 1:
            for i in data.keys():
                print("\u001b[32m" + i + "\t", "\u001b[34m" + data[i] + "\u001b[0m")  
        else:
            print("\u001b[31mError: Please add something into list\u001b[0m")

    if 'char' in dir(key) and key.char == 'h':
        print(functionality)
        
    if 'char' in dir(key) and key.char == 'q':
        print("Program Exiting...")
        exit(0)

fname = "clipBoard.json"
functionality = "\u001b[32m[c] \t\u001b[34m- save clipboard into list\n\u001b[32m[v] \t\u001b[34m- load an item from list into clipboard\n\u001b[32m[l] \t\u001b[34m- prints everything in the clipboard\n\u001b[32m[`] \t\u001b[34m- delete everything from list\n\u001b[32m[delete]\u001b[34m- remove last item from list\n\u001b[32m[h] \t\u001b[34m- print help information\n\u001b[32m[q] \t\u001b[34m- Exit Program\u001b[0m"
prevcmd = str()



print(functionality)
# Collect events until released
__main__()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


