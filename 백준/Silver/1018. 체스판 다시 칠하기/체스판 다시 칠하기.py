n, m = map(int, input().split())

arr = list(input() for _ in range(n))
cnt = []

for i in range(n-7):
    for j in range(m-7):
        
        w = 0
        b = 0
        
        for k in range(i, i+8):
            for l in range(j, j+8):
                
                # 짝수 인 경우
                if (k+l) % 2 == 0:
                    if arr[k][l] != 'W':
                        w += 1
                    else:
                        b += 1
                
                # 홀수 인 경우
                else:
                    if arr[k][l] != 'W':
                        b += 1
                    else:
                        w += 1
        
        cnt.append(w)
        cnt.append(b)
        
print(min(cnt))