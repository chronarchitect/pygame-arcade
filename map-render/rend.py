import os
fill = open('MAP')
str = fill.read().split('\n')
for i in str:
    for j in i:
        if j == 'W':
            print('▧ ', end="")
    print()

