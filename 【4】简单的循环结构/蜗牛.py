# 一只蜗牛住在井底，想爬出去看看井外的世界，于是开始沿着井壁向上爬。白天蜗牛可以向上
# 爬5米，晚上会下滑3米，输入不同的井深，计算第几天蜗牛可以爬出井，看到外面的世界。
# 输入输出样例1：
# 输入：
# 5
# 输出：
# 1天
# 输入输出样例2：
# 输入：
# 6
# 输出：
# 2天


depth = eval(input())
day = 0
while depth>0:
    day = day+1
    depth = depth-5
    if depth<=0:
        break
    depth = depth+3
print(f"{day}天")