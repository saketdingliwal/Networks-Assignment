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

s_choice = [0.5,1,5,10,20]
l_choice = [50,60,70,80,90]

for gh in range(5):
    s = s_choice[gh]
    l = 70
    per_name = 'percent_k_ginni' + str(s) + '_' + str(l)+'.csv'
    time_name = 'time_k_ginni' + str(s) + '_' + str(l)+'.csv'
    trans_name = 'trans_k_ginni' + str(s) + '_' + str(l)+'.csv'
    file1 = open(per_name,'w')
    file2 = open(time_name,'w')
    file3 = open(trans_name,'w')

    for k in range(0,maxK):
        status, output = commands.getstatusoutput("python Part2.py " + sys.argv[1] + " 26 " + str(s) + " 70 " + str(k))
        which = output.split()[0]
        val = output.split()[1]
        if int(which) == 0 :
            file1.write(str(k) + "," + val + "," +output.split()[2] +  "," +output.split()[3]+ "," +output.split()[4] + "," +output.split()[5] + '\n')
        else:
            file2.write(str(k) + "," + val + "," +output.split()[2] +  "," +output.split()[3]+ "," +output.split()[4] +  "," +output.split()[5] + '\n')
        file3.write(str(k) + "," + output.split()[2] +  "," +output.split()[3]+ "," +output.split()[4] +  "," +output.split()[5] + '\n')
        print k


for gh in range(5):
    l = l_choice[gh]
    s = 0.5
    per_name = 'percent_k_ginni' + str(s) + '_' + str(l)+'.csv'
    time_name = 'time_k_ginni' + str(s) + '_' + str(l)+'.csv'
    trans_name = 'trans_k_ginni' + str(s) + '_' + str(l)+'.csv'

    file1 = open(per_name,'w')
    file2 = open(time_name,'w')
    file3 = open(trans_name,'w')

    for k in range(0,maxK):
        status, output = commands.getstatusoutput("python Part2.py " + sys.argv[1] + " 26 "  + "0.5 " + str(l) + " " + str(k))
        which = output.split()[0]
        val = output.split()[1]
        if int(which) == 0 :
            file1.write(str(k) + "," + val + "," +output.split()[2] +  "," +output.split()[3] + "," +output.split()[4] + "," +output.split()[5] + '\n')
        else:
            file2.write(str(k) + "," + val + "," +output.split()[2] +  "," +output.split()[3]+ "," +output.split()[4] + "," +output.split()[5] + '\n')
        file3.write(str(k) + "," + output.split()[2] +  "," +output.split()[3]+ "," +output.split()[4] +  "," +output.split()[5] + '\n')
        print k
