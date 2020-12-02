def move(players,step):
    return players #根据step做了元素的移动

def play(players,step,alive):
#生成一个列表，从[1,...,players]
    list1=[i for i in range(1,players+1)]
#进入游戏循环，每次数到step时淘汰，step之前的元素移动到列表末尾
#游戏结束的条件：列表剩余人数小于alive
    while len(list1)>alive:
#移动step前的元素到列表末尾
#将如何step的元素从列表中删除
        num=step-1
        while num>0:
            tmp=list1.pop(0)
            list1.append(tmp)
            num=num-1
        list1=move(list1,step)
        list1.pop(0)
    return list1    
players_num=int(input("请输入参加游戏的人数"))
step_num=int(input("请输入淘汰的数字"))
alive_num=int(input("请输入幸存的人数"))

play_list=play(players_num,step_num,alive_num)
alive_list=play_list
print(alive_list)
