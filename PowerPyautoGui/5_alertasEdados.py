# ALERTAR E PEDIR INFFORMAÇÃO
import pyautogui

# ALERT
pyautogui.alert(text="Um alerta", title="Alerta", button="ok")

# PEDIR INFO
email = pyautogui.prompt(text='Digite seu email', title='Info')
print(f'voce digite seu {email}')

# Confirmar
resposta = pyautogui.confirm(text='continuar a automacao', title='Confirmar', buttons=['sim', 'nao', 'cancelar'])
if resposta == 'sim':
    print('Sim')
elif resposta == 'não':
    print('Não')
else:
    print('Cancelando')

# Para pedir e mascarar a senha
pyautogui.password(text='password', title='password', mask='*')