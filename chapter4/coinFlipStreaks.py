import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    coin = []
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        coin.append(random.randint(0, 1))    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(94):
        if coin[i-1]+coin[i]+coin[i+1]+coin[i+2]+coin[i+3]+coin[i+4]==6:
            numberOfStreaks += 1
            
        elif coin[i-1]+coin[i]+coin[i+1]+coin[i+2]+coin[i+3]+coin[i+4]==0:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 64 / 10000 * 100))