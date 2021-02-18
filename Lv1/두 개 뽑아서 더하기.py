def solution(numbers):
    sums = []

    for a in range(len(numbers)):
        for b in range(len(numbers)):
            if a != b and a < b:
                sum = numbers[a] + numbers[b]
                if sum not in sums:
                    sums.append(sum)
    sums.sort()

    return sums