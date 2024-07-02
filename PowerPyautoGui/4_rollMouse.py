import pyautogui
from time import sleep

pyautogui.moveTo(1294, 273, duration=1.5)
for i in range(2):
    sleep(0.5)
    pyautogui.scroll(-2400)
