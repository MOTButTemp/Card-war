import random
player_cards = 10
computer_cards = 10
while player_cards > 0 and computer_cards > 0: 
    print("Player has " + str(player_cards) + " cards remaining")
    print("Computer has " + str(computer_cards) + " cards remaining")
    input("Press Enter to flip a card")
    print()
    player = random.randint(1, 10)
    computer = random.randint(1, 10)
    print("Player drew " + str(player))
    print("Computer drew " + str(computer))
    if player > computer:
        print("Player wins the hand")
        player_cards += 1
        computer_cards -= 1
    elif computer > player:
        print("Computer wins the hand")
        computer_cards += 1
        player_cards -= 1
    else:
        print("Tie. No one wins. Everyone keeps their cards.")
    
    print()
if player_cards > computer_cards:
    print("Player wins the game!")
elif computer_cards > player_cards:
    print("Computer wins the game!")
