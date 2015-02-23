import sys
import os
import json
import operator

fcontents = open(sys.argv[1],'r')
fd = open('fdict','r')
words = []

weights = json.load(fd)

def wordclass(word,weights):
	if word not in weights.keys():
		return 0
	else:
		return max(weights[word].items(),key = operator.itemgetter(1))[0]

for line in fcontents:
	words +=line.split()
success_count=0
total_count=0
for word in words:
	wordpos = word.rsplit('/',1)
	pred_pos = wordclass(wordpos[0],weights)
	if wordpos[1]==pred_pos:
		success_count+=1
	total_count+=1
print(success_count/total_count)
fcontents.close()
fd.close()
	
