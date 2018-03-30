import sys,collections
import commands

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


file1 = open('percent_k_ginni.csv','w')
file2 = open('time_k_ginni.csv','w')
file3 = open('ginni_k.csv','w')

for k in range(0,maxK):
    status, output = commands.getstatusoutput("python Part3.py " + sys.argv[1] + " modularityclass.csv 26 " + str(k))
    which = output.split()[0]
    val = output.split()[1]
    ginni = output.split()[2]
    file3.write(str(k) + "," + ginni + '\n')
    print k
    if int(which) == 0 :
        file1.write(str(k) + "," + val + "," + ginni + '\n')
    else:
        file2.write(str(k)+","+val+ "," + ginni + '\n')
