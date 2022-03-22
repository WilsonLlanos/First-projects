"""
Abaixo, um minigame utilizando o comando choice e while
"""
from random import choice

while True:
    player = str(input("Escolha pedra, papel ou tesoura\n")).lower()
    maquina = choice("pedra papel tesoura".split()).lower()
    print(f"Maquina: {maquina}")
    if player == maquina:
        print(f"os dois escolheram {player}")
        continue

    elif player == "pedra":
        if maquina == "papel":
            print(f"Você escolheu {player} e a maquina escolheu {maquina}. Portanto, você perdeu")
            print("Fim de jogo")

        else:
            print(f"Você escolheu {player} e a maquina escolheu {maquina}. Portanto, você ganhou")

    elif player == "papel":
        if maquina == "tesoura":
            print(f"Você escolheu {player} e a maquina escolheu {maquina}. Portanto, você perdeu")
            print("Fim de jogo")

        else:
            print(f"Você escolheu {player} e a maquina escolheu {maquina}. Portanto, você ganhou")
            print("Fim de jogo")

    else:
        if maquina == "pedra":
            print(f"Você escolheu {player} e a maquina escolheu {maquina}. Portanto, você perdeu")
            print("Fim de jogo")

        else:
            print(f"Você escolheu {player} e a maquina escolheu {maquina}. Portanto, você ganhou")
            print("Fim de jogo")


    print("1. Jogar novamente")
    print("2. Sair")

    opcao = int(input("Insira a opção\n"))
    if opcao == 1:
        continue

    elif opcao == 2:
        print("Fim de jogo")
        break

    else:
        print("Opção inválida")
        opcao = int(input("Insira a opção\n"))
        if opcao == 1:
            continue
        else:
            print("Opção inválida")
            print("Fim de jogo")
            break
