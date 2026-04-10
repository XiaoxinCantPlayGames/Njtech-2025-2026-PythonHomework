# 编写程序，让用户输入一个字符串，然后统计这个字符串中有多少个元音字母（aeiou，不区分大小写），并输出结果。
# 输入示例：
# aei34590A
# 输出示例：
# 4


# 列表存储元音字母
yuan = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
s = input()
count = 0
for i in s:
    if i in yuan:
        count += 1
print(count)


# 暴力判断
s = input()
count = 0
for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        count += 1
print(count)


# 字符串处理：以全部转换为小写字母为例（同理也可以将i中的字母全部转换为大写字母进行判断）
s = input()
count = 0
for i in s:
    if i.lower() in "aeiou": # 将i中的字母全部转换为小写字母进行判断
        count += 1
print(count)