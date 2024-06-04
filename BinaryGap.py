def solution(N):
    longest_gap = 0
    counter = 0
    for n in bin(N)[2:]:
        if n == "1":
            longest_gap = max(counter, longest_gap)
            counter = 0
        else:
            counter += 1
    return longest_gap

if __name__ == '__main__':
    N = 529
    print(solution(N))