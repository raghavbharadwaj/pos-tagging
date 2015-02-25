import sys
import os
import json
import operator
import random
import perceplearn
fcontents = open(sys.argv[1],'r',errors='ignore')
words = []
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
fcontents.close()
mylist=[sys.argv[2]]
perceplearn.main(mylist)
