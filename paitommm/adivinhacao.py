print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************\n")

pais = "Brasil"
nome = "Alan"
type(pais)
type(nome)
print("Seu nome é", nome, "e você é do", pais, "\n")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou: ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!\n")
else:
    print("Você errou!\n")
