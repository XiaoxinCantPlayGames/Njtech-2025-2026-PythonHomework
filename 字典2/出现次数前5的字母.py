s='If you really want to hear about it,the first thing you will probably want to know is where I was born and what my lousy childhood was like,and how my parents were occupied and all before they had me,and all that David Copperfield kind of crap,but I do not feel like going into it,if you know the truth about.'
s=s.lower()
ls=[i for i in s if i.islower()]
d={}
for j in ls:
    if j in d:
        d[j]+=1
    else:
        d[j]=1
lt=[(k,v) for k,v in d.items()]
t=sorted(lt,key=lambda x:x[1],reverse=True)
k=t[:5]
for r in k:
    print(r[0])
print(t[:5])
