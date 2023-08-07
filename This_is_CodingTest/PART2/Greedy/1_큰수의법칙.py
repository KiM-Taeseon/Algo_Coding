from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split())) # list로 받아야 정렬 가능

data.sort()
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k # //로 나눠야 몫이 정수형태로 나옴(/로 나누면 소수점 형태)
count += m % (k + 1)

'''
가장 큰 수를 k번 더하고 두 번째로 큰 수를 한번 더하는 연산인데
그 연산을 쪼개 반복적인 수열을 찾은 다음, 횟수를 구함 
'''
result = 0
result += (count) * first 
result += (m - count) * second

print(result)