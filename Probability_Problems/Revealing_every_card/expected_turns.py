# Import shuffle to shuffle a deck of cards
from random import shuffle

def expected_turns(deck):
    
    '''
    A function that given a deck of cards, where each card is distinct, 
    returns the expected number of times you need to turn over the top
    card, record what it is, put the card back in the deck, shuffle
    and repeat this procedure in order to see every card in the deck.
    
    count - keeps track of the number of new cards you have seen,
    turns - keeps track of the number of turns you play this game, 
    cards_seen - records the cards you have seen.
    '''
    
    count,turns=0,0
    cards_seen=set()
    while count<len(deck):
        if deck[0] not in cards_seen:
            cards_seen.add(deck[0])
            count+=1
        shuffle(deck)
        turns+=1
    return turns

# Setting up the problem
deck=[x for x in range(input("Enter the size of the deck of cards: "))]
average_turns,simulations=0,int(input("Enter the number of simulations: "))

# Performing Monte Carlo simulations
for _ in range(simulations):
    average_turns+=expected_turns(deck)
average_turns/=simulations
print(int(average_turns))
