import sys
cin = sys.stdin

K = int(sys.argv[2])
src = int(sys.argv[3])
N = 1723
done = 1
data = []
devices = {}
finTime = -1
copies = 0


class Device:
	def __init__(self,did,hasChunk):
		self.id=did
		self.Ng=0
		self.hasChunk=hasChunk

class Sighting:
	def __init__(self,time,id1,id2):
		self.time=time
		self.id1=id1
		self.id2=id2

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

def transferData(sender,reciever):
	if sender.Ng==K :
		return
	sender.Ng+=1
	reciever.hasChunk=True
	global copies,done
	copies+=1
	done+=1

for sight in data:
	device1 = getDevice(sight.id1)
	device2 = getDevice(sight.id2)
	if device1.hasChunk^device2.hasChunk:
		transferData(device1,device2) if device1.hasChunk else transferData(device2,device1)
	if (done*100)>(N*90):
		finTime = sight.time
		break

if finTime==-1:
	print "0",(done*100)/(N+0.0)
else:
	print "1",finTime
