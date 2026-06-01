#表示分段函数：
#x <0:        y=0
#0<=x<5:       y=x
#5<=x<10:      y=3x-5
#10<=x<20:     y=0.5x-2
#x>20:         y=0









x=eval(input())
if x <0:
    print(0)
elif 0<=x<5:
    print(x)
elif 5<=x<10:
    print(3*x-5)
elif 10<=x<20:
    ptint(0.5*x-2)
else:
    print(0)
