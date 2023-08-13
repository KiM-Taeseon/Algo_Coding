from itertools import combinations


from sys import stdin
input = stdin.readline

# 아이디어 : 조합 라이브러리를 활용하여 볼링공의 조합의 수를 구하고, 두 볼링공의 무게가 같은 경우의 수는 제외한다.
# 책에 써있는 코드와는 다르게 python에 존재하는 combinations 라이브러리를 활용하여 문제를 품
# 문제 조건에 '서로 무게가 다른 볼링공을 고르려고 한다' 라는 말이 명시되어 있음 (문제 잘 읽기!)
n, m = map(int, input().split())
data = list(map(int, input().split()))

case = list(combinations(data, 2)) # 2개를 구하는 조합의 수
result = 0

for i in case : 
    # 두 볼링공의 무게가 같은 경우를 제외
    if i[0] != i[1] :
        result += 1

print(result)