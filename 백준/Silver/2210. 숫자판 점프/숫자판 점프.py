'''
백준 2210 숫자판 점프

5 x 5 크기 숫자판
각 칸에는 숫자(digit, 0~9)적혀있다.
임의의 위치에서 시작해, 인접해 있는 네 방향으로 다섯 번 이동하며, 각 칸에 적힌 숫자를 차례로 붙이면 6자리 수가 된다.
이동 할 때는 동일 칸을 다시 거쳐도 되며, 0으로 시작하는 수를 만들 수 있따.
서로 다른 여섯자리의 수들의 개수를 구하는 프로그램을 만들어라

입력
5 x 5의 칸에 정수로 된 숫자판

출력
만들 수 있는 수의 개수 출력

모든 출발점에서 DFS를 실행
숫자열의 길이가 6이되면 set에 저장
set의 개수를 출력
'''
def dfs(i, j, num):
    # 현재 위치 숫자를 문자로 추가
    num += str(arr[i][j])
    
    # 숫자열의 길이가 6이 되면 set에 추가하고 종료
    if len(num) == 6:
        ans.add(num)
        return
    
    # 4 방향 탐색
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        # 숫자판 내에 존재
        if 0<= ni < 5 and 0<= nj < 5:
            dfs(ni, nj, num)

# 숫자판 입력
arr = [list(map(int, input().split())) for _ in range(5)]
ans = set()

# 4 방향
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 모든 출발점에서 dfs
for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(ans))