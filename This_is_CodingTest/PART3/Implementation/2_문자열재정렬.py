from sys import stdin
input = stdin.readline

# 아이디어 : 문자와 숫자를 나눈 다음, 각각 따로 계산하여 문자의 경우 리스트에 저장하고, 정렬한 뒤에 합계가 있다면 그 뒤에 붙여 합쳐서 출력
# 알게된 점 : isalpha() 함수, append, .join()

data = input().strip()
result = []     # 리스트 생성 => 정렬하기 위해서
sum = 0

# 알파벳 따로 숫자 따로 저장
# 배열에 '문자'를 추가 할 때는 append 사용!
for i in data : 
    if i.isalpha() :    # 알파벳인지 확인하는 boolean함수 : isalpha()
        result.append(i)
    else : 
        sum += int(i)

result.sort()

# 숫자가 존재한다면 가장 뒤에 삽입
if sum != 0 : 
    result.append(str(sum))

print(''.join(result))  # 추가된 문자들을 하나의 문자열로 합칠때는 .join() 함수 사용! => 리스트를 문자열로 변환
