def solutions(A):
    min_diff = 2000
    N = len(A)
    S = sum(A)
    SL = 0
    for p in range(N-1):
        SL += A[p]
        
        diff = abs(2 * SL - S)
        min_diff = min(min_diff, diff)
    return min(min_diff, diff)



if __name__ == '__main__':
    A = [3,1,2,4,3]
    print(solutions(A))