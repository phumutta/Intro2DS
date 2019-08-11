import itertools,random

num=["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
suites = ["Hearts", "Clubs", "Diamonds", "Spades"]
deck= list(itertools.product(num,suites))

random.shuffle(deck)
for i in range(0,3):
    print(deck[i] )



