import pandas as pd
import numpy as np 

def expend(X,S):
    for i in range(len(S)):
        if X[i] != S[i] and S[i] == '':
            S[i] = X[i]
        elif X[i] != S[i] and S[i] != '':
            S[i] = '?'
    return S

def FindS(X , T):
    S = [''] * len(X[0])
    for i in range(len(X)):
        if T[i] == 'Yes':
            S = expend(X[i],S)
    return S

if __name__ == '__main__':
    data = pd.read_csv('playtennis.csv')
    X = np.array(data.iloc[:,0:-1])
    T = np.array(data.iloc[:,-1])
    S = FindS(X,T)
    print(S)