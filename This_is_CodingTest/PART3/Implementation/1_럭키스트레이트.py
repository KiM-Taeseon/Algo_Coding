from sys import stdin
input = stdin.readline

# 아이디어 : 문제에서 요구하는 데로 그대로 구현
# (자릿수가 짝수 형태로만 이루어져 홀수는 입력으로 들어오지 않는다 해서 이것도 구현 해야하는 지 알았더니 안해도 됨.)
# 참고 : 파이썬의 경우, 입력받은 데이터가 문자열 형태이므로, 각 문자를 하나씩 정수형으로 변환 뒤에 sum 변수에 넣을 수 있다.

n = input().strip()
length = len(n)     # 총 자릿수
sum = 0

for i in range(length // 2) :   # 반 나눠서 왼쪽 부분 자릿수 합 계산하여 더함
    sum += int(n[i])

for i in range(length // 2, length) :   # 오른쪽 부분 자릿수 합 계산하여 뺌
    sum -= int(n[i])

# 왼쪽과 오른쪽 자릿수 합이 동일한지 확인
if sum == 0 : 
    print("LUCKY")
else : 
    print("READY")