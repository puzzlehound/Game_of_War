import random

#This program simulates the card game War.
#A deck of 52 cards is shuffled and dealt out face-down to the players.
#The object of the game is to play until one player has all the cards
#Each player keeps their pile of cards face down and does not look at their cards.
#For each round of play, each player turns over the top card in their pile of cards.
#The highest card (disregarding suit) wins and that player gets all the cards used in that round.
#The game ends when one player has all the cards.
#If more than one card with the same rank is played in a round and there is a tie, there is a war.
#In a war, each player puts out a card face down and another card face up.
#The winner of the war is determined from the face-up cards.
#The winner adds the newly won cards to the bottom of their pile.
#War continues if there is another tie until there is a winner.
#The winner gets all the cards used in the war(s).
#If one of the players runs out of cards in the middle of a war, that player loses the war.

#In regular play, the winner wins 2 cards and cards are added to the bottom of the winners pile
#in the same order every time -- first player 1's card, then player 2's card.

#When there is a war, the winner wins 6 cards -- 3 cards in the order played from each player.
#The program swaps the middle card from each player with the middle card from the other player.
#This adjustment is necessary to avoid creating an endless game
#which can happen when you keep everything in the same order.
#I had originally kept the 6 cards in the same order from each player
#but ran into the problem of frequently creating an endless game.
#Keeping the cards in the exact same order caused winning hands to oscillate player 1 and player 2 endlessly.
#Each player stayed at approximately 26 cards in their pile
#In one instance where I let it run for awhile to see what would happen,
#the number of hands played became more than 1 million before I killed the instance.


#Letting wars continue in event of tie became problematic #since I have not mastered recursion yet.
#Without using recursion, I would have had to keep nesting if, elif, else loops infinitely.
#So for simplicity, if there is a tie on a second war, each player just
#takes back their own cards to puts at the bottom of their pile.

def create_card_list():
    #this function creates cards and puts them in order into a deck

    #Each card will have the following attributes:
    # -face with suit
    # -value

    #list of suits in unicode
    suits = ['\u2663', '\u2666', '\u2665', '\u2660']
    #list of face type of card in string format
    face_type = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    #list to deck of cards
    cards = []
    #iterate for all face_values and all suits to create a list of records for each card
    for value in range(len(face_type)):
        for suit in suits:
            #create record by mapping index # to face value and adding suit info
            card_string = face_type[value] + suit
            card = [card_string, value]
            cards.append(card)
    return(cards)

def shuffle_deck(deck):
    #shuffle the deck by randomly choosing cards and creating list in order of random choosing
    shuffled = []
    deck_copy = deck.copy()
    for i in range(52):
        card = random.choice(deck_copy)
        shuffled.append(card)
        deck_copy.remove(card)
    return(shuffled)

def deal_cards(shuffled):
    done = False
    player1 = []
    player2 = []
    #num_cards_each = int(52 / 2)
    while not done:
        player1.append(shuffled.pop())
        player2.append(shuffled.pop())
        done = shuffled == []
    return player1, player2

