import shlex, subprocess, re
from datetime import date
import numpy as np
class dateArray:
    def __init__(self):
        self.array =[]
    def add(self,dt):
        ldt =[int(i) for i in dt.split("/")]
        self.array.append(date(ldt[0],ldt[1],ldt[2]))
    def __str__(self):
        out =""
        for dt in self.array:
            out += dt.strftime("%A %d-%m-%y") + '\n'
        return out
    def __getitem__(self,index):
        return self.array[index]
    def __call__(self):
        return self.array
    
def led_argParser(arg):
    def line2list():
        p = re.compile('[^\s]+')
        return p.findall
    arg = "ledger "+ arg
    args = shlex.split(arg)
    
    p = subprocess.Popen(args,stdout= subprocess.PIPE,stdin = subprocess.PIPE,\
                         shell= True)
    count = 0
    f= line2list()
    outList =[]
    for i in p.stdout:
        outList.append(f(i))
        count += 1
    return outList
dArr = dateArray()
vArr =[]   
for line in  led_argParser("-n -p 'every day' reg ^Exp"):
    print line
    dArr.add(line[0])
    vArr.append(float(line[4]))
    

for (d,v) in zip(dArr,vArr):
    print d,v
    
import matplotlib.pyplot as plt
plt.plot(dArr(),vArr,'-')
plt.xlabel('Day')
plt.ylabel('Expense in Rs')
plt.show()
#     