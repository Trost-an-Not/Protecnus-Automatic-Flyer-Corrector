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


#x, y = get_coordinates()

#x = 1257
#y= 1053

while True:
    flyer_is_here = 0
    flyer_is_here = check_new_flyer()

    print("Flyer:", flyer_is_here)

    if flyer_is_here == 2:

        pyautogui.doubleClick()

        time.sleep(3)

        go_to_date_start()
        time.sleep((0.25))
        pyautogui.doubleClick()

        pyautogui.hotkey('ctrl', 'c')

        date = pyperclip.paste()
        print(date)

        time.sleep((0.5))

        go_to_ver_pre_cierre()

        #pyautogui.moveTo(x, y)
        #pyautogui.click()

        technician = get_technician_name()

        go_to_cerrar_detalle_de_cierre()

        go_to_editar()

        go_to_materiales()

        go_to_tipo_de_trabajo()

        go_to_nombre_apellido_tecnico()

        pyperclip.copy(technician)

        #technician_modified = technician.replace("é", "\\xe9").replace("í", "\\xed").replace("ó", "\\xf3").replace("á", "\\xe1").replace("ñ", "\\xf1").replace("ú", "\\xfa")

        keyboard.write(technician)

        pyautogui.press("enter")

        time.sleep(1)

        go_to_first_entry_tecnico()

        go_to_agregar()

        time.sleep(3)

        go_to_ampliar_busqueda()

        go_to_atencion_de_averias()

        pyautogui.doubleClick()

        time.sleep(1)

        go_to_ampliar_busqueda_tecnico()

        pyautogui.moveTo(925, 407)
        pyautogui.click()
        time.sleep(2)

        keyboard.write(technician)

        pyautogui.press("enter")

        pyautogui.moveTo(925, 429)
        pyautogui.doubleClick()
        time.sleep(2)

        go_to_cantidad()

        pyautogui.typewrite("1")

        go_to_aceptar_agregar()

        go_to_general()

        go_to_facturable()

        go_to_cerrar()

        pyperclip.copy("")
        print(pyperclip.paste())

        go_to_observaciones_start()

        drag_to_observaciones_end()

        go_to_observaciones_start()

        pyautogui.rightClick()

        go_to_copiar()

        print(pyperclip.paste())

        observation = pyperclip.paste()

        print(observation)

        corrected = correct_text(observation)

        print(corrected)

        #go_to_observaciones_start()

        #pyautogui.doubleClick()

        pyperclip.copy(corrected)

        print("Clipboard:", pyperclip.paste())

        keyboard.write(corrected)

        #pyautogui.hotkey('ctrl', 'v')

        go_to_cerrado()

        confirma_cierre()

        go_to_aceptar_cierre_de_accion()

        confirma_cierre_de_la_accion()

        aceptar_que_se_ha_cerrado()

        time.sleep(3)

        go_to_editar()

        aceptar()

        go_to_certificar()

        fecha_certificado()

        pyperclip.copy(date)

        pyautogui.hotkey('ctrl', 'v')

        aceptar_certificar_fecha()

        time.sleep(12)

        no()

        time.sleep(1)

        si()

        time.sleep(12)

        aceptar_enviado()

        go_to_salir()

        time.sleep(2)

        go_to_first_flyer()

        #pyautogui.moveTo(x, y)
        #pyautogui.click()













    elif flyer_is_here == 1:
        pyautogui.doubleClick()

        time.sleep(3)

        go_to_date_start()
        time.sleep((0.25))
        pyautogui.doubleClick()

        pyautogui.hotkey('ctrl', 'c')

        date = pyperclip.paste()
        print(date)

        time.sleep((0.5))

        go_to_ver_pre_cierre()

       # pyautogui.moveTo(x, y)
        #pyautogui.click()

        technician = get_technician_name()

        go_to_cerrar_detalle_de_cierre()

        go_to_editar()

        go_to_materiales()

        go_to_tipo_de_trabajo()

        go_to_nombre_apellido_tecnico()

        pyperclip.copy(technician)

        # technician_modified = technician.replace("é", "\\xe9").replace("í", "\\xed").replace("ó", "\\xf3").replace("á", "\\xe1").replace("ñ", "\\xf1").replace("ú", "\\xfa")

        keyboard.write(technician)

        pyautogui.press("enter")

        time.sleep(1)

        go_to_first_entry_tecnico()

        go_to_agregar()

        time.sleep(3)

        go_to_ampliar_busqueda()

        go_to_atencion_de_averias()

        pyautogui.doubleClick()

        time.sleep(1)

        go_to_ampliar_busqueda_tecnico()

        pyautogui.moveTo(925, 407)
        pyautogui.click()
        time.sleep(2)

        keyboard.write(technician)

        pyautogui.press("enter")

        pyautogui.moveTo(925, 429)
        pyautogui.doubleClick()
        time.sleep(2)

        go_to_cantidad()

        pyautogui.typewrite("1")

        go_to_aceptar_agregar()

        go_to_general()

        go_to_facturable()

        go_to_cerrar()

        pyperclip.copy("")
        print(pyperclip.paste())

        # pyautogui.hotkey('ctrl', 'v')

        go_to_cerrado()

        confirma_cierre()

        go_to_aceptar_cierre_de_accion()

        confirma_cierre_de_la_accion()

        aceptar_que_se_ha_cerrado()

        time.sleep(3)

        go_to_editar()

        aceptar()

        go_to_certificar()

        fecha_certificado()

        pyperclip.copy(date)

        pyautogui.hotkey('ctrl', 'v')

        aceptar_certificar_fecha()

        time.sleep(12)

        no()

        time.sleep(1)

        si()

        time.sleep(12)

        aceptar_enviado()

        go_to_salir()

        time.sleep(2)

        go_to_first_flyer()

        #pyautogui.moveTo(x, y)
        #pyautogui.click()

    else:
        time.sleep(300)



