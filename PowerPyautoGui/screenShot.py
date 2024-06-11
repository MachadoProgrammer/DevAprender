import pyautogui

# print tela inteira
pyautogui.screenshot('tela.jpg')

# print parte da tela
pyautogui.screenshot('parte.jpg', region=(1621, 163, 100, 50))
