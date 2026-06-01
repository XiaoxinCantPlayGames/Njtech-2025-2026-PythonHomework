d=eval(input())
ls=[(k,v) for k,v in d.items()]
cnt1=cnt2=s=0
for i in ls:
    if i[1][0]=='男':
        cnt1+=1
    elif i[1][0]=='女':
        cnt2+=1
    s+=i[1][1]
print(cnt1)
print(cnt2)
print(round(s/len(ls),1))
