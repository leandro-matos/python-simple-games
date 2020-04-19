import random

def jogar():
    print("##################################")
    print("Bem vindo ao jogo de adivinhação!!")
    print("##################################")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print(" Qual o nível de dificuldade ? ")
    print("(1)Fácil, (2)Médio, (3)Díficil")

    nivel = int(input("Define o nível:"))

    if (nivel ==1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    elif (nivel == 3):
        total_tentativas = 5
    else:
        print("Informe apenas um dos valores citados")

    for rodada in range(1, total_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100:")
        print("Você digitou o número:", chute_str)
        chute_int = int(chute_str)

        if(chute_int <1 or chute_int > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = numero_secreto == chute_int
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if (acertou):
            print("Você Acertou e fez {} pontos!!!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O chute foi maior que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif(menor):
                print("Você errou! O chute foi menor que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

    print("################")
    print("FIM DO JOGO !!!")

if(__name__ == "__main__"):
    jogar()