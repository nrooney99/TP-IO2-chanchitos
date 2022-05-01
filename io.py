import random
import statistics
import numpy as np
import pandas as pd

p=5 # cantidad de jugadores
g=1000 # cantidad de juegos
n=[] # array de rondas por juego

def rollDice():
    return int(random.random()*6)+1
for k in range(g):
    state = [[0 for col in range(5)] for row in range(p)]
    win=False
    for r in range(100):
        if win == True:
            n.append(r)
            break
        for i in state:
            dice= rollDice()
            ant=i[:]
            if dice == 6:
                for j in range(len(i)):
                    if i[j]==1:
                        i[j]=0
                        break
            elif dice in [1,2,3,4]:
                i[dice-1]=1
            elif i==[1,1,1,1,0]:
                win=True
                # print(dice)
                break
            # print('dice: ' + str(dice))
            # print(ant)
            # print(i)
            # print('--------------')

s = pd.Series(n)
print(s)
print(statistics.mean(n))
print(statistics.pstdev(n))

