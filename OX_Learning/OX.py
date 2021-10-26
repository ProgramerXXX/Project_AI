import numpy as np 
import random 

O = []
X = []
win = [[1,2,3],
       [4,5,6],
       [7,8,9],
       [1,5,9],
       [3,5,7],
       [1,4,7],
       [2,5,8],
       [3,6,9]
      ]
def checkWin(P):
    for w in win:
        if all(x-1 in P for x in w):
            return True
    return False

def displayOX():
    OX = np.array(['']*9)
    OX[O] = ['O']
    OX[X] = ['X']
    print(OX.reshape([3,3]))

def AI():
    validmove = list(set(range(9)) - set(O+X))
    V = [-100] *900 
    for m in validmove:
        tempX = X + [m]
        V[m], criticalMove = evalOX(O,tempX)
        if len(criticalMove) > 0:
            move = [i-1 for i in criticalMove if i-1 in validmove]
            return random.choice(move)
    maxV = max(V)
    imaxV = [i for i,j in enumerate(V) if j == maxV]
    return random.choice(imaxV)

def evalOX(O,X):
    SO,SX,criticalmove = calOX(O,X)
    return 1 + SX - SO , criticalmove

def calOX(O,X):
    SO = SX = 0
    criticalmove = []
    for w in win:
        O = [i-1 in O for i in w]
        X = [i-1 in X for i in w]
        if not any(X):
            nO = O.count(True)
            SO += nO
            if nO == 2:
                print('criticalmove',w)
                criticalmove = w 
            if not any(O):
                SX += X.count(True)
    return SO,SX,criticalmove

while True:
    move  = int(input('choose position [1-9]')) -1 
    while move in O+X or move > 8 or move < 0 :
        move = int(input('bad move : chose position [1-9]'))-1
    O.append(move)
    displayOX()
    if checkWin(O):
        print('O win')
        break 
    if len(O) + len(X)  == 9:
        print('Draw')
        break
    X.append(AI())
    displayOX()
    if checkWin(X):
        print('X win')
        break 
    if len(O) + len(X) == 9:
        print('Draw')
        break

