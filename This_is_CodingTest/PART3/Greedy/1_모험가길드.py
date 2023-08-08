from sys import stdin
input = stdin.readline

# 아이디어 : 오름차순으로 정렬하여 항상 최소한의 수를 포함하여 그룹을 결성하게 되고, 그렇게 되면 최대한 많은 그룹이 구성된다.
N = int(input())
data = list(map(int, input().split())) # 정렬하려면 무조건 list형태!
data.sort()

group = 0 # 총 그룹의 수 
people = 0 # 현재 그룹에 포함된 모험가의 수

for i in data : 
    people += 1 # 현재 그룹에 해당 모험가 포함
    # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성!
    if people >= i : 
        group += 1
        people = 0 # 현재 그룹의 모험가 수 초기화

print(group)
