import random

def uniform_distance():
    x=random.uniform(0,1)
    y=random.uniform(0,2)
    dist=abs(x-y)
    return dist

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
    total+=uniform_distance()
average=total/sims

variance=0
for _ in range(sims):
    variance+=(uniform_distance()-average)**2
variance/=sims

print(average,variance)
