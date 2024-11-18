Vignesh,Charan = input().split()
if Charan == Vignesh:
    print('NULL')
elif (Vignesh == 'R' and Charan == 'S') or (Vignesh == 'S' and Charan == 'P') or (Vignesh == 'P' and Charan == 'R'):
    print('Vignesh')
else:
    print('Charan')
