# Import shuffle to shuffle a deck of cards
from random import shuffle

def expected_turns(deck):
    count,turns=0,0
    hashset=set()
    while count<len(deck):
        if deck[0] not in hashset:
            hashset.add(deck[0])
            count+=1
        shuffle(deck)
        turns+=1
    return turns

deck=[x for x in range(input("Enter the size of the deck of cards: "))]
average_turns,simulations=0,int(input("Enter the number of simulations: "))
for _ in range(simulations):
    average_turns+=expected_turns(deck)
average_turns/=simulations
print(int(average_turns))
