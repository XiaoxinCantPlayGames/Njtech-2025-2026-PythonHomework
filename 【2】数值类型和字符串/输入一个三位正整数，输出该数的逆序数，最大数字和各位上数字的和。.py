# 输入一个三位正整数，输出该数的逆序数，最大数字和各位上数字的和。
# 输入示例：
# 428
# 输出示例：
# 824
# 8
# 14

# 字符串解法
x = input()
print(eval(x[::-1]))
print(max(int(x[0]),int(x[1]),int(x[2])))
print(int(x[0])+int(x[1])+int(x[2]))

# 数学解法，当然有其他办法获得a,b,c
x = input()
a = int(x[0])
b = int(x[1])
c = int(x[2])
print(c*100+b*10+a)
print(max(a,b,c))
print(a+b+c)