def solutions(A):
    d = {}
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for k, v in d.items():
        if v % 2 == 1:
            return k

if __name__ == '__main__':
    A = [9,3,9,3,9,7,9]
    print(solutions(A))