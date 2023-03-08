import cv2
import numpy as np
import re
import os
from PIL import Image, ImageEnhance
import pyautogui
import openai
import time
import pytesseract

#tesseract not working until I use path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_technician_name():
    region = [520, 410, 300, 30]

    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot(region=region)



    # Create a contrast enhancer
    enhancer = ImageEnhance.Contrast(screenshot)

    # Increase the contrast by a factor of 1.5
    screenshot = enhancer.enhance(2)

    # Increase the size of the image for better recognition
    width, height = screenshot.size
    new_width = 2 * width
    new_height = 2 * height
    screenshot = screenshot.resize((new_width, new_height))


    #Place this before and see?



    # Perform text recognition using Tesseract OCR
    custom_config = r'--dpi 600 --oem 3 --psm 12 -c tessedit_char_whitelist= ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzñÑáéíóúÁÉÍÓÚ'
    technician_name = pytesseract.image_to_string(screenshot, lang='spa', config=custom_config)

    technician_name = technician_name.replace("º", "o")

    # Print the recognized text

    print(technician_name)

    return technician_name

