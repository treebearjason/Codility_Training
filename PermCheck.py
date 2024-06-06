def solution(A):
    S = sum(range(len(A)+ 1))
    tracker_l = [0] * len(A)
    tracker_sum = 0
    for a in A:
        if a > len(A):
            return 0
        if tracker_l[a-1] == 0:
            tracker_sum += a
        tracker_l[a-1] = a
    if tracker_sum == S:
        return 1
    else: 
        return 0

if __name__ == '__main__':
    A = [1,1,3,2]
    print(solution(A))