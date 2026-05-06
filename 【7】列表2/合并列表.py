# 设有列表lst_odd=[1,3,5,7,9]和列表lst_even=[2,4,6,8,10]。试编写程序，将两个列表合
# 并成一个新的列表，并将新列表按照元素的大小降序排列。
# 【要求】不改变列表lst_odd和 lst_even的元素。
# 输出格式：
# 排好序的整个列表。



lst_odd = [1,3,5,7,9]
lst_even = [2,4,6,8,10]
lst = lst_odd + lst_even # 合并两个列表
lst.sort(reverse=True) # 将列表按照元素的大小降序排列
print(lst)