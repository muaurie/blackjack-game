import random
#blackjack or 21 game
#dealer cards
dealer_cards = []
#player cards
player_cards = []
#deal cards
# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has: ", dealer_cards[1])

while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have ", player_cards)

        
#display cards
#sum of dealer card, only see 1 of dealers cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and winss!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")
#sum of player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit? "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break
if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You win! 21.")
#compare the sums between d and p
#if p card <21, BUST
#if p card sum less than 21 = option hit or stay
#if p option stay, compare sum of d v p 
#if p sum < 21 && > D sum then P wins
#If P sum < D sum then P loses
