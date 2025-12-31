# 세 정수의 중앙값 찾기

def med3(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a<=c :
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b 

a,b,c = 1,2,3
print(f"중앙값은 {med3(a,b,c)} 입니다.")