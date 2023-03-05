import pyautogui
from PIL import Image
import time

def check_new_flyer():

    time.sleep(2)

    path = r"path"
    imageEmpty = Image.open(path + r"\emptybox.png")
    imageCPC = Image.open(path + r"\currentprecerrada3.png")



    # Try to find the second image on the screen and move the mouse to its location
    location1 = pyautogui.locateOnScreen(imageCPC, confidence=0.9)
    location2 = pyautogui.locateOnScreen(imageEmpty, confidence=0.9)

    if location1 is not None and location2 is not None:
        x, y = pyautogui.center(location1)
        pyautogui.moveTo(x, y)

        print("1")
        return 1


    if location1 is not None:
        x, y = pyautogui.center(location1)
        pyautogui.moveTo(x, y)
        print("2")
        return 2
    print("3")
    return 3

'''
if location 2

if location1 is not None:
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x, y)
else:
    print("Could not find imageCPC on screen")

# Try to find the first image on the screen and move the mouse to its location
location2 = pyautogui.locateOnScreen(imageEmpty, confidence=0.9)
if location2 is not None:
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x, y)
else:
    print("Could not find imageEmpty on screen")

# Wait for 1 second
time.sleep(1)


'''
