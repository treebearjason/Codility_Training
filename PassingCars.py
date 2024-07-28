#Prefix Sum
def solutions(A):

    def pSum(A):
        n = len(A)
        p_l = [0] * (n+1)
        for i in range(1,n+1):
            p_l[i]  += p_l[i-1] + A[i-1]
        return p_l

    p = pSum(A)
    
    res = 0
    for i, a in enumerate(A):
        if a == 0:
            res += p[len(A)] - p[i]
            
    if res > 1e9:
        return -1

    return res

if __name__ == '__main__':
    A = [0,1,0,1,1]
    print(solutions(A))