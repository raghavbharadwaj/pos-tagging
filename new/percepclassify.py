import sys
import os
import json
fjson = open(sys.argv[1],'r')
weights = json.load(fjson)
def dev(weights):
	dsuccess_count=0
	dcount=0
	fdev = open(sys.argv[2],'r')
	for line in fdev:
		linecontents = line.split()
		prevword=linecontents[1]
		nexword=linecontents[3]
		curword=linecontents[2]
		curpos=linecontents[0]
		pred_pos=wordclass(prevword,curword,nexword,weights)
		if pred_pos==curpos:
			dsuccess_count+=1
		dcount+=1
	fdev.close()
	print(dsuccess_count/dcount)

def wordclass(prevword,curword,nexword,weights):
	pred_sum=0
	pred_label=""
	for label in weights.keys():
		temp_sum=0
		if prevword in weights[label]:
			temp_sum += weights[label][prevword]
		if curword in weights[label]:
			temp_sum +=weights[label][curword]
		if nexword in weights[label]:
			temp_sum +=weights[label][nexword]
		if temp_sum >= pred_sum:
			pred_sum = temp_sum
			pred_label=label
	return pred_label
dev(weights)
print(weights.keys())

