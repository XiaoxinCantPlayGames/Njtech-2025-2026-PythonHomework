s=input()
s=s.lower()
lst=[]
for i in s:
    if i not in lst and i.isalpha():
        lst.append(i)
lst.sort()
print(lst)
