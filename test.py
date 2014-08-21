
import matplotlib.pyplot as plt
import numpy as np
from led_graphics import dateArray,led_argParser






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
        plt.xticks(np.arange(len(dictBarChart))+0.4, dictBarChart.keys(),rotation =270)
        plt.ylabel("Rupees")
        plt.show()
    def ExpenseSummary(self):
        """
        Out Pie Chart representation of Expenses
        """
        self.ledger_out_as_list = led_argParser('-s bal Exp')
        reqd_Data   = self.ledger_out_as_list[1:-2]
        dictPiechart = {}
        for line in reqd_Data:
            (amount,AccountName) = (line[0],line[2])
            dictPiechart[AccountName]=float(amount)
            
#        val =np.array(dictPiechart.values())  
        exp = [0.05]*len(dictPiechart)
        print exp
        plt.figure(figsize=(10,10))
        plt.pie(dictPiechart.values(),labels=dictPiechart.keys(),explode = exp)
        plt.show()


#    dArr.add(line[0])
#    vArr.append(float(line[0]))
#    xArr.append()
    

#for (d,v) in zip(dArr,vArr):
#    print d,v
    


if __name__ == "__main__":
    lplot = LedgerPlotter('-s bal ^Exp ')
#    lplot.BalanceSummary('Exp')
    lplot.ExpenseSummary()
    
