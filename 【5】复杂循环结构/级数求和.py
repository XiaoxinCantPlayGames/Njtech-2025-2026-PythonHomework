# 用户输入n值，编写程序计算s=1+1/2+1/3+..+1/n的值。


n = int(input())
s = 0
for i in range(1, n + 1):
    s += 1 / i
print(s)