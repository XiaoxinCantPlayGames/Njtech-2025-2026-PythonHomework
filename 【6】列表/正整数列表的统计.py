# 输入一个正整数列表，统计该列表中奇数的个数、偶数的个数、奇数的和、偶数的和，以及所有数的平均值。
# 输入格式：
# 一行列表格式的正整数序列。
# 输出格式：
# 一行值，分别表示奇数的个数、偶数的个数、奇数的和、偶数的和、所有数的平均值，各个值之间用一个空格分隔。
# 输入输出样例：
# 输入：
# [1,2,3,4,5,6,7,8,9,10]
# 输出：
# 5 5 25 30 5.5



numbers = eval(input()) # 获取输入的正整数列表
odd_count = 0 # 奇数个数
even_count = 0 # 偶数个数
odd_sum = 0 # 奇数和
even_sum = 0 # 偶数和
for num in numbers: # 遍历列表中的每个数
    if num % 2 == 0: # 如果是偶数
        even_count += 1 # 偶数个数加1
        even_sum += num # 偶数和加上该数
    else: # 如果是奇数
        odd_count += 1 # 奇数个数加1
        odd_sum += num # 奇数和加上该数
average = sum(numbers) / len(numbers) # 计算所有数的平均值
print(odd_count, even_count, odd_sum, even_sum, average)