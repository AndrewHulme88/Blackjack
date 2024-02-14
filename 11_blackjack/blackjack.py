import random

def new_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0

    def deal_card():
        return random.choice(cards)

    def calculate_score(hand):
        score = sum(hand)
        if score > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
            score = sum(hand)
        return score

    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

    print(f"Dealer's cards: {dealer_hand[0]} Total score: {dealer_hand[0]}")
    print(f"Player's cards: {player_hand} Total score: {sum(player_hand)}")

    continue_playing = True
    while continue_playing:
        if sum(player_hand) < 21:
            choice = input("Would you like to draw another card? [y/n]")
            if choice == "y":
                    player_hand.append(deal_card())
                    print(f"Player's cards: {player_hand} Total score: {sum(player_hand)}")
            else:
                continue_playing = False
        else:
            continue_playing = False

    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Dealer's cards: {dealer_hand} Total score: {dealer_score}")
    print(f"Player's cards: {player_hand} Total score: {player_score}")

    if player_score > 21:
        print("You Bust> You Lose!")
    elif dealer_score > 21:
        print("Dealer Busts! You Win!")
    elif player_score > dealer_score:
        print("You Win!")
    elif player_score < dealer_score:
        print("You Lose!")
    else:
        print("It's a draw!")
        
    play_again = input("Would you like to play again? [y/n]")
    if play_again == "y":
        new_game()
    else:
        exit()


new_game()


