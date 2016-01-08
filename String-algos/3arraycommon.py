a = map(int,raw_input().split())
b = map(int,raw_input().split())
c = map(int,raw_input().split())

last1 = len(a)-1
last2 = len(b)-1
last3 = len(c)-1

while last1 >=0 and last2>=0 and last3>=0:
    if a[last1]<b[last2] and a[last1]<c[last3]:
        last2 -= 1
        last3 -= 1
    elif b[last2]<a[last1] and b[last2]<c[last3]:
        last1 -= 1
        last3 -= 1
    elif c[last3]<b[last2] and c[last3]<a[last1]:
        last2 -= 1
        last1 -= 1

    elif a[last1]<b[last2]:
        last2 -= 1

    elif b[last2]<c[last3]:
        last3 -= 1

    elif c[last3]<a[last1]:
        last1 -= 1
    elif a[last1]==b[last2]==c[last3]:
        print c[last3],
        last1 -= 1
        last2 -= 1
        last3 -= 1



