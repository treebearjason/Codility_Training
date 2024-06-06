def solution(X, A):
    step_counter, tracker_sum = 0, 0
    tracker_l = [0] * X
    total = sum(range(X+1))
    for a in A:
        if tracker_l[a-1] == 0:
            tracker_sum += a

        tracker_l[a-1] = a
        step_counter += 1

        if tracker_sum == total:
            return step_counter - 1
    return -1

if __name__ == '__main__':
    A = [1,3,1,4,2,3,5,4]
    print(solution(5, A))