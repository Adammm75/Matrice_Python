import random

matrice=[[0,0,0],[0,0,0],[0,0,0]]

for i in range (3):
    for j in range (3):
        matrice[i][j]=random.randint(0,9)
for a in matrice:
    print(a)
