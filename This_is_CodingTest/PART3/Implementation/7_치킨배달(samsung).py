from itertools import combinations
from sys import stdin
input = stdin.readline

# 아이디어 : 치킨집을 최대 m개로 줄여서 집들로부터 m개의 치킨집까지의 거리를 줄이는 것이 목표
# 그 후, 도시의 치킨 거리 합의 최솟값을 계산
# 치킨집 중 에서 m개를 고르는 조합인데, 최대 13개이므로 아무리 많아도 13개에서 m개를 선택하는 조합과 동일
# 치킨집 중에서 m개를 고르는 모든 경우에 대해서 치킨 거리의 합을 계산(완전탐색)하여, 치킨 거리의 최솟값을 구헤서 출력
# 삼성전자 문제인데 어렵다..... 혼자서는 못 풀거 같다...

n, m = map(int, input().split())
chicken, house = [], []

# 새로운 2차원 배열 입력하는 방법 알아두기!!!
for r in range(n) : 
    data = list(map(int, input().split()))
    for c in range(n) : 
        if data[c] == 1 : 
            house.append((r, c))  # 집
        elif data[c] == 2 : 
            chicken.append((r, c))  # 치킨집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수 정의
def distance_sum(candidate) : 
    result = 0
    # 모든 집에 대하여
    for hx, hy in house : 
        temp = 1e9
        # 가장 가까운 치킨집 찾기
        for cx, cy in candidate : 
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
     
    # 치킨 거리의 모든 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates : 
    result = min(result, distance_sum(candidate))

print(result)