import sys
import os
import json
import io
fjson = open(sys.argv[1],'r')
weights = json.load(fjson)
data = io.open(sys.stdin.fileno(),'r',encoding='latin-1')

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
def dev(weights,line):
	outputline=''
	for feature in line:
		words = feature.split()
		prevword=words[0]
		nexword=words[2]
		curword=words[1]
		pred_pos=wordclass(prevword,curword,nexword,weights)
		outputline+=curword.split(':')[1]+'/'+pred_pos+' '
	print(outputline)
def makefeature():
	for inputline in  io.open(sys.stdin.fileno(),'r',encoding='latin-1'):
		words = []
		line=[]
		words = inputline.split()
		words = [ 'BOS' ] + words + [ 'EOS' ]
		fout = open('feature_output.txt','w+',encoding='latin-1')
		for i in range(1,len(words)-1):
			label = words[i].rsplit('/',1)
			newwords = ''
			newwords +="prev:"+words[i-1].rsplit('/',0)[0]+" cur:"+words[i].rsplit('/',0)[0]+" nex:"+words[i+1].rsplit('/',0)[0]
			line.append(newwords)
		dev(weights,line)
       
makefeature()



