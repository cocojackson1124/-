import random
n = int(random.random()*50+1)
i = 1
while i <= 5:
    cin = int(input("请输入你要猜的数字："))
    if(i == 5 and cin != n):
        print("你已经猜了5次了，并且都没有猜中，本局是你的败北")
        break
    elif (cin < n):
        print("你输入的数比较小")
        i = i + 1
    elif (cin > n):
        print("你输入的数比较大")
        i = i + 1
    elif(cin == n):
        print("恭喜你猜对了")
        break
