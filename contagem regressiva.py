from time import sleep

def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        numero -= 1
        sleep(0.3)
contagem_regressiva(12) 
