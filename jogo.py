from pynput import keyboard
import os
import styles
from time import sleep

class Item:
    def __init__(self, img, nome):
        self.img = img
        self.nome = nome

COR = styles.Styles(0)
BG = styles.Styles(1)
FX = styles.Styles(2)
CLEAR = styles.Styles.clear

USERNAME = ''
ESPADA = Item(COR.cyan + FX.bold + '+---\n' + CLEAR, 'Espadão')
ESCUDO = Item(COR.bgreen + FX.bold + 'D\n' + CLEAR, 'Escudo')

EQUIPADO = ESCUDO

HELPER_INVENTARIO = 1

TAMANHO_DA_LINHA = os.get_terminal_size()[0]
LEFT_SPACE = 0
PASSOS = 0

BAG = [ESPADA, ESCUDO]


def linha(qtd):
    for i in range(qtd):
        print()

def wipe():
    os.system('cls')

def chao(char, qtd, color):
    for z in range(qtd):
        for i in range(TAMANHO_DA_LINHA):
            print(color,char, end='', sep='')
        if z != 2:
            print()
    print(CLEAR, end='')

def passos():
    print(f'Você deu {PASSOS} passos.', end='')

def stats():
    global USERNAME
    print('NOME:', COR.bblue, USERNAME, CLEAR, end='\t')

def ajuda():
    global BAG
    qtd_itens = len(BAG)
    print(COR.bblue, 'ITENS NA MOCHILA:', qtd_itens, CLEAR, COR.bred, 'I - Inventário || H - Hit', CLEAR)

def interface():
    stats()
    passos()
    linha(1)
    ajuda()
    linha(1)

def printar_jogo():
    global USERNAME
    wipe()
    linha(20)
    print(' '*LEFT_SPACE + USERNAME)
    personagem = ' '*LEFT_SPACE + ' O \n' + ' '*LEFT_SPACE + '/|\\\n' + ' '*LEFT_SPACE + '/|\\'
    print(COR.red,personagem,CLEAR, sep='')
    chao('◻', 1, COR.green)
    linha(1)
    interface()
    linha(1)


def hit():
    global USERNAME
    wipe()
    linha(20)
    print(' ' * LEFT_SPACE + USERNAME)
    personagem = ' ' * LEFT_SPACE + ' O \n' + ' ' * LEFT_SPACE + '/|\\' + EQUIPADO.img + COR.red + ' ' * LEFT_SPACE + '/|\\'
    print(COR.red, personagem, CLEAR, sep='')
    chao('◻', 1, COR.green)
    linha(1)
    interface()
    linha(1)

def inventario():
    global USERNAME, HELPER_INVENTARIO
    HELPER_INVENTARIO += 1
    if HELPER_INVENTARIO % 2 == 1:
        wipe()
        linha(20)
        print(COR.blue + FX.bold + FX.under + 'NOME: ' + USERNAME + CLEAR)
        linha(2)
        print(COR.red + FX.bold + 'ITENS: ' + CLEAR)
        linha(1)
        for item in BAG:
            print(item.nome, item.img, sep='\n')
        linha(1)
    else:
        printar_jogo()

def on_press(key):
    global LEFT_SPACE, PASSOS
    if key == keyboard.Key.esc:
        print(COR.red, FX.bold, 'JOGO ENCERRADO')
        return False
    try:
        k = key.char
    except:
        k = key.name
    if k in ['left', 'right']:
        PASSOS += 1
        if k=='right':
            LEFT_SPACE += 1
        else:
            LEFT_SPACE -= 1
        printar_jogo()
    if k == 'h':
        hit()
        sleep(0.35)
        printar_jogo()
    if k == 'i':
        inventario()


def game_loop():
    global USERNAME
    USERNAME = input(f"Digite seu nickname: ")
    listener = keyboard.Listener(on_press=on_press)
    printar_jogo()
    listener.start()
    listener.join()

if __name__ == '__main__':
    game_loop()
