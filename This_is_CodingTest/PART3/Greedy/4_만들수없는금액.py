from sys import stdin
input = stdin.readline

# 아이디어 : 오름차순 정렬을 한 뒤, 1부터 차례대로 target 금액을 만들 수 있는지 확인하여 만들 수 있다면, 
# target값을 증가(업데이트)시키는 방식
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 처음에는 금액 1을 만들 수 있는지 확인하기 위해, target = 1을 설정한다. 
# (입력예시에 1이 포함되는 것 밖에 없기 때문에 target = 1 설정이 가능)
# target값이 for문을 돌면서 증가하면서 업데이트 되면 그 전까지의 수의 모든 금액을 만들 수 있다는 말과 같다.
target = 1
for i in data : 
    if target < i : 
        break
    else : 
        target += i

print(target)