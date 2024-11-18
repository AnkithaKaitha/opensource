a,b,c,x = map(int,input().split())
if x<=a+b:
    print('YES')
elif x<=b+c:
    print('YES')
elif x<=a+c:
    print('YES')
else:
    print('NO')
