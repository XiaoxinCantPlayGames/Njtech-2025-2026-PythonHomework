#【单词次数统计】

#输入一段英文（不区分大小写），对这段英文中每个单词出现的次数进行统计，输出出现次数排名前五的单词和次数。

#输入输出样例如下：

#输入示例1 (可以复制)：

#From hill to hill no bird in flight;From path to path no man in sight.A lonely fisherman afloat,Is fishing snow in lonely boat.

#输出：

#[('in', 3), ('from', 2), ('hill', 2), ('to', 2), ('no', 2)]

#代码提交后, 会测试不同输入字符串的统计结果.

#排序使用reverse关键字，需要替换的标点有,.;










x=input()
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
