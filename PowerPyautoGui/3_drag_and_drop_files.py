# Como arrastar algo para outro lugar

import pyautogui
for i in range(10):
    # Mover ate uma coordenada
    pyautogui.moveTo(1385, 257, duration=0.5)
    # drag e soltar
    pyautogui.dragTo(1360, 790, button='left', duration=0.5)
    # repetir 9

