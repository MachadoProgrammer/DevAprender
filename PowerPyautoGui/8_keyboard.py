# Como usar botoes e atalhos do teclado

import pyautogui

# Navegar e clicar no campo email
pyautogui.click(1411, 265, duration=1)
pyautogui.typewrite('admin@gmail.com')
# apertar tab
pyautogui.press('tab')
# digitar senha
pyautogui.typewrite('123456')
# apertar tab
pyautogui.press('tab')
# apertar space
pyautogui.press('space')

# PARA VER TODAS AS POSSIVEIS TECLAS, RODE:
# print(pyautogui.KEYBOARD_KEYS)

# COMBINACAO DE TECLAS Keydown e Keyup
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