def play_hand(player1, player2):
    #setup initial condition for while loop
    done = False
    #set up counters for hands played, # of wins per player, # of wars played
    hands_count = 0
    player1_wins_count = 0
    player2_wins_count = 0
    wars_played = 0
    wars_with_no_winners = 0
    while not done:
        print("Turn over top card of your pile.")
        print("player 1: " + str(player1[0][0]))
        print("player 2: " + str(player2[0][0]))
        if player1[0][1] == player2[0][1]:
            #first war
            print("We have tie! War!")
            wars_played += 1

            #check if enough cars to finish the War
            #game over if less than 3 cards left for either player
            player1_cards_for_2nd_war = len(player1)
            player2_cards_for_2nd_war = len(player2)
            if player1_cards_for_2nd_war < 3 or player2_cards_for_2nd_war < 3:
                print("GAME OVER - not enough cards left for a War!")
                done = True

            else:
                print("Take top card of your pile and place it face down. Turn over the next card.")
                print("player 1: " + str(player1[2][0]))
                print("player 2: " + str(player2[2][0]))

                if player1[2][1] == player2[2][1]:
                    # for another tied war
                    # - to keep it simple
                    # each player just takes their own cards back that were played
                    print("War #2 tied!  Everyone take back your own cards.")

                    # minor shuffling of middle append
                    player1.append(player1[0])
                    player1.append(player2[1])
                    player1.append(player1[2])

                    player2.append(player2[0])
                    player2.append(player1[1])
                    player2.append(player2[2])

                    # remove all used cards from top of pile of both players
                    for x in range(3):
                        del player1[0]
                        del player2[0]

                    wars_played += 1
                    wars_with_no_winners += 1

                elif player1[2][1] > player2[2][1]:
                    # player 1 wins first war
                    print("Player 1 wins!")
                    # player 1 gets all cards played

                    # minor shuffling of middle append
                    player1.append(player1[0])
                    player1.append(player2[1])
                    player1.append(player1[2])

                    player1.append(player2[0])
                    player1.append(player1[1])
                    player1.append(player2[2])

                    # remove all used cards from top of pile of both players
                    for x in range(3):
                        del player1[0]
                        del player2[0]

                    player1_wins_count += 1
                else:
                    # player 2 wins second war
                    print("Player 2 wins!")
                    # player 2 gets all cards played

                    # minor shuffling of middle append
                    player2.append(player1[0])
                    player2.append(player2[1])
                    player2.append(player1[2])

                    player2.append(player2[0])
                    player2.append(player1[1])
                    player2.append(player2[2])

                    # remove all used cards from top of pile of both players
                    for x in range(3):
                        del player1[0]
                        del player2[0]

                    player2_wins_count += 1

        elif player1[0][1] > player2[0][1]:
            # player 1 wins hand
            print("Player 1 wins!")
            # player 1 gets all cards played
            player1.append(player2[0])
            player1.append(player1[0])
            # remove all used cards from top of pile of both players
            del player1[0]
            del player2[0]

            player1_wins_count += 1

        else:
            print("Player 2 wins!")
            player2.append(player1[0])
            player2.append(player2[0])
            # remove all used cards from top of pile of both players
            del player1[0]
            del player2[0]

            player2_wins_count += 1

        hands_count += 1
        print("hands played = " + str(hands_count))

        player1_cards_left = len(player1)
        player2_cards_left = len(player2)
        total_cards = player1_cards_left + player2_cards_left

        print("player 1 # cards = " + str(len(player1)))
        print("player 2 # cards = " + str(len(player2)))
        #print("total cards in play = " + str(total_cards))
        #print("player 1 wins = " + str(player1_wins_count))
        #print("player 2 wins = " + str(player2_wins_count))
        #print("wars played = " + str(wars_played))
        #print("wars with no winners = " + str(wars_with_no_winners))
        print('\n')


        # if done already triggered above or players run out of cards
        done = done or player1 == [] or player2 ==[]

    #print(player1)
    #print(len(player1))
    return player1, player2, hands_count, player1_wins_count, player2_wins_count, wars_played, wars_with_no_winners



def main():
    #greeting & confirming # of players
    print("Hi!  Let's play War!")
    players = 2
    print("Confirming", players,"people playing!")
    print("\n")

    #create deck of cards, print contents & confirm # of cards
    deck = create_card_list()
    print("Here is the new deck: " + "\n" + str(deck))
    y = len(deck)
    print("Confirming # of cards: " + str(y))
    print("\n")

    #shuffle the deck, print contents of shuffled deck & confirm # of cards
    shuffled = shuffle_deck(deck)
    print("Here is the shuffled deck:  " + "\n" + str(shuffled))
    print("Confirming # of cards: " + str(len(shuffled)))
    print("\n")

    #deal cards, print contents of each player & confirm # of cards
    player1, player2 = deal_cards(shuffled)
    print("Player 1's pile (shhhh! They can't see this): " + str(player1))
    print("Player 1 # of cards: " + str(len(player1)))
    print("\n")
    print("Player 2's pile (shhhh! They can't see this): ")
    print(str(player2))
    print("Player 2 # of cards: " + str(len(player2)))
    print("\n")

    #play hands, print stats & outcomes
    player1, player2, hands_count, player1_wins_count, player2_wins_count, wars_played, wars_with_no_winners = play_hand(player1, player2)
    print("FINAL RESULTS")
    #celebrates the winner!
    if player1_wins_count > player2_wins_count:
        print("Player 1 wins it all!")
    else:
        print("Player 2 wins it all!")
    #stats on the game
    print("hands played = " + str(hands_count))
    print("player 1 wins = " + str(player1_wins_count))
    print("player 2 wins = " + str(player2_wins_count))
    print("wars played = " + str(wars_played))
    print("wars with no winners = " + str(wars_with_no_winners))
    if player1 == []:
        print("Player 1 has no cards left")
    else:
        print("Player 1 has these cards: " +"\n" + str(player1))
        print(str(len(player1)) + " cards")
    if player2 == []:
        print("Player 2 has no cards left")
    else:
        print("Player 2 has these cards: " +"\n" + str(player2))
        print(str(len(player2)) + " cards")

if __name__ == '__main__':
    main()