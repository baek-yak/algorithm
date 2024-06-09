'''
백준 2579 계단 오르기

계단 아래 시작점 부터 계단 꼭대기 도착점까지 가는 게임
각 계단을 밟으면 계단에 쓰인 점수를 얻는다
계단은 한 번에 하나 or 두개 씩 오를 수 있다
연속된 세 개는 밟으면 안된다(시작점은 계단에 포함 안함)
마지막 도착은 반드시 밟아야 한다.

입력
계단의 개수
계단의 점수

출력
총 점수의 최댓값

'''
# 계단 개수
n = int(input())
# 계단 점수
arr = [int(input()) for _ in range(n)]

dp = [0] * n

# 계단이 2개 이하
if len(arr) <= 2:
    print(sum(arr))

# 계단이 3개 이상
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    
    for i in range(2, n):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
    
    print(dp[-1])