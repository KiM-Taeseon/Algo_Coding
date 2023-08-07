from sys import stdin
input = stdin.readline

# 이 문제는 답지의 내용과 다르게 내가 좀 더 간단하게 이중문과 min을 섞어서 작성하였다.
# 아이디어 : 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는다.
n, m = map(int, input().split())
result = 0

for i in range(n) : 
    data = list(map(int, input().split()))
    for a in data : 
        # 현재 줄에서 가장 작은 수 찾기
        min_value = min(data)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
    