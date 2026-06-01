s='From hill to hill no bird in flight;From path to path no man in sight.A lonely fisherman afloat,Is fishing snow in lonely boat.'
s=s.lower()
t=s.replace( ',',' ').replace('.',' ').replace(';',' ')
lt=t.split()
d={}
for i in lt:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
lt2=[(k,v) for k,v in d.items()]
m=sorted(lt2,key=lambda x:x[1],reverse=True)
print(m[:5])

