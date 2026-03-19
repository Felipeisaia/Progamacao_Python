hp_heroi = 100
hp_monstro = 100

dano_heroi = int(input("Digite o dano do herói por rodada: "))
dano_monstro = int(input("Digite o dano do monstro por rodada: "))

rodada = 1

while hp_heroi > 0 and hp_monstro > 0:
    print(f"\n--- Rodada {rodada} ---")

    hp_monstro -= dano_heroi
    if hp_monstro < 0:
        hp_monstro = 0

    hp_heroi -= dano_monstro
    if hp_heroi < 0:
        hp_heroi = 0

    print(f"HP do Herói: {hp_heroi}")
    print(f"HP do Monstro: {hp_monstro}")

    rodada += 1

if hp_heroi > 0 and hp_monstro == 0:
    print("\nO herói venceu!")
elif hp_monstro > 0 and hp_heroi == 0:
    print("\nO monstro venceu!")
else:
    print("\nEmpate! Ambos foram derrotados.")