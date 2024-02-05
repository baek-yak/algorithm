T = int(input())
for case in range(1, T + 1):
    char = input()
    result = ''
 
    for i in range(len(char) - 1, -1, -1):
        if char[i] == 'b':
            result += 'd'
        elif char[i] == 'd':
            result += 'b'
        elif char[i] == 'p':
            result += 'q'
        elif char[i] == 'q':
            result += 'p'
 
    print(f'#{case} {result}')