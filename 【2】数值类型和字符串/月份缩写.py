# 已知月份字符串为：months="JanFebMarAprMayJunJulAugSepOctNovDec"
# 用户输入一个整数，输出对应的月份缩写。


# 字典
months={"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May",
        "6":"Jun","7":"Jul","8":"Aug","9":"Sep",
        "10":"Oct","11":"Nov","12":"Dec"}
x = input()
print(months[x])

# 字符串切片
months="JanFebMarAprMayJunJulAugSepOctNovDec"
x = input()
print(months[(int(x)-1)*3:(int(x)-1)*3+3])