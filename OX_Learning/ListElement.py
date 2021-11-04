import numpy as np
import pandas as pd

def ListElim(X,T):
    X = np.array(X)
    T = np.array(T)
    n = X.shape[1]
    A = []
    for i in range(n):
        A.append(sorted(list(set(X[:,i]))))
    H = []
    t = []
    i = 1

    idx_data = [0] * n 
    while True:
        h = []
        for j in range(n):
            h.append(A[j][idx_data[j]])
        for tt in np.unique(T):
            if isConsist(X,T,h,tt):
                H.append(h)
                t.append(tt)
                print(i, h ,tt)
                i += 1
        
        idx_data[-1] += 1 
        letter_index = n-1
        while idx_data[letter_index] > len(A[letter_index])-1:
            idx_data[letter_index] = 0
            letter_index -= 1 
            if letter_index < 0:
                return H,t
            idx_data[letter_index] += 1 

    return H,t

def isConsist(X,T,h,t):
    for i in range(len(X)):
        if h == list(X[i]):
            if T[i] != t:
                return False
    return True

if __name__ == '__main__':

    data = pd.read_csv('playtennis.csv')
    X = np.array(data.iloc[:,0:-1])
    T = np.array(data.iloc[:,-1])
    # X = [['Sunny','Warm','Normal','Strong','Warm','Same'],
    #      ['Sunny','Warm','High','Strong','Warm','Same'],
    #      ['Rainy','Cold','High','Strong','Warm','Change'],
    #      ['Sunny','Warm','High','Strong','Cool','Change']
    # ]
    # T =['Yes','Yes','No','Yes']

    H,t = ListElim(X,T)
