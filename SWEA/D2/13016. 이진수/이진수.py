t = int(input())
for case in range(1, t+1):
    N, HEXX = input().split()
    
    h = int(HEXX, 16)
    
    b = bin(h)
    ans = b[2:]
    
    N = int(N)
    
    if len(ans) == 4*N:
        print(f'#{case} {ans}')
    else:
        print(f'#{case} {"0"*( (4*N)-len(ans) ) + ans}')