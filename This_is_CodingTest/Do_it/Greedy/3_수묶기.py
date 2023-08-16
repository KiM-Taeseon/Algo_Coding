from queue import PriorityQueue
from sys import stdin
input = stdin.readline

# 아이디어 : 가장 큰 수 끼리 묶어야 결과값이 커지고 음수끼리 곱하면 양수로 변한다. 조건을 네 가지의 분기로 나눠서 계산한다.
# while문이 이해가 안감...(3개일 때는 이해가 가 근데 이게 4개나 5개 되면 while문 성립이 안되는 걸로 알고 있는데 이게 왜 맞을까?)
n = int(input())

plus_pq = PriorityQueue()
minus_pq = PriorityQueue()
one = 0
zero = 0

# 큐는 오른쪽으로 들어가서 왼쪽으로 나간다.(우선순위 큐 => 오름차순 정렬)
for i in range(n) : 
    data = int(input())
    # 데이터를 4개의 그룹으로 분리
    if data > 1 : 
        plus_pq.put(data * -1)  # 반대로 하기 위해서 음수로 만들어서 내림차순 정렬처럼 만든다.
    elif data == 1 :
        one += 1
    elif data == 0 : 
        zero += 1
    else : 
        minus_pq.put(data)

sum = 0

# 양수 처리
while plus_pq.qsize() > 1 :
    first = plus_pq.get() * -1  # 꺼내고 나서는 양수이므로 -1을 다시 곱해줘서 원래 숫자로 만든다.
    second = plus_pq.get() * -1
    sum += first * second
if plus_pq.qsize() > 0 : 
    sum += plus_pq.get() * -1

# 음수 처리
while minus_pq.qsize() > 1 : 
    first = minus_pq.get()
    second = minus_pq.get()
    sum += first * second
if minus_pq.qsize() > 0 : 
    if zero == 0 : 
        sum += minus_pq.get()

# 1 처리
sum += one

print(sum)
