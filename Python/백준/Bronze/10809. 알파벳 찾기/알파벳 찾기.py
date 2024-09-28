# 알파벳찾기

alphabets = [-1 for _ in range(26)]

sentense = input()
for i in range(len(sentense)):
    alpha = sentense[i]
    if alphabets[ord(alpha) - 97] == -1:
        alphabets[ord(alpha) - 97] = i

print(*alphabets)