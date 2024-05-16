'''
백준 1645 랜선 자르기

N개의 랜선을 만들어야하는데 K개의 랜선의 길이는 제각각 잘라서 만들어야한다.

입력
랜선의 개수 k, 필요 랜선의 개수 n
k줄에 걸쳐 각 랜선의 길이

출력
N개를 만들 수 있는 랜선의 최대 길이

이진 탐색으로 풀면 될듯하다.
'''
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]

# 이진탐색 처음 끝
start = 1 
end = max(lan) 

# 이진탐색 실행
while start <= end: 
    # 중간 위치
    mid = (start + end) // 2 
    
    # 랜선 수
    lines = 0 
    
    for i in lan:
        # 분할 된 랜선 수
        lines += i // mid 
        
    # 랜선 개수가 분기점
    if lines >= N: 
        start = mid + 1
    else:
        end = mid - 1
print(end)