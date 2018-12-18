import os
import re
def toGeneMy():
	textfile = open("output.txt", 'r')
	gene = []
	content = ""
	reg = re.compile("(ATG)([TCAG]+)(TAA|TAG|TGA)")
	for line in textfile:
		content =line.strip()
		d=reg.findall(content)
		for p in d:
                	a=str(p[0])+str(p[1])+str(p[2])
                	gene.append(a)
	textfile.close()
	return gene


def toGeneHis():
	textfile = open("1.2-copie.txt", 'r')
	gene = []
	g = ""
	i=1
	for line in textfile:
		if line[0] == ">":
			gene.append(g)
			g=""
		else:
			line=line.replace('\n','')
			g+=line
	textfile.close()
	return gene



def geneToGene(myGene,hisGene):
	count=0
	lenMyGene=len(myGene)
	lenHisGene=len(hisGene)
	j=3
	for i in range(3, len(hisGene)-3,3):
		while j<=lenMyGene-3:
			if hisGene[i]==myGene[j] and hisGene[i+1]==myGene[j+1] and hisGene[i+2]==myGene[j+2]:
				count+=1
				j+=3
				break
			else:
				j+=3

	if(count>0):
		return  (count+2)/((len(myGene)/3))*100
	else:
		return 0

def maxProcent(myGene,hisOutput):
	procent=0
	gena=0
	for k in range(0, len(hisOutput)):
		p=geneToGene(myGene,hisOutput[k])
		if p>procent:
			procent=p
			gena=k
	return (str(round(procent,2)) + "% cu gena " + str(gena))


def compara():
	myOutput=toGeneMy()
	hisOutput=toGeneHis()
	lenMyOutput=len(myOutput)
	lenHisOutput=len(hisOutput)
	count = 0
	found=0
	gena=myOutput[1]
	for i in range(0, lenMyOutput):
		for j in range(0, lenHisOutput):
			if myOutput[i] == hisOutput[j]:
				count+=1
				found=1
				print ("Gena mea "+ str(i)+" identica cu " + str(j) + " -->total perfecte " + str(count))
				hisOutput[j]=""
				break
			else:
				found=0
		if found==0:
			print ("Gena mea " + str(i)+" " + maxProcent(myOutput[i],hisOutput))
			found=0

			
	print ("Sunt " + str(count) + " bune din " + str(lenMyOutput))





compara()

#myOutput=toGeneMy()
#hisOutput=toGeneHis()
#print( myOutput[8]+ "<a mea  - a lui> "+ hisOutput[75522])


