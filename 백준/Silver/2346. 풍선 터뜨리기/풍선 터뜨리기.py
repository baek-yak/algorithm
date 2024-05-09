'''
백준 2346 풍선 터트리기

1~N N개의 풍선
원형으로 풍선이 오른쪽으로 증가하며 놓여있음
풍선 안에는 종이가 있고 종이에 -n~n사이의 정수가 적혀있음

1번 풍선 터트림
종이 값 만큼 이동해 풍선 터트림 양수 오른쪽 음수 왼쪽이동

터진 풍선의 번호를 차례로 출력
'''
from collections import deque

N = int(input())
ballon = deque(enumerate(map(int, input().split())))

for i in range(N):
    ans, paper = ballon.popleft()
    print(ans+1, end=' ')

    if paper > 0:
        ballon.rotate(-(paper - 1))
    else:
        ballon.rotate(-paper)