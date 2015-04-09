import sys
import os
import json
import io
fjson = open(sys.argv[1],'r')
weights = json.load(fjson)

def wordclass(features,weights):
	pred_sum=0
	pred_label=""
	for label in weights.keys():
		temp_sum=0
		for feat in features:
			if feat in weights[label]:
				temp_sum += weights[label][feat]
		if temp_sum >= pred_sum:
			pred_sum = temp_sum
			pred_label=label
	return pred_label
def dev(weights):
	for feature in io.open(sys.stdin.fileno(),'r',encoding='latin-1'):
		features  = feature.split()
		pred_pos=wordclass(features,weights)
		print(pred_pos)
dev(weights)



