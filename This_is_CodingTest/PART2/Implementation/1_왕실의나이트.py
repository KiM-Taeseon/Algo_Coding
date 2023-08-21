from sys import stdin
input = stdin.readline

# 아이디어 : 이동경로를 steps 변수에 모두 저장한 다음, 반복문을 통해 현재 위치에 이동 경로를 더하여 마지막으로 가능여부를 확인한다.
# 참고 : 이동할 방향을 dx, dy 리스트를 선언하여 기록하거나, 하나의 변수를 통해 모든 경로를 선언 및 저장하여 기록할 수도 있다.
# 두 가지 모두 구현에 자주 사용되므로 반복숙달하자!

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
