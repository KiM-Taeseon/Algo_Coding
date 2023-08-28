# 아이디어 : 길이가 n인 문자열이 입력되었다면 1부터 n/2까지의 모든 수를 단위로 하여 탐색하여 가장 짧은 길이를 출력한다.
# 주의할 점 : s[] 값은 인덱스 값이다! / prev를 잘 따라가자!
# 알게된 점 : compressed += str(count) + prev if count >= 2 else prev 는
#     (=)    if count >= 2 : 
#                compressed += str(count) + prev
#            else : 
#                compressed += prev
#           로 뜻하고 표기할 수 있다.

def solution(s) : 
    answer = len(s)

    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1) : 
        compressed = ""
        prev = s[0 : step]  # 앞에서부터 step만큼의 문자열 추출(인덱스이므로)
        count = 1

        # step 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step) : 
            # 이전 상태와 동일하다면 count 증가
            if prev == s[j : j + step] : 
                count += 1
            # 다른 문자열이 나왔다면
            else : 
                if count >= 2 : 
                    compressed += str(count) + prev
                else : 
                    compressed += prev
                # 다시 prev 초기화
                prev = s[j : j + step]
                count = 1

        # 남아 있는 문자열(step 반복문)에 대해서 똑같이 처리
        if count >= 2 : 
            compressed += str(count) + prev
        else : 
            compressed += prev
        
        # 압축문의 길이와 원래 문자열의 길이 중 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer