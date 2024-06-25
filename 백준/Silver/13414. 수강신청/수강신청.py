'''
백준 13414 수강신청

수강신청 시스템
1. 수강신청 버튼 활성화 후, 버튼 누른 순으로 대기목록에 들어감
2. 대기열에서 다시 누르면 맨뒤로 밀려남
3. 버튼이 비활성 되면, 대기목록에서 가장 앞에 있는 학생부터 자동으로 수강신청완료되며, 가능인원이 꽉찰경우 대기목록 무시하고 종료

수강신청에 성공한 인원을 출력하는 프로그램을 작성

입력
과목의 수강 가능 인원 K
학생들이 버튼을 클릭한 순서 대기목록 길이 L
L개의 줄에 학생의 학번(8자리) 클릭순으로 주어짐

출력
수강신청 성공한 인원학번 한줄에 1개

수강신청이 들어온 순으로 학번과 순서를 key:value로 저장
순서를 기준으로 오름차순 정렬해 제한 인원 수 대로 출력
'''
import sys
input = sys.stdin.readline

# 인풋
K, L = map(int, input().split())

# 학번
arr = {}
for i in range(L):
    arr[input().strip()] = i

# 오름차순 정렬
ans = sorted(arr.items(), key = lambda x:x[1])

# 답 출력
for i in range(min(K, len(ans))):
    print(ans[i][0])