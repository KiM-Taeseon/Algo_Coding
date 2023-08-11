from sys import stdin
input = stdin.readline

# 아이디어 : 큰 수를 만들 때는 + 보다는 * 가 더 값을 크게 만든다. 하지만 0과 1은 + 가 더 큰 수를 만든다.
# 따라서, 연산을 수행할 때 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱한다.

# 입력값 중에 문자가 여러 개 붙어있는 경우에는, /n(개행문자) 포함하는 stdin.readline를 쓰지 않거나, 
# 만약 쓴다면 입력값에 strip()를 붙여준다. 
s = input().strip()
result = int(s[0]) # 결과 초기값 설정

for i in range(1, len(s)) : # 인덱스 1부터 시작
    num = int(s[i])
    if num <= 1 or result <= 1 :
        result += num
    else : 
        result *= num

print(result)
