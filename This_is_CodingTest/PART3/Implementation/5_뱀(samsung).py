from sys import stdin
input = stdin.readline

# 아이디어 : 시물레이션 유형으로, 문제에서 요구하는 대로 실수없이 구현해내야 한다.
# 알게 된 것 
#   1. 동서남북 구현과 동쪽으로 보고 있을 때는 방향 바꿔주기
#   2. python의 음수의 나머지 연산 규칙
#   3. 큐를 생성하고 큐 정의에 따라 꼬리인 맨 앞쪽을 pop(0)을 통해 제거
#   4. nx = x + dx[direction]을 통해 이동하고 조건에 부합한다면, 마지막에 x = nx 해주기
#   5. def 함수로 print 출력하기

n = int(input())
k = int(input())
# 인덱스가 0부터 시작하고, 좌표가(1, 1) 부터 시작하기 때문에
data = [[0] * (n + 1) for _ in range(n + 1)]    # 맵 정보
info = []   # 방향 회전 정보

# 사과 있는 곳 정보 입력
for _ in range(k) : 
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l) : 
    x, c = input().split()
    info.append((int(x), c))

# 방향 정의 => dx와 북 부터! 
# 무조건, dx = 북남, dy = 서동 / 북과 서는 -1, 남과 동은 1 !!!
# 순서 : 북 동 남 서 (시계방향 순)
# 처음에 오른쪽을 보고 있으니 오른쪽으로 하나씩 옮겨서 나타내기 
# => 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 함수 생성 => python의 음수의 나머지 연산 규칙 이용!!
def turn(direction, c) : 
    if c == "L" : 
        direction = (direction - 1) % 4
    else : 
        direction = (direction + 1) % 4
    return direction

def simulate() : 
    x, y = 1, 1     # 뱀의 머리 현재 위치
    data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시
    direction = 0   # 처음에는 동쪽으로 보고 있고, 우리는 방향을 동쪽을 기준으로 설정해놨음
    time = 0    # 시작한 뒤에 지난 초 시간
    index = 0   # 다음에 회전할 정보
    q = [(x, y)]    # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽) => 머리는 큐 맨 뒤에 추가가 되고, 꼬리는 큐 맨 앞에서 제거

    while True : 
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2 : 
            # 사과가 없다면 이동 후에 꼬리 제거 => pop(0)
            if data[nx][ny] == 0 : 
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1 : 
                data[nx][ny] = 2
                q.append((nx, ny))

            x, y = nx, ny   # 이동은 항상 맨 나중에!
            time += 1
        
        # 벽이나 뱀의 몸통과 부딪혔다면
        else : 
            time += 1
            break
        
        # 회전할 시간인 경우 회전
        if index < l and time == info[index][0] : 
            direction = turn(direction, info[index][1])
            index += 1
    
    return time

print(simulate())
