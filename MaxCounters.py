def solutions(N, A):
    res = [0] * N
    low_max, curr_max = 0, 0
    for ops in A:
        if ops <= N:
            pos = ops - 1
            res[pos] = max(res[pos], low_max)
            res[pos] += 1
            curr_max = max(curr_max, res[pos])
        else:
            low_max = curr_max
    for i, r in enumerate(res):
        res[i] = max(res[i], low_max)

    return res


if __name__ == '__main__':
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solutions(N, A))