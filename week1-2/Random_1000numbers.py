import random
a=[]
for i in range(1,10):
  x=9
  while x>=i:
    a.append(x)
    x=x-1
d={}
res=[]
for i in range(0,1000):
  x=random.randrange(0,len(a))
  res.append(a[x])
  if a[x] in d.keys():
    d[a[x]]+=1
  else:
    d[a[x]]=1
for i in range(1,10):
  #print(i)
  print(f' {i} ,{d[i]}')