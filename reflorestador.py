meta = float(input("Digite a meta de biomassa: "))

biomassa_total = 0
quantidade_arvores = 0

while biomassa_total < meta:
    biomassa_arvore = float(input("Digite a biomassa da árvore plantada: "))
    biomassa_total += biomassa_arvore
    quantidade_arvores += 1

print(f"Meta atingida!")
print(f"Foram necessárias {quantidade_arvores} árvores.")
print(f"Biomassa total: {biomassa_total}")