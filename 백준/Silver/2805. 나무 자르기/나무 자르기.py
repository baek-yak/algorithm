'''
백준 2805 나무 자르기

절단기에 높이 h 지정
톱날이 h 위로 올라간 후 나무를 절단 높이가 h보다 큰 나무는 h 위의 부분이 잘림
잘린 만큼을 들고감
적어도 m의 나무를 갖고가기 위해 설정할 높이의 최댓값

입력
나무의 수 n, 나무의 길이 m
나무의 높이(n개)

출력
적어도 m의 나무를 갖고가기 위해 설정할 높이의 최댓값

아이디어 
1. 처음에 높이를 찾는 방식으로 풀었는데 시간초과가 났다
2. 이분탐색으로 풀이
'''
n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    result = 0
    
    for t in tree:
        if t >= mid:
            result += t - mid
            
    if result >= m:
        start = mid + 1
    else :
        end = mid - 1

print(end)