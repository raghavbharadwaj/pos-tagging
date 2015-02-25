import sys
import os
import json
import operator
import random
words = []
weights = {}

fcontents = open(sys.argv[1],'r')
words = []
for line in fcontents:
        words +=line.split()
words = [ 'BOS' ] + words + [ 'EOS' ]
newwords = []
wordstring = []
for i in range(1,len(words)-1):
	label = words[i].rsplit('/',1)
	newwords = ""
	newwords +=label[1] +" prev:"+words[i-1].rsplit('/',1)[0]+" cur:"+words[i].rsplit('/',1)[0]+" nex:"+words[i+1].rsplit('/',1)[0]+'\n'
	wordstring.append(newwords)



def changeweight(prevword,curword,nexword,predpos,curpos,weights,labels):
	weights[predpos][prevword]-=1
	weights[predpos][curword]-=1
	weights[predpos][nexword]-=1
	weights[curpos][prevword]+=1
	weights[curpos][curword]+=1
	weights[curpos][nexword]+=1


def initialize(weights,labels):
	for label in labels:
		weights[label]={}
	for label in labels:
		for line in wordstring:
			flist = line.split()
			if flist[1] not in weights[label]:
				weights[label][flist[1]]=0
			if flist[2] not in weights[label]:
					weights[label][flist[2]]=0
			if flist[3] not in weights[label]:
					weights[label][flist[3]]=0

	 
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


labels = []
for line in wordstring:
	label = line.split()[0]
	if label not in labels:
		labels.append(label)
print(labels)
def total(weights,average):
	for key1 in weights.keys():
		for key2 in weights[key1].keys():
			average[key1][key2]+=weights[key1][key2]

initialize(weights,labels)		
'''for i in range(1,2):
	for line in wordstring:
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
print(wordstring)'''
f = open('fdicttry','w+')
json.dump(weights,f)
#fcontents.close()
#f.close()
