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

from text_corrector import correct_text
from GUI_navigator_cmds import *
from recognise_name import get_technician_name
from flyer_checker import check_new_flyer
from get_IDE_coordinates import get_coordinates

def slow_type(text):
    for char in text:
        keyboard.write(char)
        time.sleep(0.01)


x, y = get_coordinates() #Click L-CTRL when the mouse is hovering over the IDE in order to start the programme!
                         #Make sure IDE is minimised and not covering the icons

#x = 1257
#y= 1053

while True:

    flyer_is_here = 0
    flyer_is_here = check_new_flyer()
    #print("Flyer:", flyer_is_here)

    if flyer_is_here == 1:

        #Clicking on the entry
        pyautogui.doubleClick()

        time.sleep(3)


        #Getting the date of the flyer
        go_to_date_start()
        time.sleep((0.5))
        pyautogui.doubleClick()
        pyperclip.copy("")
        time.sleep(2)
        pyautogui.hotkey("ctrl", "c")
        pyautogui.hotkey("ctrl", "c")
        print(pyperclip.paste())
        date = pyperclip.paste()
        #print(date)

        #Getting the technician's name from the certificate using OpenCV
        time.sleep((0.5))
        go_to_ver_pre_cierre()
        technician = get_technician_name()
        go_to_cerrar_detalle_de_cierre()

        go_to_editar()


        go_to_materiales()

        #Specifying the technician who performed work on the flyer's mission
        go_to_tipo_de_trabajo()
        go_to_nombre_apellido_tecnico()
        keyboard.write(technician) #Add technician to tipo de trabajos
        pyautogui.press("enter")
        time.sleep(1)

        #Specifying the type of service on the materials list
        go_to_first_entry_tecnico()
        go_to_agregar()
        time.sleep(3)
        go_to_ampliar_busqueda()
        go_to_atencion_de_averias()
        pyautogui.doubleClick()
        time.sleep(1)
        #Adding the technician to the materials list
        go_to_ampliar_busqueda_tecnico()
        pyautogui.moveTo(925, 407) #Technician search bar
        pyautogui.click()
        time.sleep(2)
        keyboard.write(technician)
        pyautogui.press("enter")
        pyautogui.moveTo(925, 429)
        pyautogui.doubleClick()
        time.sleep(2)
        #Adding the number of operations performed for this particular ticket
        go_to_cantidad()
        pyautogui.typewrite("1")
        go_to_aceptar_agregar()

        #Closing the flyer
        go_to_general()
        go_to_facturable()
        go_to_cerrar()
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
        go_to_editar()
        aceptar()
        go_to_certificar()
        fecha_certificado()
        keyboard.write(date)
        time.sleep(3)
        aceptar_certificar_fecha()
        time.sleep(3)
        no()
        time.sleep(1)
        si()
        go_to_salir()

        #Sets up the refresh
        time.sleep(11)
        aceptar_enviado()
        time.sleep(9)
        go_to_first_flyer()
        pyautogui.moveTo(x, y)
        pyautogui.click()


    #If there is no comment for this flyer:
    elif flyer_is_here == 2:
        pyautogui.doubleClick()

        time.sleep(3)

        previous_saved_clipboard = pyperclip.paste()
        #print(previous_saved_clipboard)
        pyperclip.copy("")

        go_to_editar()

        go_to_observaciones_general_start()
        drag_to_observaciones_general_end()
        go_to_observaciones_general_start()

        pyautogui.rightClick()
        time.sleep(0.5)
        go_to_copiar_observaciones_general()
        time.sleep(2)
        currently_saved = pyperclip.paste()
        pyperclip.copy("")
        print("Currently saved:", currently_saved)
        print("Previously saved:", previous_saved_clipboard)

        #If the box isn't empty
        if currently_saved != "":
            pyautogui.click(pyautogui.press('backspace'))
            aceptar()
            go_to_editar()
            go_to_cerrar()
            go_to_observaciones_start()
            pyautogui.click()
            slow_type(currently_saved)
            go_to_aceptar_cierre_de_accion()
            confirma_cierre_de_la_accion()
            aceptar_que_se_ha_cerrado()
            aceptar()
            go_to_salir()
            time.sleep(12)
            pyautogui.moveTo(x, y)
            pyautogui.click()

        #In the case that there is no text at all.
        else:
            print("No text")

            # Getting the date of the flyer
            go_to_date_start()
            pyautogui.click()
            time.sleep((0.5))
            pyautogui.doubleClick()
            pyperclip.copy("")
            time.sleep(2)
            pyautogui.hotkey("ctrl", "c")
            pyautogui.hotkey("ctrl", "c")
            print(pyperclip.paste())
            date = pyperclip.paste()
            # print(date)

            # Getting the technician's name from the certificate using OpenCV
            time.sleep((0.5))
            go_to_ver_pre_cierre()
            technician = get_technician_name()
            go_to_cerrar_detalle_de_cierre()

            go_to_editar()

            go_to_materiales()

            # Specifying the technician who performed work on the flyer's mission
            go_to_tipo_de_trabajo()
            go_to_nombre_apellido_tecnico()
            keyboard.write(technician)  # Add technician to tipo de trabajos
            pyautogui.press("enter")
            time.sleep(1)

            # Specifying the type of service on the materials list
            go_to_first_entry_tecnico()
            go_to_agregar()
            time.sleep(3)
            go_to_ampliar_busqueda()
            go_to_atencion_de_averias()
            pyautogui.doubleClick()
            time.sleep(1)
            # Adding the technician to the materials list
            go_to_ampliar_busqueda_tecnico()
            pyautogui.moveTo(925, 407)  # Technician search bar
            pyautogui.click()
            time.sleep(2)
            keyboard.write(technician)
            pyautogui.press("enter")
            pyautogui.moveTo(925, 429)
            pyautogui.doubleClick()
            time.sleep(2)
            # Adding the number of operations performed for this particular ticket
            go_to_cantidad()
            pyautogui.typewrite("1")
            go_to_aceptar_agregar()

            # Closing the flyer
            go_to_general()
            go_to_facturable()
            go_to_cerrar()
            pyperclip.copy("")
            go_to_observaciones_start()
            slow_type("Elevador/ascensor queda operativo.")
            go_to_cerrado()
            confirma_cierre()
            go_to_aceptar_cierre_de_accion()
            confirma_cierre_de_la_accion()
            aceptar_que_se_ha_cerrado()

            time.sleep(3)

            # Get certification
            go_to_editar()
            aceptar()
            go_to_certificar()
            fecha_certificado()
            keyboard.write(date)
            time.sleep(3)
            aceptar_certificar_fecha()
            time.sleep(3)
            no()
            time.sleep(1)
            si()
            go_to_salir()

            # Sets up the refresh
            time.sleep(11)
            aceptar_enviado()
            time.sleep(9)
            go_to_first_flyer()
            pyautogui.moveTo(x, y)
            pyautogui.click()

    else:
        #Wait and refresh after 5 minutes
        time.sleep(300)
        go_to_previsualizar()



