import sys
input = sys.stdin.readline

def solve(lst, target):
    low, high = 1, max(lst)
    result, count = 0, 0
    while low <= high:
        count = 0
        mid = (low + high) // 2
        for i in lst:
            if i % mid == 0: count += (i // mid)
            else: count = count + (i // mid) + 1
        if count > target:
            low = mid + 1
        else:
            result = mid
            high = mid - 1

    return result
N, M = map(int, input().split())
color = []
for _ in range(M):
    color.append(int(input()))
print(solve(color, N))