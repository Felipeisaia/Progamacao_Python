nivel = 0

while nivel >= 0:
    nivel = float(input("Digite o nível do rio em metros (negativo para encerrar): "))

    if nivel < 0:
        print("Leitura encerrada.")
    elif nivel < 3:
        print("Estado Normal")
    elif nivel <= 5:
        print("Estado de Alerta")
    else:
        print("Evacuação Imediata")