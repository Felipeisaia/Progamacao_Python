import random

# Método para popular a lista com n números aleatórios
def popular_lista(n):
    lista = []
    for i in range(n):
        numero = random.randint(100, 400)
        lista.append(numero)
    return lista

# Método para exibir a lista
def exibir_lista(lista):
    print(lista)

# Método para remover números repetidos da própria lista
def remover_repetidos(lista):
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                lista.pop(j)
            else:
                j += 1
        i += 1

# Programa principal
numeros = popular_lista(15)

print("Lista original:")
exibir_lista(numeros)

remover_repetidos(numeros)

print("Lista sem repetidos:")
exibir_lista(numeros)