# 구구단 곱셈표 출력하기

print("-" * 27)
for i in range(1,10):        # 행 
    for j in range(1,10):    # 열
        print(f"{i*j:2}", end= " ")
    print()
print("-" * 27)