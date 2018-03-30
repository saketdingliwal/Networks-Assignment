import sys,random
import numpy as np
import matplotlib.pyplot as plt
cin = sys.stdin

src=int(sys.argv[2])
S = float(sys.argv[3])
L = float(sys.argv[4])
p = int(sys.argv[5])
deg_max=386
freq = [0]*deg_max
cumL = [0]*deg_max
data = []
devices = {}
copies=0
done=0
N=1723
finTime=-1

class Device:
	def __init__(self,did,hasChunk):
		self.id=did
		self.Ng=[]
		self.hasChunk=hasChunk
		self.catg=1
		self.transmit=0

class Sighting:
	def __init__(self,time,id1,id2):
		self.time=time
		self.id1=id1
		self.id2=id2

def readFile():
	with open(sys.argv[1]) as f:
		file_content = f.readlines()
		for line in file_content:
			line_content = line.rstrip('\n').split(";")
			data.append(Sighting(int(line_content[0]),int(line_content[1]),int(line_content[2])))

def fillNeighbours():
	for sight in data:
		id1 = sight.id1
		id2 = sight.id2
		device1 = getDevice(id1)
		device2 = getDevice(id2)
		device1.Ng.append(id2)
		device2.Ng.append(id1)

def formCCDF():
	global freq,cumL
	for did in devices:
		device = devices[did]
		device.Ng = list(set(device.Ng))
		freq[len(device.Ng)]+=1
	cumL[deg_max-1]=freq[deg_max-1]
	for i in xrange(deg_max-2,-1,-1):
		cumL[i]=cumL[i+1]+freq[i]
	# print freq
	x = np.arange(1,1+len(cumL))
	x = np.log(x)
	print x
	cumL = [(elem/1723.0) for elem in cumL]
	cumL = np.log(cumL)
	plt.figure()
    # plt.errorbar(np_arr[:,0],np_arr[:,5],yerr=np_arr[:,6],ecolor='red')
	plt.plot(x,cumL)
	plt.title("CCDF")
	plt.xlabel("degree")
	plt.ylabel("the complementary distribution function")
	plt.savefig("Plot/"+'demo_1' +'.png',bbox_inches='tight')

	# print len(cumL)


def categorise():
	temp = [device for device in devices.values()]
	list.sort(temp,key=lambda x: len(x.Ng))
	for i in xrange(N):
		device = temp[i]
		if ((i*100.0)/N)<=L:
			device.catg=0
		elif ((i*100.0)/N)>=(100-S):
			device.catg=2

def getDevice(did):
	if not did in devices:
		device = Device(did,did==src)
		devices[did]=device
	return devices[did]

def transferData(sender,reciever):
	global copies,done
	sample = random.randint(1,100)
	if (reciever.catg==2 and sample>p) or (reciever.catg==1 and sample<=p):
		return
	reciever.hasChunk=True
	sender.transmit+=1
	copies+=1
	done+=1

readFile()
fillNeighbours()
formCCDF()
categorise()
for sight in data:
	id1 = sight.id1
	id2 = sight.id2
	device1 = devices[id1]
	device2 = devices[id2]
	if device1.hasChunk^device2.hasChunk:
		transferData(device1,device2) if device1.hasChunk else transferData(device2,device1)
	if (done*100)>(N*90):
		finTime = sight.time
		break


if finTime==-1:
	print "0",(done*100)/(N+0.0),
else:
	print "1",finTime,


sumNd = [0.0]*3
ctNd = [0.0]*3


for device in devices.values():
	sumNd[device.catg]+=device.transmit
	ctNd[device.catg]+=1

ginni_num = 0.0
ginni_den = 0.0
nn = 0
for device1 in devices.values():
	for device2 in devices.values():
		ginni_num+= abs(device1.transmit - device2.transmit)
	nn+=1
	ginni_den+= device1.transmit

ginni_den = 2 * nn * ginni_den

ginni = (ginni_num/ginni_den)


print sumNd[0]/ctNd[0],sumNd[1]/ctNd[1],sumNd[2]/ctNd[2],ginni
