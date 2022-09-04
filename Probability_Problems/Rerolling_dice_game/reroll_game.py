# Import shuffle to generate random dice roll
from random import shuffle

def reroll_game(dice,n):

  '''
  A function that given a list of positive integers 'dice' as
  input, and a positive integer 'n', returns a random list entry,
  where you are given the option, but not the requirement,
  to repeat this process up to n times. 
  '''

  # Expectation for a dice game without rerolling
  expect,best=sum(dice)/len(dice),max(dice)

  # Define temporary variables p and tmp
  p,tmp=0,0

  # Loop to generate expectation depending on rerolls
  for _ in range(n):
      for num in dice:
          if num<expect:
              p+=1
          elif num>=expect:
              tmp+=num
      expect=(p/len(dice))*expect+(tmp/len(dice))

      # Reset the game to re-calculate expectation
      p,tmp=0,0

  # Proceed to play the game
  for _ in range(n+1):
      shuffle(dice)
      if dice[0]>=expect:
          return dice[0]
  return dice[0]

# Input number of re-rolls and simulations
while True:
  try:
    n=input("Enter the number of re-rolls: ")
    n=int(n)
    break
  except ValueError:
    print("Not a valid input for re-rolls! Please try again ...")

while True:
  try:
    sims=input("Enter the number of simulations: ")
    sims=int(sims)
    break
  except ValueError:
    print("Not a valid input for the number of simulations! "
    +"Please try again ...")

# Perform Monte Carlo simulations
total,dice=0,[x for x in range(1,7)]
for _ in range(sims):
    total+=reroll_game(dice,n)
print(total/sims)
