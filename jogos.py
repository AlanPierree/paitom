import forca
import adivinhacao

def escolhe_jogo():

    print("\n*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************\n")

    print("(1) Forca (2) Adivinhação\n")

    jogo = int(input("Escolha seu jogo: "))

    if (jogo == 1):
        print("\nJogando forca!")
        forca.jogar()
    elif (jogo == 2):
        print("\nJogando adivinhação!")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()