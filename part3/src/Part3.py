import sys,random
cin = sys.stdin

src=int(sys.argv[3])
p = int(sys.argv[4])
data = []
devices = {}
copies=0
done=0
N=1723
finTime=-1

class Device:
	def __init__(self,did,hasChunk):
		self.id=did
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

def getDevice(did):
	if not did in devices:
		device = Device(did,did==src)
		devices[did]=device
	return devices[did]

def createDevices():
	for sight in data:
		device1 = getDevice(sight.id1)
		device2 = getDevice(sight.id2)

def categorise():
	with open(sys.argv[2]) as f:
		file_content = f.readlines()
		for line in file_content:
			line_content = line.rstrip('\n').split(";")
			did = int(line_content[0])
			catg = int(line_content[1])
			devices[did].catg=catg

def transferData(sender,reciever):
	global copies,done
	sample = random.randint(1,100)
	if (reciever.catg!=sender.catg and sample>p) or (reciever.catg==sender.catg and sample<=p):
		return
	reciever.hasChunk=True
	sender.transmit+=1
	copies+=1
	done+=1

readFile()
createDevices()
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

ginni_num = 0.0
ginni_den = 0.0
nn = 0
for device1 in devices.values():
	for device2 in devices.values():
		ginni_num+= abs(device1.transmit - device2.transmit)
	nn+=1
	ginni_den+= device1.transmit

ginni_den = 2 * nn * ginni_den
if ginni_den==0:
	print 0.0
ginni = (ginni_num/ginni_den)
print ginni
