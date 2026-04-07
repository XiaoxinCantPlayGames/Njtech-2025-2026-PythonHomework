# 输入整数m和n，求区间[m,n]中所有的素数。
# 每行输出7个素数，每个素数之间一个空格分隔。
# 输入输出示例：
# 3,30#输入使用语句m,n=eval(inputO)
# 3 5711 13 17 19
# 23 29


m, n = input().split(",")
m, n = int(m), int(n)
count = 0 
for i in range(max(m,2),n+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        count += 1  # 统计素数的个数
        print(i,end=" ")
        if count % 7 == 0: # 每输出7个素数换行
            print()