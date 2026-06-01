readings=[23.5, 24.1, 22.8, 25.0, 23.9]
ls=[23.5]
for i in range(1,3+1):
    a=(readings[i-1]+readings[i]+readings[i+1])/3
    a=round(a,1)
    ls.append(a)
ls.append(23.9)
print(ls)
