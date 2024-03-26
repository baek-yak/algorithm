arr = input()
ans = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] == '(':
        cnt += 1
    else:
        cnt -= 1
        if arr[i-1] == '(':
            ans +=cnt
        else:
            ans += 1
print(ans)