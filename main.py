from historyGenerator import generateHistory
from playerGenerator import generatePlayer

def main():
    playerCount = int(input("Введите количество игроков: "))
    players = []

    for _ in range(playerCount):
        players.append(generatePlayer())

    history = generateHistory()

    return players, history

if __name__ == "__main__":
    players, history = main()

    print(f"----------------------------\nИстория:\n\n{history}")


    print(f"----------------------------\nИгроки:")
    for playerNumber, player in enumerate(players):
        print(f"\nИгрок: {playerNumber + 1}")
        for key, value in player.items():
            print(f"{key}: {value}")