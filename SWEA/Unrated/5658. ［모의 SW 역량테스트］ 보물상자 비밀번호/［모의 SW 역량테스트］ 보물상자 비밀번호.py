T = int(input())

for case in range(1, T+1):
    N, K = map(int, input().split())
    data = input()
    num = []
    
    for i in range(N//4):
        for j in range(0, N, N//4):
            num.append(data[j:j+(N // 4)])
        
        data = data[-1] + data[:-1]
    
    num = list(set(num))
    num.sort(reverse=True)
    
    ans = num[(K-1)]
    
    print(f'#{case} {int(ans,16)}')