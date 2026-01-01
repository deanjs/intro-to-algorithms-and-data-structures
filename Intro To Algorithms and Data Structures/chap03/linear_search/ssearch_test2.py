# seq_search() 함수를 사용하여 특정 인덱스 검색하기

from ssearch_for import seq_search

t = (1, 2, 3, 4, 1.1, 2.2, 3.3)
s = "string"
a = ["DTS", "AAC", "FLAC"]

print(f"{t}에서 1.1의 인덱스는 {seq_search(t, 1.1)}입니다.")
print(f"{s}에서 r의 인덱스는 {seq_search(s, "r")}입니다.")
print(f"{a}에서 'DTS' 의 인덱스는 {seq_search(a, "DTS")}입니다.")