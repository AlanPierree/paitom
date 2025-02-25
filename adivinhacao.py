# https://docs.python.org/3/library/string.html#formatexamples

import random

def jogar():

    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

    username = str(input("Digite seu nome: "))

    numero_secreto = round(random.randrange(1,101))
    # random.seed(100) - seed define um número aleatório, usando a mesma seed pode-se gerar o mesmo número
    total_de_tentativas = 0
    pontos = 1000

    print("\nNíveis de dificuldade:")
    print("\n(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("\nDefina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}\n".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("\nVocê deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\nParabéns, {}, você acertou e fez {} pontos".format(username, pontos))
            break
        else:
            if (maior):
                print("\nVocê errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("\nVocê errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        


    print("\nFim do jogo,", username + "!\n")

if (__name__ == "__main__"):
    jogar()
