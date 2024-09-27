arr = list(map(int, input().split()))

def main(arr):
    now = arr[0] - arr[1]
    for i in range(2, len(arr)):
        if arr[i - 1] - arr[i] != now:
            return 'mixed'
    if now == 1:
        return 'descending'
    else:
        return 'ascending'

print(main(arr))