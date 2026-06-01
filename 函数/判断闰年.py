#编写一个程序，在主程序中求1900~2020中所有的闰年，每行输出5个年份，每个年份用一个空格分隔。

#要求定义一个函数isLeap，该函数用来判断某年是否为闰年，是闰年则函数返回True，否则返回False。

#判断闰年的方法：某年能被4整除但是不能被100整除，或者能被400整除。









def isLeap(x):
    if x%400==0:
        return True
    elif x%4==0 and x%100!=0:
        return True
cnt=0
for i in range(1900,2020+1):
    if isLeap(i)==True:
        print(i,end=' ')
        cnt+=1
        if cnt%5==0:
            print()
        
