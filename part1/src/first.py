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
maxK = 100


file1 = open('percent_k.csv','w')
file2 = open('time_k.csv','w')

for k in range(1,maxK):
    status, output = commands.getstatusoutput("python Part1.py " + sys.argv[1] + " " + str(k) + " 26")
    which = output.split()[0]
    val = output.split()[1]
    if int(which) == 0 :
        file1.write(str(k) + "," + val + '\n')
    else:
        file2.write(str(k)+","+val+'\n')
