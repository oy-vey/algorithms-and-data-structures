# Uses python3
def edit_distance(s, t):
    D=[]
    m = len(t)
    n = len(s)
    for i in range(0,n + 1):
        D.append([])
        for j in range(0,m + 1):
            if j == 0:
                D[i].append(i)
            elif i == 0:
                D[i].append(j)
            else:
                D[i].append(-1)
    for j in range(1,m+1):
        for i in range(1,n+1):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i - 1][ j - 1] + 1
            if(s[i-1]==t[j-1]):
                D[i][j] = min(insertion,deletion,match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
