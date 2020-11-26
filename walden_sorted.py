import collections
t=open("text.txt").read()
t=t.replace(',','').replace('.','').replace('"','').replace(':','')
t=t.split()
r=collections.Counter(t)
print(r)