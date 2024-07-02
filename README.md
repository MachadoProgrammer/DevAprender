# Pyautogui 

## Automatização com mouse e teclado

-- Problemas para reconhecer certas imagens -> Snippong Tool, usar PrtSc Windows
-- Problemas com resolução
-- Mouse e teclado ficam controlados pelo bot 
````Possiveis Soluções

1. Máquina virtual -> VirtualBox
2. VPS -> AWS, DigitalOcean, Render, Railway, etc...
3. Um PC somente para o bot rodar


````
### Cuidados e Obs

1. Velociadade de automação -> (sleep, duration)
2. Encontrar rápido uma coordenada -> mouseInfo()
3. locateCenterOnScreen() -> captcha[0], captcha[1] -> (x, y) -> coordenadas
4. Pyperclip para se em frase ou texto tiver caracteres especiais(quote?) 
5. Images: Consider saving them in PNG format because of the way it compresses images without losing much information. -> lightshot
    
````Usar mouseInfo
-- No cmd
pip install mouseinfo
write python
from mouseinfo import mouseInfo
mouseInfo()

````



````Projetos

1. Bot de curtidas e comentários instagram
2. Zerar GuitarFlash
3. Zerar Piano Titles
4. Bot de mensagens WhatsApp

````