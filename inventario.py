peso_total = 0

while peso_total <= 15:
    peso_item = float(input("Digite o peso do item encontrado: "))

    if peso_total + peso_item > 15:
        print("Mochila cheia, item descartado")
        break
    else:
        peso_total += peso_item
        print(f"Peso atual na mochila: {peso_total} kg")

print(f"Peso final total: {peso_total} kg")