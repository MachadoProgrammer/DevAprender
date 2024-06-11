# Como usar a função click
import pyautogui

# Click personalisado
# clicks x vezes
pyautogui.click(1349, 452, clicks=2, interval=1, button='left', duration=2)

# click na posição
pyautogui.click(button='left')  # right, middle

# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()
