import random
import csv
data = csv.reader(open('人工智能201名单.csv'))
data = dict(data)
del data['学号']
num_in = input("要点几个人:")
for i in range(int(num_in)):
    r = int(random.random() * 39 + 1)
    classmate = data.pop(str(r))
    print(r, classmate)
