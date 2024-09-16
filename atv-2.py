import datetime

ano_atual = datetime.datetime.now().year

while True:
    ano_nascimento = int(input("Digite o ano de nascimento para se inscrever no concurso: "))

    idade = ano_atual - ano_nascimento

    if idade >= 18:
        print(f"Você tem {idade} anos. Inscrição permitida!")
        break
    else:
        print(f"Você tem {idade} anos. Inscrição não permitida. Tente novamente.")