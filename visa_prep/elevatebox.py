n=int(input())
arr=list(map(int, input().split()))
tot=sum(arr)
weig=0
bal=[]
for i in range(n):
    right_weight=tot-weig-arr[i]
    bal.append(abs(weig-right_weight))
    weig += arr[i]
print(*bal)
