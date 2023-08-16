from sys import stdin 
input = stdin.readline

# 아이디어 : 최솟값을 만들기 위해서는 최대한 큰 수를 빼야 한다. (더하기 연산을 모두 실행한 뒤, 가장 앞에 있는 값에서 빼준다.)
# def로 정의해서 푸는 게 어려움 (문제 이해는 했는데 혼자 하면 못 풀겠음)

a = list(map(str, input().split("-")))  # str을 -를 구분으로 나눠서 리스트에 저장

def mySum(i) :  # 나뉜 그룹의 더하기 연산 수행 
    sum = 0
    temp = str(i).split("+")
    for i in temp : 
        sum += int(i)
    return sum

answer = 0

for i in range(len(a)) : 
    temp = mySum(a[i])
    if i == 0 : 
        answer += temp  # 가장 앞에 있는 것만 더함
    else : 
        answer -= temp  # 뒷부분은 더한 값들이므로 뺌.

print(answer)