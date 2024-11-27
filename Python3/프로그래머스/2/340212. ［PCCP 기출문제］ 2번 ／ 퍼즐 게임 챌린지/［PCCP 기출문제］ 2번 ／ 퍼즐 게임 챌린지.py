# level에 따라 걸리는 시간을 반환하는 함수?
def calTime(level, diffs, times):
    result = 0
    for i in range(len(diffs)):
        cnt = diffs[i] - level
        # level이 더 크다면 그냥 더해줌
        if cnt <= 0:
            result += times[i]
        else:
            if i == 0:
                result += cnt * times[i] + times[i]
            else:
                result += cnt * (times[i - 1] + times[i]) + times[i]
    return result

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if calTime(mid, diffs, times) > limit:
            left = mid + 1
        else:
            right = mid - 1

    return (left + right) // 2 + 1