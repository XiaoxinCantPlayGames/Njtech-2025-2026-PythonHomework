# 计算奥运会比赛某个参赛选手的得分。假设共有10个裁判，每个裁判给该参赛选手打分（分值在0~10之间），去掉一个最高分和一个最低分之后的平均分即为该运动员的最后得分。
# 提示：使用内置的max()方法求出最高分、min()方法求出最低分、remove()方法删除一个最高分和一个最低分。
# 输入输出格式：
# 输入：一行列表格式的数，数可以是整数，也可以是小数。
# 输出：一个值，代表运动员的最后得分。
# 输入输出样例：
# 输入：
# [9, 10, 8, 9, 10, 7, 6, 8, 7, 8]
# 输出：
# 8.25



# 一步一步来
scores = eval(input()) # 获取输入的分数列表
max_score = max(scores) # 获取最高分
min_score = min(scores) # 获取最低分
scores.remove(max_score) # 删除最高分
scores.remove(min_score) # 删除最低分
average = sum(scores) / len(scores) # 计算平均分
print(average) # 输出最后得分


# 嵌套
scores = eval(input()) # 获取输入的分数列表
scores.remove(max(scores)) # 删除最高分
scores.remove(min(scores)) # 删除最低分
average = sum(scores) / len(scores) # 计算平均分
print(average) # 输出最后得分