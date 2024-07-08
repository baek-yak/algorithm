from sys import stdin

# 빈 큐
q = []  

# 명령 수
N = int(stdin.readline())  

for n in range(N):
    # 인풋
    input = stdin.readline().split()  

    # 큐의 뒤에 정수 추가
    if input[0] == "push":
        q.append(int(input[1]))  
    
    elif input[0] == "pop":
        # 큐가 비어있으면 -1
        if len(q) == 0:
            print(-1)  
        # 큐의 앞에서 정수를 제거
        else:
            print(q.pop(0))  
    
    # 큐의 크기
    elif input[0] == "size":
        print(len(q))  
    
    elif input[0] == "empty":
        # 큐가 비어있으면 1
        if len(q) == 0:
            print(1)  
        # 큐가 비어있지 않으면 0
        else:
            print(0)  
    
    elif input[0] == "front":
        # 큐의 가장 앞에 있는 정수
        if len(q) != 0:
            print(q[0])  
        # 큐가 비어있으면 -1
        else:
            print(-1)  
    
    elif input[0] == "back":
        # 큐의 가장 뒤에 있는 정수
        if len(q) != 0:
            print(q[-1])  
        # 큐가 비어있으면 -1
        else:
            print(-1)  