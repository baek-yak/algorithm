function solution(N, stages) {
    // 결과를 저장할 배열
    let ans = []; 
    // 스테이지 수만큼 반복
    for (let i = 1; i <= N; i++) { 
        // 스테이지에 도달한 플레이어 수
        let end = stages.filter((x) => x >= i).length;

        // 스테이지에 머무르고 있는 플레이어 수
        let fail = stages.filter((x) => x === i).length;

        // 현재 스테이지, 실패율 배열에 저장
        ans.push([i, fail / end]);
    }

    // 실패율 기준으로 배열 내림차순
    ans.sort((a, b) => b[1] - a[1]);

    // 스테이지 반환
    return ans.map((x) => x[0]);
}
