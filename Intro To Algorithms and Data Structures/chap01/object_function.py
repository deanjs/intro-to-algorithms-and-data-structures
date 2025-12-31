# 함수 내부, 외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n = 1
def put_id():
    x = 1
    print(f"id(x) = {id(x)}")

print(f"id(n) = {id(n)}")
print(f"id(1) = {id(1)}")
put_id()

# 1부터 100까지 반복 출력

for i in range(1, 100 + 1):
    print(f"i = {i:3} id({i}) = {id(i)}")