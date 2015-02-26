import sys
import os
import json
import operator
import random
def main(argv):
	words = []
	average = {}
	weights = {}
	#random.shuffle(words)
	#print(average,file=faverage)
	flearn = open(argv[0],'r')
	contents = []
	for line in flearn:
		contents.append(line)
	flearn.close()
	for i in range(1,10):
		for line in contents:
			features=line.split()
			label = features[0]
			total=0
			temp=0
			pred_label=""
			if label not in weights:
				weights[label]={}
				average[label]={}
			for plabel in weights.keys():
				
				if features[1] not in weights[plabel]:
					weights[plabel][features[1]]=0
				if features[2] not in weights[plabel]:
					weights[plabel][features[2]]=0
				if features[3] not in weights[plabel]:
					weights[plabel][features[3]]=0
				temp = weights[plabel][features[1]] + weights[plabel][features[2]]+ weights[plabel][features[3]]
				if temp > total:
					total = temp
					pred_label = plabel
			if label!=pred_label:
				weights[label][features[1]]+=1
				weights[label][features[2]]+=1
				weights[label][features[3]]+=1
				if pred_label!="":
					weights[pred_label][features[1]]-=1
					weights[pred_label][features[2]]-=1
					weights[pred_label][features[3]]-=1
		
		for key1 in weights.keys():
			for key2 in weights[key1].keys():
				if key2 not in average[key1]:
					average[key1][key2]=weights[key1][key2]
				average[key1][key2]+=weights[key1][key2]
		print("Iteration"+str(i))

	f = open(argv[1],'w+')
	json.dump(average,f)
	f.close()
if __name__=='__main__':
	sys.exit(main(sys.argv[1:]))

