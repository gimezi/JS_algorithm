# OX 퀴즈

n = int(input())
for _ in range(n):
    test_case = input()
    
    now_score = 0
    total_score = 0

    for case in test_case:
        if case == 'O':
            now_score += 1
            total_score += now_score
        else:
            now_score = 0
    
    print(total_score)