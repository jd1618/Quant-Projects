import random
import numpy as np
from math import pi
from math import sqrt

def average_center_distance():
    theta=random.uniform(0,2*pi)
    r=random.uniform(0,1)
    r=r**(1/2)

    x=r*np.cos(theta)
    y=r*np.sin(theta)

    dist=sqrt(x**2+y**2)

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
    total+=average_center_distance()

average=total/sims
variance=0
for _ in range(sims):
    variance+=(average_center_distance()-average)**2

variance/=sims
print(average,variance)
