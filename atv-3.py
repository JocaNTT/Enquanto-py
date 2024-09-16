import random

numero_secreto = random.randint(1, 50)

tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 5 tentativas para adivinhar o número secreto entre 1 e 100.")

while tentativas > 0:
    chute = int(input("Digite seu palpite: "))

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
    
    tentativas -= 1
    print(f"Você ainda tem {tentativas} tentativa(s) restante(s).")

if tentativas == 0:
    print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")
