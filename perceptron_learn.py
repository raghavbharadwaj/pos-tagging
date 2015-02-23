import sys
import os
import json
import operator
import random
fcontents = open(sys.argv[1],'r')
words = []
weights = {}
def dev(weights):
	dwords=[]
	dsuccess_count=0
	dcount=0
	fdev = open (sys.argv[2],'r')
	for line in fdev:
		dwords+=line.split()
	for word in dwords:
		dwordpos = word.rsplit('/',1)
		pred_pos=wordclass(dwordpos[0],weights)
		if pred_pos==dwordpos[1]:
			dsuccess_count+=1
		dcount+=1
	print(dsuccess_count/dcount)

def initialize(word,pos,weights):
	weights[word]={}
	weights[word][pos]=1

def changeweight(word,pos,pred_pos,weights):
	if pos not in weights[word]:
		weights[word][pos]=0
	weights[word][pos]+=1
	weights[word][pred_pos]-=1	

def wordclass(word,weights):
	if word not in weights:
		return 0
	return max(weights[word].items(),key = operator.itemgetter(1))[0]

for line in fcontents:
	words +=line.split()
changed =0
for i in range(1,10):
	count=0
	for word in words:
		wordpos = word.rsplit('/',1)
		pred_pos = wordclass(wordpos[0],weights)
		if pred_pos == 0:
			count+=1
			initialize(wordpos[0],wordpos[1],weights)	
		elif wordpos[1]!=pred_pos:
			changeweight(wordpos[0],wordpos[1],pred_pos,weights)
	dev(weights)
	print(count)
	random.shuffle(words)
f = open('fdict','w+')
json.dump(weights,f)
fcontents.close()
