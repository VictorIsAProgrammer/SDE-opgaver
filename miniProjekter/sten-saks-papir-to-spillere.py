import random

def choose_winner(p1, p2):
    print("Spiller 1 valgte: " + p1)
    print("Spiller 2 valgte: " + p2)
    # uafgjort:
    if p1 == p2:
        return "uafgjort"
    # player sten
    if p1.lower() == "sten":
        if p2 == "saks": # player 1 wins
            return "spiller 1"
        elif p2 == "papir": # player 2 wins
            return "spiller 2"
    # player saks
    if p1 == "saks":
        if p2 == "papir": # player 1 wins
            return "spiller 1"
        elif p2 == "papir": # player 2 wins
            return "spiller 2"
    # player papir
    if p1.lower() == "papir":
        if p2 == "sten": # player 1 wins
            return "spiller 1"
        elif p2 == "saks": # player 2 wins
            return "spiller 2"

HAND_SIGNS = ["sten", "saks", "papir"]

game_winner = "uafgjort"

while game_winner.lower() == "uafgjort":
    player_1_hand = input("Spiller 1: Sten, saks eller papir?\n").lower()
    player_2_hand = input("Spiller 2: Sten, saks eller papir?\n").lower()
    if player_1_hand and player_2_hand in HAND_SIGNS:
        game_winner = choose_winner(player_1_hand, player_2_hand)
        print("Vinderen er: " + game_winner)
        play_again = input('Hvis du vil spille igen, så skriv "Ja"\n').lower()
        if play_again == "ja":
            game_winner = "uafgjort"
        else:
            print("Tak for spillet.")
            break
    else:
        print("En af spillerene skrev forkert. Prøv igen.") #