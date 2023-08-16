from queue import PriorityQueue
from sys import stdin
input = stdin.readline


# 아이디어 : 카드의 수가 적은 묶음 순대로 먼저 합치는 것이 전체 비교 횟수를 줄여 최소 값이 나올 수 있다.
# 우선순위 큐를 이용!(데이터의 삽입, 삭제, 정렬이 자주 일어남으로)
# 책이랑은 다르게 data1, data2 = 0 코드를 뺐다. (빼도 돌아간다.)
n = int(input())

# 우선순위 큐는 내부에서 자동 정렬되기 때문에 자동으로 오름차순으로 정렬되며, get으로 반환할 때 최소값이 먼저 반환이 된다.
# 따라서 우선순위 큐는 최소값부터 차례대로 꺼낼 수 있는 특성을 가진다.
# heapq는 비슷하지만 리스트가 있거나 구성해야함! (상대적으로 난 priorityqueue가 더 편하고 좋은 듯)
pq = PriorityQueue()
for i in range(n) : 
    data = int(input())
    pq.put(data)

answer = 0

while pq.qsize() > 1 : 
    data1 = pq.get()
    data2 = pq.get()
    sum = data1 + data2
    answer += sum
    pq.put(sum)

print(answer)
