import sys
import os
import json
import operator
import random
fcontents = open(sys.argv[1],'r')
words = []
weights = {}
def dev(weights):
	dsuccess_count=0
	dcount=0
	fdev = open(sys.argv[3],'r')
	for line in fdev:
		linecontents = line.split()
		prevword=linecontents[1].rsplit('/')[0]
		nexword=linecontents[3].rsplit('/')[0]
		curword=linecontents[2].rsplit('/')[0]
		curpos=linecontents[0]
		pred_pos=wordclass(prevword,curword,nexword,weights,labels)
		if pred_pos==curpos:
			dsuccess_count+=1
		dcount+=1
	print(dsuccess_count/dcount)

def changeweight(prevword,curword,nexword,predpos,curpos,weights,labels):
	weights[prevword][predpos]-=1
	weights[curword][predpos]-=1
	weights[nexword][predpos]-=1
	weights[prevword][curpos]+=1
	weights[curword][curpos]+=1
	weights[nexword][curpos]+=1

def wordclass(prevword,curword,nexword,weights,labels):
	if prevword not in weights:
		weights[prevword]={}
		for label in labels:
			weights[prevword][label]=0
	if curword not in weights:
		weights[curword]={}
		for label in labels:
			weights[curword][label]=0
	if nexword not in weights:
		weights[nexword]={}
		for label in labels:
			weights[nexword][label]=0
	for label in labels:
		pred_label_sum=0
		temp_label_sum = weights[prevword][label] + weights[curword][label]+weights[nexword][label]
		if temp_label_sum >= pred_label_sum:
			pred_label_sum=temp_label_sum
			pred_label=label
	return pred_label

for line in fcontents:
	words +=line.split()
words = [ 'BOS' ] + words + [ 'EOS' ]
newwords = []
fout = open(sys.argv[2],'w+')
for i in range(1,len(words)-1):
	label = words[i].rsplit('/',1)
	newwords = []
	newwords +=label[1] +" prev:"+words[i-1].rsplit('/',1)[0]+" cur:"+words[i].rsplit('/',1)[0]+" nex:"+words[i+1].rsplit('/',1)[0]
	wordstring = ''.join(newwords)
	print(wordstring,file=fout)
words_new=[]
fout.close()
fout = open(sys.argv[3],'r')
labels = []
for line in fout:
	label = line.split()[0]
	if label not in labels:
		labels.append(label)
fout.close()
fout=open(sys.argv[3],'r')
average = {}
def total(weights,average):
	for key1 in weights.keys():
		if key1 not in average:
			average[key1]={}
		for key2 in weights[key1].keys():
			if key2 not in average[key1]:
				average[key1][key2]=weights[key1][key2]
			else:
				average[key1][key2]+=weights[key1][key2]
		
for i in range(1,2):
	for line in fout:
		linecontents = line.split()
		prevword = linecontents[1].rsplit('/')[0]
		nexword = linecontents[3].rsplit('/')[0]
		curword=linecontents[2].rsplit('/')[0]
		curpos = linecontents[0]
		pred_pos = wordclass(prevword,curword,nexword,weights,labels)
		if curpos!=pred_pos:
			changeweight(prevword,curword,nexword,pred_pos,curpos,weights,labels)
	total(weights,average)

	dev(weights)
	#random.shuffle(words)
#print(average,file=faverage)
fout.close()
f = open('fdict','w+')
json.dump(weights,f)
fcontents.close()
