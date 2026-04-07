# 从键盘上输入若干个整数，并求出这些数中所有奇数之和、偶数之和及所有数的平均值。当从
# 键盘输入字符’Q’或者‘q‘时，程序停止接收输入，并输出计算结果。
# 提示：使用while循环结构
# 输入输出格式说明：
# 输入：有多行，每行代表一个整数，最后一行为Q或者q。
# 输出：一行，依次为奇数之和、偶数之和、所有数的平均值，各值间隔一个空格。
# 输入输出样例1：
# 输入：
# q
# 输出：
# 未输入整数
# 输入输出样例2：
# 输入：
# 1
# 2
# 3
# 4
# q
# 输出：
# 46 2.5


# 列表
num = []
while True:
    x = input()
    if x=='Q' or x=='q':
        break
    num.append(int(x))
if len(num)==0:
    print("未输入整数")
else:
    odd_sum = 0 # 奇数之和
    even_sum = 0 # 偶数之和
    for i in num:
        if i%2==0:
            even_sum = even_sum+i
        else:
            odd_sum = odd_sum+i
    average = sum(num)/len(num)
    print(f"{odd_sum} {even_sum} {average}")


# 变量
odd_sum = 0 # 奇数之和
even_sum = 0 # 偶数之和
count = 0 # 输入的整数个数
total = 0 # 输入的整数之和
while True:
    x = input()
    if x=='Q' or x=='q':
        break
    num = int(x)
    total = total+num
    count = count+1
    if num%2==0:
        even_sum = even_sum+num
    else:
        odd_sum = odd_sum+num
if count == 0:
    print("未输入整数")
else:
    average = total / count
    print(f"{odd_sum} {even_sum} {average}")