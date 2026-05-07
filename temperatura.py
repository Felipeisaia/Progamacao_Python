quantidade_dias = int(input("Quantos dias deseja analisar? "))

contador = 0
soma_temperaturas = 0

while contador < quantidade_dias:
    temperatura = float(input(f"Digite a temperatura do dia {contador + 1}: "))
    soma_temperaturas += temperatura
    contador += 1

media = soma_temperaturas / quantidade_dias

print(f"Média das temperaturas: {media:.2f} °C")

if media > 25:
    print("Acima do esperado")
else:
    print("Dentro da normalidade")