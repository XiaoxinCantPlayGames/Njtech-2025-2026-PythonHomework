# 定义列表students存储下表三个学生的信息，
# 姓名性别年龄 籍贯
# Plain Text
# 
# ls=[‘张山'，'男，18，‘江苏南京”],
# 2
# [‘李诗’，‘女’，19,‘山东济南”],
# 3
# [王武’，‘男’，20,‘江苏镇江’]
#
# 并通过列表的遍历实现：
# 1）输出所有学生的姓名和年龄；（一行一个学生的姓名和年龄，用一个空格分隔）
# 2）输出所有男生的姓名和籍贯；（一行一个学生的姓名和籍贯，用一个空格分隔）
# 3）统计江苏省的学生人数；（单独一行输出一个值，表示人数。提示：使用in运算符判断籍贯是否包含江苏)
# 4）求学生的平均年龄。（单独一行输出一个值，表示平均年龄）



students = [['张山','男',18,'江苏南京'],['李诗','女',19,'山东济南'],['王武','男',20,'江苏镇江']]
# 1）输出所有学生的姓名和年龄
for student in students:
    print(student[0],student[2])

# 2）输出所有男生的姓名和籍贯
for student in students:
    if student[1] == '男':
        print(student[0],student[3])

# 3）统计江苏省的学生人数
count = 0
for student in students:
    if '江苏' in student[3]:
        count += 1
print(count)

# 4）求学生的平均年龄
total_age = sum(student[2] for student in students)
average_age = total_age / len(students)
print(average_age)