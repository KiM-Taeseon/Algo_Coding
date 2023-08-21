from sys import stdin
input = stdin.readline


# **전형적인 시뮬레이션(이동경로) 문제. 문제에서 요구하는 내용을 성실하게 구현하기만!** 
# 아이디어 : dx, dy 리스트를 만들어 방향을 정하고 구현을 시작
# 참고 : 일단 이동 후, 조건에 맞다면 값 저장
n, m = map(int, input().split())

# 방문한 위치를 저장할 수 있는 맵 생성 및 초기화
# 2차원 리스트를 초기화 시키는 방법 꼭 기억!
v = [[0] * m for _ in range(n)]     # 리스트 컴프리헨션
x, y, direction = map(int, input().split())
v[x][y] = 1

# 전체 맵 생성 및 입력값 받기
array = []
for i in range(n) : 
    array.append(list(map(int, input().split())))

# 방향 정의 (문제에 나와 있는대로!) => 무조건 dx와 북을 맨 앞 기준으로!!!
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽방향 도는 함수 정의
def turn_left() : 
    # 함수 바깥에서 선언된 direction 변수를 끌어쓰기 위해 global
    global direction
    direction -= 1
    if direction == -1 : 
        direction = 3

# 초기화
count = 1
turn_time = 0

# 반복문(구현 시작)
while True : 
    turn_left()
    # 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 이후 조건에 맞다면 방문 배열 체크 및 값 옮기기
    if v[nx][ny] == 0 and array[nx][ny] == 0 : 
        v[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 이후 가보지 않은 칸이 없거나 바다인 경우
    else : 
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4 : 
        # 이동
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0 : 
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else : 
            break
        turn_time = 0

print(count)