# Como Movimentar, clicar e zerar um jogo Pyautogui
import pyautogui
from time import sleep

pyautogui.moveTo(1349, 452, duration=2)
# pyautogui.move(0, -20, duration=2)
for i in range(1000):
    # sleep(0.3)
    pyautogui.click()
