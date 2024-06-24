'''
백준 2023 신기한 소수

예를 들어 4자리 숫자중 앞의 세 숫자, 두 숫자, 한 숫자 모두 소수인 수를 신기한 소수라 한다
N이 주어질 때, N자리의 소수를 모두 찾아보자

입력
N

출력
소수를 오름차순으로 정렬해 한줄에 하나씩 출력

DFS 활용 문제 풀이
'''
import math
# 인풋
N = int(input())

# 소수 판별
def prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if int(x) % i == 0:
            return False
    return True

# dfs로 소수 찾기
def dfs(num):
    # 숫자의 자리수가 N이면 숫자 출력
    if len(str(num)) == N:
        print(num)
    else:
        # 한 자리 수 중 홀수만
        for i in range(1, 10, 2):
            # 다음 숫자 만들기 숫자뒤에 i 추가
            arr = num*10 + i
            # 만든 숫자가 소수인지 확인
            if prime(arr):
                # 소수라면 탐색
                dfs(arr)
                
dfs(2)
dfs(3)
dfs(5)
dfs(7)