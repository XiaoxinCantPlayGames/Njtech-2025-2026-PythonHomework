# 从键盘输入正整数n，输出斐波拉契数列的前n的和。要求使用列表生成斐波拉契数列。
# 【提示】：求出前n项数列值，存入列表，再对列表求和
# 输入输出样例如下：
# 输入：
# 5
# 输出
# 12



n = int(input())
x, y, count = 1, 1, 2 # x和y是数列中的第一二项，count是用来计数的
_ = [] # 存放计算结果的列表
_.append(x)
_.append(y)
for _ in range(2, n):
    x, y = y, x + y
    _.append(y)
print(sum(_))