def solutions(A):
    all_values = [i for i in range(1,len(A)+2)]
    print(all_values)
    res_l = set(all_values) - set(A)
    return list(res_l)[0]


if __name__ == '__main__':
    A = [2,3,1,5]
    print(solutions(A))