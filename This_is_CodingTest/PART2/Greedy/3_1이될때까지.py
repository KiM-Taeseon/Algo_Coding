from sys import stdin
input = stdin.readline

# 아이디어 : 항상 1을 빼는 것보다 k로 나누기 하는 횟수가 최대한 많아야 최소의 횟수를 만들 수 있는 방법
n, k = map(int, input().split())
result = 0

# 조건에 만족한다면 계속해서 반복해야 하는 조건문이라면 if보다 while! (break문 안 써도 됨)
while n >= k :
    while n % k != 0 :
        n -= 1
        result += 1
    n //= k
    result += 1

# K보다 작은 마지막으로 남은 수에 대해서 1씩 빼기
while n > 1 : 
    n -= 1
    result += 1

print(result)