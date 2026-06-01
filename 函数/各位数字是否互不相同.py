#编写一个函数isdiff(n),用来判断参数n的各位数字是否互不相同,若不同,则返回1,否则返回0。并在主程序中测试该函数。

#输入输出样例

#输入

#4052169

#输出

#1

#输入

#4059169

#输出

#0









def isdiff(x):
    y=str(x)
    for i in y:
        if y.count(i)!=1:
            return False
    else:
        return True
m=eval(input())
if isdiff(m)==True:
    print(1)
else:
    print(0)
