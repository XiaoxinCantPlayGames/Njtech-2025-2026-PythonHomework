# 输入一个正整数，判断该数是否是平方数。如果是平方数，输出yes；否则输出no。
# 提示：一个数开平方后取整所得的值，再进行平方计算，等于该数本身，则该数为平方数。
# 输入输出样例一：
# 16
# yes
# 输入输出样例二：
# 23
# no


# math库的sqrt方法
import math
x = eval(input())
if math.sqrt(x) ** 2 == x:
    print("yes")
else:
    print("no")


# 幂运算
x = eval(input())
if int(x ** (1/2)) ** 2 == x:
    print("yes")
else:
    print("no")