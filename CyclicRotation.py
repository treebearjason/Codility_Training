def solution(A, K):
    if A:
        for _ in range(K):
            A.insert(0, A.pop())
    return A


if __name__ == '__main__':
    A = []
    K = 3
    print(solution(A, K))