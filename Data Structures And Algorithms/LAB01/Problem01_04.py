# 세 정수 중앙값 구하기

def med3(a,b,c):
    if (b>=a and c<=a) or (b<=a and c>=a):
        return a
    elif (a>b and c<b) or (a<b and c>b):
        return b
    else:
        return c
    
a,b,c = 1,2,3
print(f"중앙값은 {med3(a,b,c)} 입니다.")