#输入一串字符作为密码,密码只能由数字与字母组成。

#编写一个函数judge(password)，用来求出密码的强度level，并在主程序中测试该函数,输出对应密码强度。

#密码强度判断准则如下，满足其中一条，密码强度增加一级：

#①有数字;    ②有大写字母;    ③有小写字母;    ④位数不少于8位

#如输入测试密码：Abc12345，密码强度为4级

#   输入测试密码：abc123，密码强度为2级

#示例：

#输入：

#Abc123

#输出

#3






def judge(x):
    cnt=0
    if len(x)>=8:
        cnt+=1           
    for i in x:
        if i.isdigit():
            cnt+=1
            break
    for j in x:
        if j.islower():
            cnt+=1
            break
    for k in x:
        if k.isupper():
            cnt+=1
            break           
    return cnt
        
s=input()
print(judge(s))


