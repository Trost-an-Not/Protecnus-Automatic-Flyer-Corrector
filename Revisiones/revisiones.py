import cv2
import numpy as np
import os
import PIL
import pyautogui
import openai
import time
import pytesseract
import pyperclip
import keyboard

from text_corrector_turbo import correct_text
from Revisiones.GUI_navigator_cmds import *
from Revisiones.recognise_date import get_date_by_screenshot
from flyer_checker import check_new_flyer
from get_IDE_coordinates import get_coordinates

def slow_type(text):
    for char in text:
        keyboard.write(char)
        time.sleep(0.01)


def correct_revisiones_main():


    x, y = get_coordinates() #Click L-CTRL when the mouse is hovering over the IDE in order to start the programme!
                            #Make sure IDE is minimised and not covering the icons

    #x = 1257
    #y= 1053

    while True:

        flyer_is_here = 0
        flyer_is_here = check_new_flyer()
        #print("Flyer:", flyer_is_here)

        if flyer_is_here != 3:

            #Clicking on the entry
            pyautogui.doubleClick()

            time.sleep(3)


            #Getting the date of the flyer
            time.sleep(4)
            date = get_date_by_screenshot()
            time.sleep(1)
            #print(date)


            #Closing the flyer
            go_to_cerrar()

            if flyer_is_here == 1:
                pyperclip.copy("")
                print(pyperclip.paste())
                go_to_observaciones_start()
                drag_to_observaciones_end()
                go_to_observaciones_start()
                pyautogui.rightClick()
                go_to_copiar() #Copying the technician's comment, and from the clipboard saving it onto a variable
                #print(pyperclip.paste())
                observation = pyperclip.paste()
                #print(observation)
                corrected = correct_text(observation)
                #print(corrected)
                time.sleep(0.5)
                slow_type(corrected) #Types the corrected version of the observation.
                time.sleep(0.3)

            go_to_cerrado()
            confirma_cierre()
            go_to_aceptar_cierre_de_accion()
            confirma_cierre_de_la_accion()
            aceptar_que_se_ha_cerrado()

            time.sleep(3)

            #Get certification
            go_to_certificar()
            fecha_certificado()
            keyboard.write(date)
            time.sleep(3)
            go_to_elegir_colegido()
            go_to_colegiado_elegido()


            aceptar_certificar_fecha()
            time.sleep(3)
            no()
            time.sleep(1)
            go_to_salir()

            #Sets up the refresh
            time.sleep(4)
            aceptar_enviado()
            time.sleep(4)
            go_to_first_flyer()
            pyautogui.moveTo(x, y)
            pyautogui.click()


        else:
            #Wait and refresh after 5 minutes
            time.sleep(300)
            go_to_previsualizar()



