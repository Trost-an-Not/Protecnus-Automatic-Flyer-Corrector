import pyautogui
from pynput import keyboard


i = 0


x = y = None  # Initialize x to None
x1 = 0
x2 = 0
y1 = 0
y2 = 0


def on_press(key):
    global y, x, x1, x2, y1, y2

    if key == keyboard.Key.ctrl_l:
        x, y = pyautogui.position()
        name = input()
        #print("#" + name)
        print(x,", ", y)
        global i
        i += 1
        #print(i)

    if key == keyboard.Key.shift_l:

        x1, y1 = pyautogui.position()
        print(x1,",",y1)

    if key == keyboard.Key.shift_r:

        x2, y2 = pyautogui.position()
        print(x2,",",y2)

    if key == keyboard.Key.ctrl_r:
        print("Width and height:")
        print(x2 - x1,",",y2 - y1)


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
