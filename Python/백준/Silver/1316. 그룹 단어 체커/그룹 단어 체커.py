# 그룹 단어 체커

def check_group(string):
    box = [string[0]]
    for i in range(1, len(string)):
        # 만약 앞에꺼랑 다르다면,
        if string[i] != string[i - 1]:
            # 그리고 이미 나온거라면
            if string[i] in box:
                return False
            else:
                box.append(string[i])
    return True  

n = int(input())
cnt = 0
for _ in range(n):
    sentense = input()
    if check_group(sentense):
        cnt += 1
print(cnt)