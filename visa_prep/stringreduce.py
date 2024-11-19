air=input().strip()
beet_str = ""
count=1
for i in range(1, len(air)):
    if air[i]==air[i-1]:
        count+=1
    else:
        beet_str += air[i-1]+str(count)
        count=1
beet_str += air[-1]+str(count)
print(beet_str)
