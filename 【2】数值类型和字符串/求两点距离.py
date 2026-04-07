# 输入平面直角坐标系中的两点坐标 A(x1,y1) 和 B(x2,y2)。
# 计算AB两点之间的距离，结果保留两位小数。
# 距离=√((x1-x2)²+(y1-y2)²)
# 输入语句如下：
# x1,y1=eval(input())#一次输入两个值
# 输入示例：
# 3,0
# 0,4
# 输出示例：
# 5.00


# math库的sqrt方法
import math
x1,y1 = eval(input())
x2,y2 = eval(input())
x = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
print(f"{x:.2f}")


# 幂运算
x1,y1 = eval(input())
x2,y2 = eval(input())
x = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**(1/2)
print(f"{x:.2f}")
