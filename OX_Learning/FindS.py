
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
    X = [['Sunny','Warm','Normal','Strong','Warm','Same'],
         ['Sunny','Warm','High','Strong','Warm','Same'],
         ['Rainy','Cold','High','Strong','Warm','Change'],
         ['Sunny','Warm','High','Strong','Cool','Change']
    ]
    T =['Yes','Yes','No','Yes']
    S = FindS(X,T)
    print(S)