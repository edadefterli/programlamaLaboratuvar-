liste_1=[4,-3,5,-2,-1,2,6,-2]
max_1=0
for i in range(8):
    for j in range(i,8):
        t=0
        for k in range(i,j):
            t+=liste_1[k]
        if max_1<t:
            max_1=t
            i_1,i_2=i,j
print(max_1,i_1,i_2)