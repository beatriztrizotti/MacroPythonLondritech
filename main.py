import pyautogui #biblioteca para identificar acoes na tela
import keyboard #biblioteca para identificar eventos no teclado com pip install keyboard
altura = 600 #altura da captura da tela
largura = 500 #largura da captura da tela
captura =(360, 320, altura, largura) #regiao da captura da tela
ecra = pyautogui.screenshot(region=captura) #tirar captura da tela

def identifica_vermelho(imagem):
    altura_imagem , largura_imagem = imagem.size
    for x in range(0, altura_imagem): #identificar primeira coordenada do pixel
        for y in range(0, largura_imagem): #identificar segunda coordenada do pixel
            if imagem.getpixel((x, y)) == (255, 0, 0): #se o pixel tiver coordenada (x,y), entao ele vai ser vermelho
                return x, y #devolve coordenada (x,y)
    
while not keyboard.is_pressed('m'): #enquanto o m for pressionado, o programa vai ser executado
    pixel_vermelho = identifica_vermelho(ecra) #identificar pixel vermelho
    if pixel_vermelho: #se existir pixel vermelho
        pyautogui.moveTo(pixel_vermelho[0]+captura[0], pixel_vermelho[1]+captura[1]) #mover para essa localidade
        pyautogui.mouseDown() #segurar o mouse
    pyautogui.sleep(0.016)
    ecra = pyautogui.screenshot(region=captura) #tirar captura da tela
#pyautogui.moveTo(largura,altura, duration=0.1)