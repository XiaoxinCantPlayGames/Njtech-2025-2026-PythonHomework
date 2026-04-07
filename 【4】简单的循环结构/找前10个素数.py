# 由用户输入正整数n，由大到小输出小于等于n的前10个素数。
# 输入输出示例：
# 输入：
# 300
# 输出：
# 293
# 283
# 281
# 277
# 271
# 269
# 263
# 257
# 251
# 241


n = int(input())
count = 0
for i in range(n, 1, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1  # 统计素数的个数
        print(i)
        if count == 10: # 每输出7个素数换行
            break