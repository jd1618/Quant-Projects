# Import shuffle to generate random dice roll
from random import shuffle

def reroll_game(dice,n):

  '''
  A function that given a list of positive integers as input,
  and a positive integer n, returns the outcome of a dice game,
  where you are given the option, but not required, to reroll 
  the dice n times
  
  expect - expected value of the game,
  lesser_frequency - the number of integers less than expect,
  greater_sum - the sum of numbers greater than expect
  '''

  expect=sum(dice)/len(dice)
  lesser_frequency,greater_sum=0,0
  
  # Loop to generate expectation depending on rerolls
  for _ in range(n):
      for num in dice:
          if num<expect:
              lesser_frequency+=1
          elif num>=expect:
              tmp+=num
      expect=(lesser_frequency/len(dice))*expect
      +greater_sum/len(dice)
      p,tmp=0,0

  for _ in range(n+1):
      shuffle(dice)
      if dice[0]>=expect:
          return dice[0]
  return dice[0]

# Generate a list representing a dice with sides 1 to 6
dice=[x for x in range(1,7)]
total=0

# Perform Monte Carlo simulations
for _ in range(1000):
    total+=reroll_game(dice,0)

print(total/1000)
