while True:
    valor = int(input("Digite um valor inteiro (digite um número negativo para sair): "))

    if valor < 0:
        print("Programa encerrado.")
        break

    if valor > 100:
        print("Limite excedido")
    elif valor > 10:
        print(f"O quadrado de {valor} é {valor ** 2}")
    elif valor > 5:
        print(f"O cubo de {valor} é {valor ** 3}")