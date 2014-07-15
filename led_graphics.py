# This is the main file
import re,subprocess,shlex
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

