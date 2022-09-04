# Import shuffle to shuffle a deck of cards
from random import shuffle

def expected_turns(deck):

    '''
    A function that given a list of distinct positive integers 'deck'
    returns the expected number of times you need to rearrange the list
    and observe the first entry until you have seen every element.
    '''

    # Keep track of cards seen and turns taken
    count,turns=0,0

    # Record any new cards 
    cards_seen=set()

    while count<len(deck):
        if deck[0] not in cards_seen:
            cards_seen.add(deck[0])
            count+=1
        shuffle(deck)
        turns+=1
    return turns

# Setting up the problem with exceptions
while True:
  try:
    n=input("Enter the number of cards in the deck: ")
    n=int(n)
    break
  except ValueError:
    print("Not a valid input for the number of cards! "
    +"Please try again ...")

while True:
  try:
    sims=input("Enter the number of simulations: ")
    sims=int(sims)
    break
  except ValueError:
    print("Not a valid input for the number of simulations! "
    +"Please try again ...")
avg_turns,deck=0,[x for x in range(n)]

# Performing Monte Carlo simulations
for _ in range(sims):
    avg_turns+=expected_turns(deck)
avg_turns/=sims
print(int(avg_turns))
