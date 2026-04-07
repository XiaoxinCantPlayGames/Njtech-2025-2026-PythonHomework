# 编程计算1*2*3*……*n的结果。n的值由用户输入。
# 输入输出样例1：
# 3
# 6
# 输入输出样例1：
# 5
# 120

# for循环
n = eval(input())
result = 1
for i in range(1,n+1):
    result = result*i
print(result)

# while循环
n = eval(input())
result = 1
i = 1
while i<=n:
    result = result*i
    i = i+1
print(result)
