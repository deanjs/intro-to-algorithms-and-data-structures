# for 문으로 작성한 선형 검색 알고리즘

from typing import Sequence, Any

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

if __name__ == "__main__":
    num = int(input("원소 수를 입력하세요: "))        # num 값을 입력받음
    a = [None] * num                                # 원소수가 num인 배열을 생성   

    for i in range(num):
        a[i] = int(input(f"x[{i}]: "))
    
    ky = int(input("검색할 값을 입력하세요: "))        # 검색할 키 ky를 입력받음
    idx = seq_search(a, ky)                          # ky와 값이 같은 원소를 x에서 검색

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")