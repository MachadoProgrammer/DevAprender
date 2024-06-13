# Quebrar captcha com reconhecimento de imagem simples

import pyautogui

# # encontrar as coordenadas proximo a imagem
# print(pyautogui.locateOnScreen('numero_4.png'))
#
# # encontrar as coordenadas do centro da imagem
# print(pyautogui.locateCenterOnScreen('numero_4.png'))
#
# # usar na pretica
# pyautogui.click(x=1300, y=657, duration=2)

# Imagem 1 vez na tela e bem recortada

captcha = pyautogui.locateCenterOnScreen('google.png')
pyautogui.click(captcha[0], captcha[1], duration=2)
