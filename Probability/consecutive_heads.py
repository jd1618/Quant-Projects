from random import shuffle

def consecutive_heads(n):
    toss=0
    outcomes=[1,-1]
    for _ in range(n):
        shuffle(outcomes)
        outcome=outcomes[0]
        if toss==1 and outcome==1:
            return 0
        if toss!=outcome:
            toss=outcome
    return 1

# Input number of coins tosses and simulations
while True:
  try:
    n=input("Enter the number of coin tosses: ")
    n=int(n)
    break
  except ValueError:
    print("Not a valid input for number of coin tosses! Please try again ...")

while True:
  try:
    sims=input("Enter the number of simulations: ")
    sims=int(sims)
    break
  except ValueError:
    print("Not a valid input for the number of simulations! "
    +"Please try again ...")

total=0
for _ in range(sims):
    total+=consecutive_heads(n)

print(total/sims)
