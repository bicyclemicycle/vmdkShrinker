import os
import sys
import signal

loc = sys.argv[1]

if len(sys.argv) > 2:
	VMWarePath = sys.argv[2]
else:
	# default install location for vmware
	VMWarePath = "C:\\Program Files (x86)\\VMware\\VMware Workstation"

def scan(path):
	# for folder in directory:
	for item in os.listdir(path):
		if os.path.isdir(path + "\\" + item):
			vmxfound = False
			# find a vmx file in the directory read it
			for vmxfile	in os.listdir(path + "\\" + item):
				if vmxfile.endswith(".vmx"):
					vmxfound = True
					try:
						with open(path + "\\" + item + "\\" + vmxfile, "rb") as vmx:
							for line in vmx:
								# find the first drive scsi 0:0, defrag and compact it
								if line.startswith("scsi0:0.fileName = \""):
									print "Defrag and compact: \"" + path + "\\" + item + "\\" + line[20:-1]
									os.system("vmware-vdiskmanager.exe -d \"" + path + "\\" + item + "\\" + line[20:-1])
									os.system("vmware-vdiskmanager.exe -k \"" + path + "\\" + item + "\\" + line[20:-1])
					except Exception as e:
						print e
						pass
			# if no vmx file was found, the directory might a directory to a VM so recursively search below
			if vmxfound == False:
				scan(path + "\\" + item)
# Main
os.chdir(VMWarePath)
scan(loc)

