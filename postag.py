import sys
import os
import json
import operator
import random
fcontents = open(sys.argv[1],'r')
words = []
weights = {}
def changeweight(prevword,curword,nexword,predpos,curpos,weights,labels):
	weights[predpos][prevword]-=1
	weights[predpos][curword]-=1
	weights[predpos][nexword]-=1
	weights[curpos][prevword]+=1
	weights[curpos][curword]+=1
	weights[curpos][nexword]+=1


def initialize(weights,labels,average):
	for label in labels:
		weights[label]={}
		average[label]={}
	features = open (sys.argv[1],'r')
	for line in features:
		flist = line.split()
		for label in labels:
			if flist[1] not in weights[label]:
				weights[label][flist[1]]=0
			if flist[2] not in weights[label]:
				weights[label][flist[2]]=0
			if flist[3] not in weights[label]:
				weights[label][flist[3]]=0
	features.close()
	 	
def wordclass(prevword,curword,nexword,weights,labels):
	pred_label_sum=0
	for label in labels:
		temp_label_sum = weights[label][prevword] + weights[label][curword]+weights[label][nexword]
		if temp_label_sum >= pred_label_sum:
			pred_label_sum=temp_label_sum
			pred_label=label
	return pred_label
def devwordclass(prevword,curword,nexword,weights,labels):
        for label in labels:
                pred_label_sum=0
                temp_label_sum = weights[label][prevword] + weights[label][curword]+weights[label][nexword]
                if temp_label_sum >= pred_label_sum:
                        pred_label_sum=temp_label_sum
                        pred_label=label
        return pred_label


flabels = open(sys.argv[1],'r')
labels = []
for line in flabels:
	label = line.split()[0]
	if label not in labels:
		labels.append(label)
flabels.close()
average = {}
def total(weights,average):
	for key1 in weights.keys():
		for key2 in weights[key1].keys():
			average[key1][key2]+=weights[key1][key2]
fcontents = open(sys.argv[1],'r')
initialize(weights,labels,average)		
for i in range(1,15):
	for line in fcontents:
		linecontents = line.split()
		prevword = linecontents[1]
		nexword = linecontents[3]
		curword=linecontents[2]
		curpos = linecontents[0]
		pred_pos = wordclass(prevword,curword,nexword,weights,labels)
		if curpos!=pred_pos:
			changeweight(prevword,curword,nexword,pred_pos,curpos,weights,labels)
	#total(weights,average)

	#dev(weights)
	#random.shuffle(words)

#print(average,file=faverage)
fcontents.close()
f = open('fdict','w+')
json.dump(weights,f)
fcontents.close()
f.close()
