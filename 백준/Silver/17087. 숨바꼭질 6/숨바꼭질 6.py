'''
백준 17087 숨바꼭질 6

동생 N명과 숨바꼭질하고 있다.
현재 S에 있고 동생은 a1, a2, ..., an에 있다
수빈이의 위치가 x일때 걷는다면 1초 후에 x+-d로 이동할 수 있다.
모든 동생을 찾기위해 d값을 정하려한다. d의 최댓값을 구하자

입력
N S
동생위치

출력
D의 최댓값

동생이 있는 곳ㅇ르 모두 방문하려면 D가 동생과의 거리의 약수여야함
모든 동생을 찾기 위한 공통 약수의 최댓값 찾기
'''
import math
# 인풋
N, S = map(int, input().split())
# 동생 위치
arr = list(map(int,input().split()))

# 각 동생사이 거리 d
d = []
for i in arr:
    d.append(abs(S-i))

ans = d[0]

# 모든 거리 d의 최대 공약수 계산
for i in range(1, N):
    ans = math.gcd(d[i], ans)
    
print(ans)