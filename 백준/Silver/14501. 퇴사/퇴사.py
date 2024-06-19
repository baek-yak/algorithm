'''
백준 14501 퇴사

퇴사하려한다
N+1일째 되는 날 퇴사 하기 위해 N일 동안 최대한 많은 상담 하려 한다.
각각의 상담은 완료기간 T와 금액 P로 이루어져있다

입력
N
N개 줄에 T와 P가 1일부터 N일까지 순서대로

출력
최대 이익

백트래킹
'''
def dfs(n, sm):
    global ans
    # 종료조건
    if n>=N:
        ans = max(ans, sm)
        return

    # 상담하는 경우
    if n+T[n]<=N:   
        dfs(n+T[n], sm+P[n])
    # 상담 하지 않는 경우
    dfs(n+1, sm)   

N = int(input())
T = [0]*N
P = [0]*N

for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)

print(ans)