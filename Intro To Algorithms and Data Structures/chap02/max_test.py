def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)): 
        # i 값은 1부터 시작하여
        # 4까지 증가한다. (len(a) == 5 이기 때문이다.)
        if a[i] > maximum:
            maximum = a[i]
    return maximum

print(max_of([22,57,11,91,32]))