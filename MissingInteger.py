def solutions(A):
    N = [0] * 1000001
    for a in A:
        if a >= 0:
            N[a] += 1
    for i, n in enumerate(N[1:]):
        if n == 0:
            return i + 1



if __name__ == '__main__':
    A = [1000000]
    print(solutions(A))