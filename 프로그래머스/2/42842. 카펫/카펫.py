'''
프로그래머스 carpet

갈색 격자수, 노란색 격자수가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 반환
'''
def solution(brown, yellow):
    # 결과 저장 리스트
    ans = []  
    
    # 가로(x) 세로(y) 초기화
    x, y = 0, 0  
    
    # yellow 격자를 기준으로 가로와 세로를 모두 확인
    for i in range(1, yellow+1):
        # i가 yellow의 약수인지 확인
        if yellow % i == 0:  
            # 가로
            x = int(yellow / i)  
            # 세로
            y = i  
            
            # 가로*2 + 세로*2 + 4가 brown과 같은지 확인
            if x * 2 + y * 2 + 4 == brown:
                # 주어진 brown 격자의 모서리에는 yellow 격자가 포함되지 않음. 
                # 그러므로 brown 격자에는 yellow 격자에 대한 추가적인 길이가 더해져야 함.
                # brown 격자에는 yellow 격자 길이가 포함되어 있어야 하므로, 이를 고려하여 2를 더해줍니다.
                ans.append(x+2)  
                ans.append(y+2)  

                # 결과를 내림차순으로 정렬
                return sorted(ans, reverse=True)  
    
    # 결과 반환
    return ans  
