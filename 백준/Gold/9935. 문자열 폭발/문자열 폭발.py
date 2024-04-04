'''
9935 문자열 폭발

문자열이 폭발 문자열을 포함한 경우, 모든 폭발 문자열 폭발.
남은 문자열을 이어 붙여 문자열 생성
폭발 문자열이 없을 때 까지 계속 됨

입력 - 문자열, 폭발 문자열
출력 - 남은 문자열 출력, 남은게 없는 경우 FRULA 출력
'''

# 문자열, 폭발 문자열.
letter = input()
boom = input()

# 문자 담을 스택
stack = []  

# 문자열 순회
for char in letter:
    # 스택에 문자 추가
    stack.append(char)
    
    # 스택의 끝이 폭발 문자열과 같음 제거
    if char == stack[-1] and ''.join(stack[-len(boom):]) == boom:
        # 스택에서 폭발 문자열 제거
        del stack[-len(boom):]

# 남은 문자 합치기
ans = ''.join(stack)  

# 답 없을 경우 FRULA 출력, 답 출력
if len(ans) == 0:
    print('FRULA')  
else:
    print(ans)