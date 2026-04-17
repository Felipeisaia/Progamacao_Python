lista_numeros = [5, 3, 1, 19, 25, 88, 10, 42]

lista_numeros.sort()
print("Lista ordenada:", lista_numeros)

numero_pesquisa = int(input("Digite um número para pesquisar na lista: "))

if numero_pesquisa in lista_numeros:
    print("O número está na lista")
    lista_numeros.remove(numero_pesquisa)
else:
    print("O número não está na lista")

print("Lista após pesquisa:", lista_numeros)

menor = min(lista_numeros)
maior = max(lista_numeros)
media = sum(lista_numeros) / len(lista_numeros)

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Média:", media)

lista_sem_pares = [num for num in lista_numeros if num % 2 != 0]
print("Lista sem números pares:", lista_sem_pares)

lista_com_repetidos = [1,1,2,3,4,4,5,5,5,6]
lista_sem_repetidos = list(set(lista_com_repetidos))
lista_sem_repetidos.sort()

print("Lista original com repetidos:", lista_com_repetidos)
print("Lista sem repetidos:", lista_sem_repetidos)