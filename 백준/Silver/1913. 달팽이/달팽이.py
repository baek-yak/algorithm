'''
백준 1913 달팽이

N이 주어졌을 때, 달팽이를 출력
또한 N^2 의 좌표도 같이 출력

입력
첫째 줄에 홀수인 자연수 N
위치를 찾고자 하는 N^2 

출력
표
좌표

가운데 부터 채워나감 패턴동일
'''
# 자연수 N, 찾고자 하는 숫자
n = int(input())
num = int(input())

# 방향 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 2차원
arr = [[0] * n for _ in range(n)]

# 배열 중앙 좌표
x = n // 2
y = n // 2

# 배열 중앙 1
arr[x][y] = 1

# 시작 숫자 2
number = 2

# 초기 반복 거리와 방향 인덱스
repeat = 1
i = 0

# 배열의 중앙부터 시작
ans = [x + 1, y + 1]

# 중앙 시작 달팽이
while number <= n * n:
    # 각 반복에서 두 번 같은 길이만큼 이동
    for _ in range(2):  
        for _ in range(repeat):
            if number > n * n:
                break
            x += dx[i]
            y += dy[i]
            # 현재 좌표에 숫자 입력
            arr[x][y] = number  
            # 찾고자 하는 숫자
            if number == num:  
                # 저장
                ans = [x + 1, y + 1]  
            # 숫자 증가
            number += 1  
        # 방향 전환
        i = (i + 1) % 4  
    # 이동 거리 증가
    repeat += 1  


for row in arr:
    print(*row)

print(*ans)
