import random as rd

def bottom_to_top(deck):
    bottom=deck[len(deck)-1]
    count=0
    while deck[0]!=bottom:
        idx=rd.randrange(len(deck))
        tmp=deck[0]
        for i in range(idx):
            deck[i]=deck[i+1]
        deck[idx]=tmp
        count+=1
    return count

deck=[x for x in range(52)]
rd.shuffle(deck)

total=0
for _ in range(1000):
    total+=bottom_to_top(deck)

print(int(total/1000))
