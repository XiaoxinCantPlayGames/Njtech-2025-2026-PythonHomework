#国家与首都的对应关系如以下字典：
#d={"China":"Beijing","America":"Washington","Norway":"Oslo","Japan":"Tokyo","Germany":"Berlin","Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
#输入输出样例如下：
#输入：
#china
#输出：
#Beijing
#输入:
#ITALY
#输出：
#未查询到该国家名
#【提示】输入的国家名需要规格化处理



d={"China":"Beijing","America":"Washington","Norway":"Oslo","Japan":"Tokyo","Germany":"Berlin","Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
x=input()
y=x.capitalize()
if y not in d:
    print('未查询到该国家名')
else:
    print(d[y])
