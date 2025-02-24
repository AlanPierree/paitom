# https://docs.python.org/3/library/string.html#formatexamples

total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print("\n*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print("\nTentativa {} de {}\n".format(rodada, total_de_tentativas))

    numero_secreto = 42
    username = "Alan"

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
        print("\nParabéns", username + ", você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    


print("\nFim do jogo!\n")
