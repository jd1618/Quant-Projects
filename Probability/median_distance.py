import numpy as np
from math import pi
from math import sqrt

def shortest_distance(n):
    shortest_dist=-1
    for _ in range(n):
        # Spherical coordinates
        phi=np.random.uniform(0,2*pi)
        theta=np.random.uniform(0,pi)
        r=np.random.uniform(0,1)

        # Sampling variable due to coordinate transform
        r=r**(1/3)

        x=r*np.sin(theta)*np.cos(phi)
        y=r*np.sin(theta)*np.sin(phi)
        z=r*np.cos(theta)
        dist=sqrt(x**2+y**2+z**2)

        # Tracking the shortest distance
        if shortest_dist<0 or dist<shortest_dist:
            shortest_dist=dist
    return shortest_dist

def median_distance(n,sims):
    shortest_distances=[]
    for _ in range(sims):
        shortest_distances.append(shortest_distance(n))
    shortest_distances.sort()
    if len(shortest_distances)%2!=0:
        mid=len(shortest_distances)//2
        return shortest_distances[mid]
    else:
        left=len(shortest_distances)//2-1
        right=len(shortest_distances)//2
        median=(shortest_distances[left]
        +shortest_distances[right])/2
        return median

while True:
    try:
        n=input("Enter the number of random points: ")
        n=int(n)
        break
    except ValueError:
        print("Not a valid input for the number of points! "
        +"Please try again ...")

while True:
    try:
        sims=input("Enter the number of simulations: ")
        sims=int(sims)
        break
    except ValueError:
        print("Not a valid input for the number of simulations! "
        +"Please try again ...")

print(median_distance(n,sims))
