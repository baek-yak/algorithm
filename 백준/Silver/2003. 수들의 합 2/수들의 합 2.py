'''
백준 2003 수들의 합2

N개의 수로 된 수열이 있다.
수열의 i 번째 수부터 j 번째 수까지의 합이 M이 되는 경우의 수를 구하라

입력
N과 M
수열

출력
경우의 수

슬라이싱으로 구간을 설정하고 구간 부분합을구해 답을 구한다.
'''
# 수열, 합 입력
N, M = map(int, input().split())
# 수열 
arr = list(map(int, input().split()))

# l,r 초기 배열 인덱스 설정
l = 0
r = 1
ans = 0

while r <= N and l <= r:
    # 현재 부분수열 합 계산
    sum_n = arr[l:r]
    sum_s = sum(sum_n)
    
    # 부분 수열 합이 M일 때 답 증가, 오른쪽 배열 이동
    if sum_s == M:
        ans += 1
        r += 1
    # 부분 수열 합이 작을 때, 오른쪽 배열 이동
    elif sum_s < M:
        r += 1
    # 부분 수열 합이 클 때, 왼쪽 배열 이동
    else :
        l += 1

print(ans)