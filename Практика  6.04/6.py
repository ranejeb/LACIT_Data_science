import math
centralnumber=int(input("Input a central number:"))
a={k:0 for k in range(-centralnumber+1,centralnumber) }
nn =centralnumber
n = 1
while nn/10>=1:
    nn = nn / 10
    n += 1
print(n)
for i in range(-centralnumber+1,centralnumber):
    if i<=0:
        k=i+centralnumber
    else:
        k=i-centralnumber
        k=int(math.fabs(k-1))
    for j in range(k):
        if i<=0:
            if j==0:
                a[j]+=1
            else:
                a[j]+=1
                a[-j]+=1
        else:
            if j==0:
                a[j]-=1
            else:
                a[j]-=1
                a[-j]-=1


    for x in range(-centralnumber+1,centralnumber):


        if a[x]==0:
            print(' '*n,end='')
        else:

            nn = a[x]
            nx = 1
            while nn/10>=1:
                nn = nn / 10
                nx += 1


            if nx!=n:
                print(str(a[x])+" "*(n-nx),end='')
            else:
                print(str(a[x]) , end='')
    print()