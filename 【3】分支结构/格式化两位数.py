# 输入一个两位整数，规格化该两位数，保证十位数大于等于个位数。
# 输入输出示例1：
# 34
# 43
# 输入输出示例2：
# 43
# 43


x = input()
a = eval(x[0])
b = eval(x[1])
if a < b:
    print(f"{b}{a}")
else:
    print(f"{a}{b}")