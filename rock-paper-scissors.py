import random

c = random.randint(0, 2)
print(c)
p = int(input('0 = rock, 1 = paper, 2 = scissors: '))

if (c == p):
    print('equal')
else: 
    s = c - p
    if (s == 1):
        print('win')
    else:
        print('lost')




