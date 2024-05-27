'''
백준 1715 카드 정렬하기 

정렬된 두 묶음 숫자 카드가 존재
a,b 를 비교하려면 a+b번 비교를 해야함

입력
숫자 카드 묶음의 각각의 크기가 N 줄

출력
최소 비교 횟수 출력

가장 작은 묶음을 두 개 찾아서 더하는게 가장 적게 비교하는 방법
'''
import heapq

n = int(input())
arr = []

for i in range(n):
    heapq.heappush(arr, int(input()))

ans = 0

while len(arr) > 1:
    # 가장 작은 두 카드 묶음 합
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    card_sum = a + b

    # 합한 값 누적 & 결과 큐 삽입
    ans += card_sum
    heapq.heappush(arr, card_sum)

print(ans)