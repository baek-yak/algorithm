'''
2382 미생물 격리

N *N 구역에 k개 미생물 존재
1. 각 미생물, 위치, 개수, 방향이 주어짐
2. 미생물은 1시간마다 이동
3. 경계에 도착 시 절반 감소, 이동방향 반대
4. 두 개 이상 모이면 합쳐짐 방향은 큰 값으로 감

M 시간 이동 후 남아있는 미생물 총합 구하기

'''
# 이동방향
di = [0, -1, 1, 0, 0] 
dj = [0, 0, 0, -1, 1]

# 반대방향 표시 
rd = [0, 2, 1, 4, 3]
 
T = int(input())

for case in range(1, T + 1):
    # N : 배열, M : 격리시간, k : 미생물 수
    N, M, K = map(int, input().split())
    # 미생물 정보(세로, 가로, 수, 이동방향)
    # 0 : i, 1 : j, 2 : n, 3 : dr
    arr = [list(map(int, input().split())) for _ in range(K)]
 
    for _ in range(M):
        # 1칸 이동, 경계면 // 2, 방향반대
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] //= 2
                arr[i][3] = rd[arr[i][3]]
 
        # 내림차순 정렬
        arr.sort(key=lambda x: (x[0],x[1],x[2]), reverse=True)
 
        # 같은 좌표 합치기
        i = 1
        
        while i < len(arr):
            if arr[i-1][0:2] == arr[i][0:2]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)

            else:
                i += 1
 
    ans=0
    
    for i in arr:
        ans += i[2]
 
    print(f'#{case} {ans}')