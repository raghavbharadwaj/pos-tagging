import sys
import os
import json
import operator
import random
def main(argv):
	words = []
	average = {}
	weights = {}
	flearn = open(argv[0],'r',encoding='latin-1',errors='strict',buffering=1)
	contents = []
	for line in flearn:
		contents.append(line)
	flearn.close()
	for i in range(1,10):
		random.shuffle(contents)
		for line in contents:
			features=line.split()[1:]
			label = line.split()[0]
			total=0
			temp=0
			pred_label=""
			if label not in weights:
				weights[label]={}
				average[label]={}
			for plabel in weights.keys():
				for feat in features:		
					if feat not in weights[plabel]:
						weights[plabel][feat]=0
				for feat in features:
					temp+= weights[plabel][feat]
				if temp > total:
					total = temp
					pred_label = plabel
			if label!=pred_label:
				for feat in features:
					weights[label][feat]+=1
				if pred_label!="":
					for feat in features:
						weights[pred_label][feat]-=1
		
		for key1 in weights.keys():
			for key2 in weights[key1].keys():
				if key2 not in average[key1]:
					average[key1][key2]=weights[key1][key2]
				average[key1][key2]+=weights[key1][key2]
		print("Iteration"+str(i))
	f = open(argv[1],'w+',encoding='latin-1')
	json.dump(average,f)
	f.close()
if __name__=='__main__':
	sys.exit(main(sys.argv[1:]))

