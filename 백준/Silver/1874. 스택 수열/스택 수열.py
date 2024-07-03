'''
백준 1874 스택 수열

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다
스택에 push하는 순서는 반드시 오름차순
열이 주어졌을 때 스택을 이용해 그 수열을 만들기 가능
가능하다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있는 프로그램을 작성

입력
N
N개의 줄에 수열을 이루는 1이상 N이하의 정수

출력
수열을 만들기 위해 필요한 연산을 한 줄에 하나 출력
push = +, pop = -로 표현
불가능한 경우 NO

스택에 push하는 순서는 반드시 오름차순

'''
# 인풋
N = int(input())
stack = []
ans = []
find = True

# 숫자 1부터 시작
num = 1

for _ in range(N):
    arr = int(input())
    
    # push
    while num <= arr:
        stack.append(num)
        ans.append('+')
        num += 1
    # pop
    if stack[-1] == arr:
        stack.pop()
        ans.append('-')
    # 불가능
    else :
        find = False

if not find :
    print('NO')
else:
    for i in ans:
        print(i)