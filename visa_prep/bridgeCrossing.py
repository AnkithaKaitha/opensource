def max_mango(x,y,z):
    capacity = z-y
    max_mango = capacity//x
    return max_mango
x,y,z = map(int,input().split())
print(max_mango(x,y,z))
