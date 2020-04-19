import forca
import adivinhacao

print("##################################")
print("ESCOLHA O SEU JOGO!!")
print("##################################")

print("(1) Forca, (2) Adivinhação")

jogo = int(input("Qual o jogo você deseja: "))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando Adivinhação")
    adivinhacao.jogar()
else:
    print("Opção Inválida")
