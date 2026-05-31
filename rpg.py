# função para ler o arquivo e retornar uma lista de dicionarios
def ler_arquivo(nome_arquivo):
    jogadores = []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            jogador = {
                "nome": dados[0],
                "classe": dados[1],
                "kills": int(dados[2]),
                "deaths": int(dados[3]),
                "dano": int(dados[4])
            }

            jogadores.append(jogador)

    return jogadores


# função para calcular o KDA
def calcular_kda(kills, deaths):
    if deaths == 0:
        return kills  
    return kills / deaths


#funçao para filtrar jogadores por classe
def filtrar_por_classe(jogadores, classe):
    filtrados = []

    for jogador in jogadores:
        if jogador["classe"].lower() == classe.lower():
            filtrados.append(jogador)

    return filtrados

#le os dados do arquivo
jogadores = ler_arquivo("partida.txt")

# jogador com maior dano
maior_dano = max(jogadores, key=lambda j: j["dano"])

# média de kills
total_kills = 0

for jogador in jogadores:
    total_kills += jogador["kills"]

media_kills = total_kills / len(jogadores)

# jogadores com KDA superior a 2.0
jogadores_kda_alto = []

for jogador in jogadores:
    kda = calcular_kda(jogador["kills"], jogador["deaths"])

    if kda > 2.0:
        jogadores_kda_alto.append(jogador["nome"].upper())


# relatório
print("===== RELATÓRIO DA PARTIDA =====")

print(f"\nJogador com maior dano: {maior_dano['nome']}")
print(f"Dano causado: {maior_dano['dano']}")

print(f"\nMédia de kills da partida: {media_kills:.2f}")

print("\nJogadores com KDA superior a 2.0:")
for nome in jogadores_kda_alto:
    print(nome)

#exemplo de filtragem por classe
print("\n===== MAGOS DA PARTIDA =====")

magos = filtrar_por_classe(jogadores, "Mago")

for mago in magos:
    print(mago["nome"])