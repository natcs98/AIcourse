import os
import numpy as np
name='myfile.txt'
check=os.path.exists(name)
print(check)
line='001,john,12-06-1999'
infor=line.split(',')
string=(',').join(infor)
print(string)
print(line==string)
a=[1,0,1,0,1,0,1,0,1,1]
print(sum(a))
#C://Users//Administrator//Documents//NetBeansProjects//SpamEmail//SpamEmail//data//datatrain//data.dat
file =open('C://Users//Administrator//Documents//NetBeansProjects//SpamEmail//SpamEmail//data//datatrain//data.dat','rb')
print(x)
file.close()