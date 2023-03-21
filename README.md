# Protecnus-Automatic-Flyer-Corrector

1. Do note that this build uses Python 3.8. This works for Protecnus 5.9.5.

2. Make sure to install cmake and add it to the PATH on your computer. Do the same for Pytesseract and OpenCV. Make sure to uncomment the Pytesseract path inside "recognise_name.p". 

3. Furthermore, make sure to add the proper path (root) to both images inside "flyer_checker.py".

4. Make sure to run the following commands on the terminal inside the root:

pip install opencv-python
pip install numpy
pip install Pillow
pip install pyautogui
pip install openai
pip install pytesseract
pip install pyperclip
pip install keyboard

5. If needed, install the appropriate language package from https://tesseract-ocr.github.io/tessdoc/Data-Files.html and place it inside "C:\Program Files (x86)\Tesseract-OCR\tessdata.exe".

6. Sometimes, the keyboard.write() method causes the app to be unable to catch up. For that reason, it might be preferable to replace it with:

for char in correct:
  keyboard.write(char)
  time.sleep(0.02)
  
7. Enter you openai API key in "text_corrector_turbo.py".

8. To use DaVinci 3.0 to correct the flyers, in "main.py" replace "turbo" in "from text_corrector_turbo import correct_text" with "davinci".

9. Ensure that the application Protecnus is in fullscreen mode, and make sure to filter out all flyers except the "pre-cerradas". 

10. Make sure to have the IDE open as you try running the program (you will have to type in the console), but make sure the window does not cover the flyer icons (and make sure that the box outline is not dotted out).

11. If it does not properly recognise the flyers, replace "fullbox.png" with a newly taken screenshot of the icons.
