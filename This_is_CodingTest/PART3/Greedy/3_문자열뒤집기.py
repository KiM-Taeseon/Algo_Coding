from sys import stdin
input = stdin.readline

# 아이디어 : 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산
# 이중 if문이어서 헷갈림. 코드를 잘 따라가야 함...
s = input().strip()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫번째 원소부터 먼저 처리한 다음, 그 다음은 for문으로 다시 처리!
if s[0] == '1' :
    count0 += 1
else :
    count1 += 1

for i in range(len(s) - 1) :
    if s[i] != s[i + 1] :
        # 다음 수에서 1로 바뀌는 경우 => 0으로 바꿔준다.
        if s[i + 1] == '1' :
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우 => 1로 바꿔준다.
        else : 
            count1 += 1

print(min(count0, count1))