#【幸运素数】
#素数，又称质数，是指除1和其自身之外，没有其他约数的正整数。例如2、3、5、 13 都是素数，而4、9、 12、18 则不是。特别地，规定1不是素数(因此自然数的质因数分解就是唯一的)。
#如果一个数本身是素数，并且把最低位删除后得到的数仍是素数、再把最低位删除后得到的数仍是素数... ..如此往复，直到得到一个一位素数，我们就称它是“幸运素数”。以233为例:
#233 本身是素数；
#23 = [233/10] 是素数;
#2 = [23/10]是素数，
#因此233 是“幸运”素数。而211则不是幸运素数:虽然211是素数， 但21不是素数。请编程求出一定范围内的所有幸运数字。
#输入输出示例:
#输入
#6
#30
#输出
#7
#23
#29







def fun1(x):
    if x==1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
        else:
            return True
#错误写法：
#        for i in range(2,x):
#            if x%i!=0:
#                return True
#        else:
#            return False
#除以一个因数没有余数不一定是素数
#除以一个因数等于0一定不是素数
        
m=eval(input())
n=eval(input())
for j in range(m,n+1):
    k=j
    while k!=0:#不确定多久结束，用while循环
        if fun1(k)==False:
            break
        k=k//10
    else:#else在for，while中的应用
        print(j)
   

