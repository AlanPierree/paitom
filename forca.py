def jogar():

    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not acertou and not enforcou):

        chute = input("Digite uma letra: ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrou a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()