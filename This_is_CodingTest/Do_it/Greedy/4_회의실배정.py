from sys import stdin
input = stdin.readline

# 아이디어 : 회의의 종료 시간이 빠를수록 회의가 많이 나올 수 있으므로, 회의 종료 시간이 빠른 순서대로 정렬한 다음,
# 겹치지 않는 회의실을 적절히 선택
n = int(input())
a = [[0] * 2 for _ in range(n)]     # 정렬하려면 리스트로 만들어야 함, 2차원 배열 생성 및 초기화 / 이때 n이 행의 수!

# 2차원 배열 입력값 입력방법 익히기!
for i in range(n) : 
    s, e = map(int, input().split())
    a[i][0] = e     # 종료시간 우선 정렬이 우선이기 때문에 0번째에 종료시간을 먼저 저장
    a[i][1] = s

# 이렇게 되면 한번에 정렬되며, 앞에서 종료시간 우선정렬 시켰기 때문에 문제 없음!
a.sort()

count = 0
end = -1    # 시작하는 시간과 끝나는 시간이 0일 수도 있으므로 (문제에 있음)

for i in range(n) : 
    if a[i][1] >= end :     # 겹치지 않은 다음 회의가 있는 경우
        end = a[i][0]   # 종료시간 업데이트
        count += 1

print(count)
