import random
def get_choices():
    player_choice = input ("Tanlang(tosh, qaychi, qogoz): ")
    options = ["tosh", "qaychi", "qogoz"]
    computer_choice = random.choice(options)
    return player_choice, computer_choice

def check_win(player, computer):
    if player == computer:
        return "Durrang!"
    elif (player == "tosh" and computer == "qaychi") or (player == "qaychi" and computer == "qogoz") or (player == "qogoz" and computer == "tosh"):
        return "Siz yutdingiz!"
    else:
        return"Kompyuter yutdi!"
    
def play():
    player_choice, computer_choice = get_choices()
    print(f"Siz tanladingiz: {player_choice}, Kompyuter tanladi: {computer_choice}")
    result = check_win(player_choice, computer_choice)
    print(result)

play()