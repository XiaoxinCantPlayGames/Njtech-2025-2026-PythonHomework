# n!!表示正整数n的双阶乘，即不超过n且与n具有相同奇偶性的所有正整数的乘积。
# 例如：
# 3!!=3x1=3
# 8!! =8 x6×4 ×2 =384
# 11!=11×9×7×5×3×1=10395
# 输入列表lst1，列表lst1中的元素均为正整数。
# 编写程序创建列表lst2，将列表lst1中每个元素对应的双阶乘数存放在列表lst2中，输出lst2。
# 输入输出示例：
# 输入：
# [3,8,11]
# 输出：
# [3,384,10395]



# 函数
def double_factorial(n):
    if n == 0 or n == 1: # 双阶乘的定义：0!!=1，1!!=1
        return 1
    else:
        return n * double_factorial(n - 2) # 递归计算双阶乘

lst1 = eval(input()) # 获取输入的列表
lst2 = [double_factorial(num) for num in lst1] # 使用列表推导创建新列表，计算每个元素的双阶乘
print(lst2) # 输出结果


# 列表推导
lst1 = eval(input()) # 获取输入的列表
lst2 = [num * double_factorial(num - 2) if num > 1 else 1 for num in lst1] # 使用列表推导创建新列表，计算每个元素的双阶乘
print(lst2) # 输出结果


# for循环
lst1 = eval(input()) # 获取输入的列表
lst2 = [] # 创建空列表
for num in lst1: # 遍历输入列表中的每个元素
    if num == 0 or num == 1: # 双阶乘的定义：0!!=1，1!!=1
        lst2.append(1) # 将1添加到新列表中
    else:
        lst2.append(num * double_factorial(num - 2)) # 计算双阶乘并添加到新列表中
print(lst2) # 输出结果