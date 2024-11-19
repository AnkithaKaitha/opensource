T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    if m<n:
        a=n-m
        print(a)
    else:
        print(0)
