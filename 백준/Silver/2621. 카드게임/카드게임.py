'''
백준 2621 카드게임

카드는 빨강, 파랑, 노랑, 초록 네 가지 색
색별로 1~9 숫자가 쓰인 9장 카드 존재
36장의 카드에서 5장을 뽑고 점수 계산
1. 카드 5장이 모두 같은 색이며 숫자가 연속적일때, 가장 높은 숫자에 900을 더한다
2. 4장의 숫자가 같을 때 점수는 같은 숫자에 800을 더한다
3. 3장의 숫자가 같고 나머지 2장도 숫자가 같을때 3장이 같은 숫자에 10을 곱하고 2장이 같은 숫자를 더한 다음 700을 더한다
4. 5장의 카드 색이 모두 같을때 가장 높은 숫자에 600을 더한다
5. 숫자가 연속적일 때 가장 높은 숫자에 600을 더한다
6. 3장의 숫자가 같을 때 점수는 같은 숫자에 400을 더한다.
7. 2장의 숫자가 같고 또 다른 2장의 숫자가 같을 때 같은 숫자중 큰 숫자에 10을 곱하고 작은 숫자를 더한다음 300을 더한다.
8. 2장의 숫자가 같을 때 같은 숫자에 200을 더한다
9. 어느 경우도 해당되지 않으면 가장 큰 숫자에 100을 더한다

입력
한줄에 한장의 카드가 색과 숫자가 표시되어 5장 입력

출력
카드 점수 출력
'''
import sys
input = sys.stdin.readline

def f():
    # 1
    if 5 in color_count.values():
        count = 0
        max_num = 0

        for number, cnt in enumerate(number_count):
            if cnt > 0:
                count += 1
                max_num = max(max_num, number)
            else:
                count = 0
            if count == 5:
                break

        if count == 5:
            result = max_num + 900
            return result
        
    # 2
    elif 4 in number_count:
        number = number_count.index(4)
        result = 800 + number
        return result
    
    # 3
    elif 3 in number_count and 2 in number_count:
        number3 = number_count.index(3)
        number2 = number_count.index(2)
        result = number3 * 10 + number2 + 700
        return result

    # 4
    if 5 in color_count.values():
        max_num = 0
        for color, number in card:
            if max_num < number:
                max_num = number
        result = 600 + number
        return result

    # 5
    cnt = 0
    max_num = 0
    for number, count in enumerate(number_count):
        if count > 0:
            cnt += 1
            max_num = max(max_num, number)
        else:
            cnt = 0
        if cnt == 5:
            break
    if cnt == 5:
        result = 500 + max_num
        return result
    
    # 6
    if 3 in number_count:
        number = number_count.index(3)
        result = 400 + number
        return result

    # 7
    cnt = 0
    max_num = 0
    min_num = 9
    for number, count in enumerate(number_count):
        if count == 2:
            cnt += 1
            max_num = max(max_num, number)
            min_num = min(min_num, number)
        if cnt == 2:
            break
    if cnt == 2:
        result = 10 * max_num + min_num + 300
        return result
    
    # 8
    if 2 in number_count:
        number = number_count.index(2)
        result = 200 + number
        return result
    
    # 9
    max_num = 0
    for color, number in card:
        if max_num < number:
            max_num = number

    return 100 + max_num

# 카드 리스트
card = []
# 색 딕셔너리
color_count = {
    'R':0,
    'B':0,
    'Y':0,
    'G':0,
}
# 숫자 개수
number_count = [0] * 10

# 인풋
for _ in range(5):
    color, number = map(str, input().split())
    number = int(number)
    card.append((color, number))

    color_count[color] += 1
    number_count[number] += 1

# 숫자기준 정렬
card = sorted(card, key=lambda x: x[1])

ans = f()
print(ans)