n=eval(input())
for i in range(10**(n-1),10**n):
    m=str(i)
    s=0
    for j in m:
        s+=int(j)**n
    if s==i:
        print(i)
        
