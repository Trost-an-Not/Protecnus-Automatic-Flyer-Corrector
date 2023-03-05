import pyautogui
from pynput import keyboard


def get_coordinates():

    x = y = None

    def on_press(key):
        nonlocal x, y
        if key == keyboard.Key.ctrl_l:
            x, y = pyautogui.position()
            print(x, y)
            listener.stop()



    def on_release(key):
        pass


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    return x, y
