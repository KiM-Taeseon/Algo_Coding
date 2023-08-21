from sys import stdin
input = stdin.readline

# 입력값 받기
data = input().strip()
# 현재 나이트의 위치값 초기 설정
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 모든 값 정의
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (1,2), (1, -2), (2, 1)]

# 이동하고자 하는 위치 이동
result = 0
for step in steps : 
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 가능유무 확인
    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8 : 
        result += 1

print(result)
