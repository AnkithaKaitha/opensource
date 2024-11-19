e = int(input())
for _ in range(e):
    a,b = map(int, input().split())
    score = (a//10)*b
    print(score)
