import sys,collections
import commands
import random
import numpy as np
import threading


data = []
devices = []
with open(sys.argv[1]) as f:
    file_content = f.readlines()
    for line in file_content:
        line_content = line.rstrip('\n').split(";")
        devices.append(int(line_content[1]))
        devices.append(int(line_content[2]))
devices = sorted(list(set(devices)))

N = len(devices)
maxK = 150
# print np.std(devices)

file1 = open('percent_k_100.csv','w')
file2 = open('time_k_100.csv','w')

src=[]
for i in range(100):
    src.append(random.randint(0,N-1))

class thr(threading.Thread):
    def __init__(self,name,kk):
        threading.Thread.__init__(self)
        self.name = name
        self.k = kk
    def run(self):
        data_1 = []
        data_2 = []
        global src
        for i in range(0,100):
            status, output = commands.getstatusoutput("python Part1.py " + sys.argv[1] + " " + str(self.k) + " " + str(devices[src[i]]))
            which = output.split()[0]
            val = output.split()[1]
            if int(which) == 0 :
                data_1.append(float(val))
            else:
                data_2.append(float(val))
        if len(data_1):
            file1.write(str(self.k) + "," + str(np.mean(data_1)) +","+ str(np.std(data_1)) +'\n')
            file1.flush()
        if len(data_2):
            file2.write(str(self.k) + "," + str(np.mean(data_2)) +","+ str(np.std(data_2)) +'\n')
            file2.flush()
        print self.k




k=1
while k < maxK:
    thr_obj = []
    for i in range(12):
        thr_obj.append(thr("tt",k+i))
        thr_obj[i].start()
    for i in range(12):
        thr_obj[i].join()
    k+=12
