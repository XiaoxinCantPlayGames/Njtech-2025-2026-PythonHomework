d=eval(input())
ls=[(k,v) for k,v in d.items()]
a=sorted(ls,key=lambda x:x[1],reverse=True)
for i in a:
    print(i[0])

