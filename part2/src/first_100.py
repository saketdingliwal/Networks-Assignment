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
maxK = 101
# print np.std(devices)

file1 = open('percent_k_100_ginni.csv','w')
file2 = open('time_k_100_ginni.csv','w')
file3 = open('trans_rate_100_ginni.csv','w')

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
        data_3 = []
        data_4 = []
        data_5 = []
	data_6 = []
        global src
        for i in range(0,100):
            status, output = commands.getstatusoutput("python Part2.py " + sys.argv[1] + " "  + str(devices[src[i]]) + " 0.5 70 " + str(self.k))
            which = output.split()[0]
            val = output.split()[1]
            data_3.append(float(output.split()[2]))
            data_4.append(float(output.split()[3]))
            data_5.append(float(output.split()[4]))
	    data_6.append(float(output.split()[5]))
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
        file3.write(str(self.k) + "," + str(np.mean(data_3)) +","+ str(np.std(data_3)) + "," + str(np.mean(data_4)) +","+ str(np.std(data_4)) + "," + str(np.mean(data_5)) +","+ str(np.std(data_5)) + "," + str(np.mean(data_6)) + "," + str(np.std(data_6)) + '\n')
        file3.flush()
        print self.k



Maxthread = 12
k=0
while k < maxK:
    thr_obj = []
    for i in range(Maxthread):
        thr_obj.append(thr("tt",k+i))
        thr_obj[i].start()
    for i in range(Maxthread):
        thr_obj[i].join()
    k+=Maxthread
