def solution(edges):
    # 우선 노드 수 구하기
    max_num = 0 
    for edge in edges:
        for num in edge:
            if num > max_num:
                max_num = num
    
    # in과 out이 각 몇개인지 구하기
    in_out = [[0, 0] for _ in range(max_num)]
    exist = [0 for _ in range(max_num)]
    for edge in edges:
        in_out[edge[0] - 1][1] += 1
        in_out[edge[1] - 1][0] += 1
        exist[edge[0] - 1] += 1
        exist[edge[1] - 1] += 1
    
    # in은 없으면서 out이 2개 이상인 애 찾기 -> 걔가 추가된 edge
    added_edge = 0
    for i in range(max_num):
        in_cnt, out_cnt = in_out[i]
        if in_cnt == 0 and out_cnt >= 2:
            added_edge = i + 1
            
    # 추가된 edge빼고 계산해보기
    new_edges = [[0, 0] for _ in range(max_num)]
    all = 0
    for edge in edges:
        if added_edge not in edge:
            new_edges[edge[0] - 1][1] += 1
            new_edges[edge[1] - 1][0] += 1
        else:
            all += 1
            
    donut = 0 
    macdae = 0
    palja = 0
    for i in range(max_num):
        new_edge = new_edges[i]
        if exist[i] != 0:
            # 이건 막대 그래프
            if new_edge[0] == 0 and i != added_edge - 1:
                macdae += 1
            if new_edge == [2, 2]:
                palja += 1
    
    donut = all - macdae - palja
            
    return [added_edge, donut, macdae, palja]
    
    
    
    