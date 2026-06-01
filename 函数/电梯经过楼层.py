x=eval(input())
for i in range(1,5+1):
    if x[i]>x[i-1]:
        print('↑'*(x[i]-x[i-1]),end='')
    else:
        print('↓'*(x[i-1]-x[i]),end='')
