'''
백준 1107 리모컨

0~9 + - 버튼 일부 숫자 버튼이 고장남 
N으로 이동하기 위해 몇 번을 눌러야 하는지

입력
이동 하려는 채녈 N
고장난 버튼 개수 M 
고장난 버튼

출력 
몇 번 눌러야하는지

완전 탐색으로 풀이
'''
n = int(input())
m = int(input())
# 고장난 버튼이 없는 경우 존재
if m != 0:
    b = list(input().split())
else:
    b = []

# ++ 또는 --로 이동할 경우
ans = abs(100 - n)

for i in range(1000000 + 1):
    for j in str(i):
        
        # 숫자 버튼이 고장난 경우
        if j in b: 
            break
        
    else:
        # 번호를 누른 횟수와 해당 번호 부터 n 까지의 차이 최솟값 출력
        ans = min(ans, len(str(i)) + abs(i - n)) 

print(ans)