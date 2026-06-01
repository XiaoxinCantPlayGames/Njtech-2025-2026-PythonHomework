'''x=eval(input())'''
x='From hill to hill no bird in flight;From path to path no man in sight.A lonely fisherman afloat,Is fishing snow in lonely boat.'
x=x.lower()
s=x.replace(',',' ').replace(';',' ').replace('.',' ')
t=s.split()
d={}
for i in t:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ls=[(k,v) for k,v in d.items()]
a=sorted(ls,key=lambda x:x[1],reverse=True)
b=a[:5]
print(b)
