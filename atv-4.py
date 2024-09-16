print(f"\nLojão do Manoel\n")

total_compra = 0

while True:
    preco = float(input("Digite o preço do produto (ou 0 para finalizar): "))
    
    if preco == 0:
        break
    
    total_compra += preco

print(f"\nTotal: R$ {total_compra:.2f}")

dinheiro = float(input(f"\nDigite o valor em dinheiro: "))

troco = dinheiro - total_compra

print(f"\nDinheiro: R$ {dinheiro:.2f}")
print(f"\nTroco: R$ {troco:.2f}\n")