import sys
import os
import json
import operator
import random
import imp
impname = imp.load_source('perceplearn','../perceplearn.py')
def makefeature():
	fcontents = codecs.open(sys.argv[1],'r',encoding='latin-1',errors='strict',buffering=1)
	words = []
	for line in fcontents:
		words +=line.split()
	words = [ 'BOS' ] + words + [ 'EOS' ]
	newwords = []
	fout = open('pos_training.txt','w+')
	for i in range(1,len(words)-1):
		label = words[i].rsplit('/',1)
		newwords = []
		newwords +=label[1] +" prev:"+words[i-1].rsplit('/',1)[0]+" cur:"+words[i].rsplit('/',1)[0]+" nex:"+words[i+1].rsplit('/',1)[0]
		wordstring = ''.join(newwords)
		print(wordstring,file=fout)
		
	words_new=[]
	fout.close()
	fcontents.close()
makefeature()
mylist=['pos_training.txt',sys.argv[2]]
#perceplearn.main(mylist)
impname.main(mylist)

