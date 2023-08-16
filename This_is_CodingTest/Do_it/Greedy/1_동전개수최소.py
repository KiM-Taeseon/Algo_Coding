from sys import stdin
input = stdin.readline

# 아이디어 : 가장 큰 가격부터 내림차순으로 탐색 몫을 카운터에 더하고 나머지로 계속 탐색
# 책이랑은 다르게 int로 하지않고 몫만 나올 수 있는 // 사용
n, k = map(int, input().split())
a = [0] * n # 배열 초기화

for i in range(n) : 
    a[i] = int(input()) # 입력값을 배열로 만들 때는 이런식으로!

count = 0

for i in range(n - 1, -1, -1) : # 내림차순으로 for문 돌리기
    if a[i] <= k : # i가 아니라 a[i]!!!
        count += k // a[i] 
        k = k % a[i]

print(count)