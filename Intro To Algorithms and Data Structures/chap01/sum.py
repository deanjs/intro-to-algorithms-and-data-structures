# a 부터 b 까지 정수의 합 구하기 (for 문)

a, b = tuple(input("a, b 값을 입력하세요(띄워쓰기로 판단)").split(" "))
a = int(a)
b = int(b)
# a, b = map(int, input().split())

if a> b:
    a,b = b,a

sum = 0
for i in range(a, b+1):
    sum +=i
print(f"{a}부터 {b}까지 정수의 합은 {sum}입니다.")