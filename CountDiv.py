# Prefix Sum
def solutions(A, B, K):
    end = B // K
    div , mod = divmod(A, K)
    if mod == 0:
        count = end - div + 1
    else:
        count = end - div
    return count

if __name__ == '__main__':
    A = 0
    B = 11
    K = 3
    print(solutions(A, B, K))