# 求s=a+aa+aaa+...+aaa...aaa的值，其中a是1~9之间的某个数字，n是一个正整数。例如:若a=2,n=5,则s=2+22+222+2222+22222=24690。
# 【提示】
# 如何表示该多项式中的某一项呢？
# 可利用字符串的乘法特性，比如”2"*2的值为”22”，"2"*3的值为”222”。如果a=2，则第二项为
# int(str(a)*2),第三项为int(str(a)*3),第四项为int(str(a)*4),第n项为int(str(a)*n)。
# 输入输出格式说明：
# 输入：有两行，第一行表示a的值，第二行表示n的值。
# 输出：计算结果
# 输入输出样例：
# 输入：
# 2
# 5
# 输出：
# 24690


# 循环
a = eval(input())
n = eval(input())
s = 0
for i in range(1, n + 1):
    s += int(str(a) * i)
print(s)


# 定义函数fun()，该函数根据参数a和n的值返回表达式a+aa+aaa+...+aaa...aaa的值，并在主程序中测试该函数。
def fun(a,n):
    s = 0
    for i in range(1,n+1):
        s += int(str(a)*i)
    return s
print(eval(input()))
