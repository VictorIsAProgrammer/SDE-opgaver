import random
# det er ikke smukt, men det virker
def choose_winner(player_hand):
    pc_hand = random.choice(HAND_SIGNS)
    print("Du valgte: " + player_hand)
    print("Computeren valgte: " + pc_hand)
    # uafgjort:
    if player_hand == pc_hand:
        return "uafgjort"
    # player sten
    if player_hand.lower() == "sten":
        if pc_hand == "saks": # player wins
            return "dig"
        elif pc_hand == "papir": # pc wins
            return "computeren"
    # player saks
    if player_hand.lower() == "saks":
        if pc_hand == "papir": # player wins
            return "dig"
        elif pc_hand == "papir": # pc wins
            return "computeren"
    # player papir
    if player_hand.lower() == "papir":
        if pc_hand == "sten": # player wins
            return "dig"
        elif pc_hand == "saks": # pc wins
            return "computeren"

HAND_SIGNS = ["sten", "saks", "papir"]

game_winner = "uafgjort"

while game_winner.lower() == "uafgjort":
    player_hand = input("Sten, saks eller papir?\n")
    if player_hand.lower() in HAND_SIGNS:
        game_winner = choose_winner(player_hand)
        print("Vinderen er: " + game_winner)
        play_again = input('Hvis du vil spille igen, så skriv "Ja"\n') #
        if play_again.lower() == "ja":
            game_winner = "uafgjort"
        else:
            break
    else:
        print("Forstod ikke input. Indtast: Sten, saks eller papir")