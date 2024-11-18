x=int(input())
dis_10=x-(0.1*x)
dis_100=x-100
tot = min(dis_10,dis_100)
print(int(tot))
