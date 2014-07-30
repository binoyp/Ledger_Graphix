# This is the main file
import re,subprocess,shlex
from datetime import date
class dateArray:
    """
    A class to hold date values in List
    add date as string  yyy/m/dd
    
    
    """
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
    """
    Return output of ledger query as list
    arg are ledger arguements
    
    """
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
    
class LedgerPlotter:
    def __init__(self,args):
        self.ledger_out_as_list = led_argParser(args)
        
    def BalanceSummary(self,arg):
        """
        Gets the status of Total Expenses in Detail
        Input arguements should start with -s bal [arguements]      
        """        
        arg = '-s bal '+arg
        print arg
        self.ledger_out_as_list = led_argParser(arg)
        
        reqd_Data   = self.ledger_out_as_list[0:-2] #crops to required data
        #amount Rs AccName
        dictBarChart = {}
        for line in reqd_Data:
            (amount,AccountName) = (line[0],line[2])
            dictBarChart[AccountName]=amount
        print dictBarChart    
        for i,key in enumerate(dictBarChart):
            if float(dictBarChart[key]) <= 0:
                c = 'red'
            else:
                c = 'green'
            plt.bar(i,float(dictBarChart[key]),color=c,alpha =0.5)
        plt.xticks(np.arange(len(dictBarChart))+0.4, dictBarChart.keys(),\
        rotation =270)
        plt.ylabel("Rupees")
        plt.show()   