def solutions_slow(X, Y, D):
    counter = 0
    while(X < Y):
        X += D
        counter += 1
    return counter

def solutions(X, Y, D):
    ans = (Y - X) / D
    q, r = divmod(ans, 1)
    return int(q) + bool(r)

if __name__ == '__main__':
    X = 1
    Y = 5
    D = 2
    print(solutions(X, Y, D))