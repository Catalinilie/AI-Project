import json
import re

r = re.compile("\s[0-9]+\s[0-9]+\s")


def getGeneID(inString):
    idGene = re.compile("\Achr\w+").search(inString)
    return idGene[0]


def getStartStopGeneAndLen(inString):
    pos = r.findall(inString)[0].replace('\t', ' ')
    pos = re.compile("(\d+)").findall(pos)
    lista = []
    lista += [pos[0]]
    lista += [pos[1]]
    lista += [int(pos[1]) - int(pos[0])]

    return tuple(lista)


def getCodingSequence(line, fh):
    gene = line
    line = fh.readline()
    while '# protein sequence = [' not in line:
        gene += line
        line = fh.readline()

    gene = gene.replace("# coding sequence = [", '').replace('# ', '').replace(']', '').replace('\n', '')
    # gene += '\n'
    return gene


def generareJSON(lista, id):
    entriesList = []
    currentGene=''
    lastGene=lista[0][0]
    idNR=0
    for i in lista:
        id=''
        gene = i[2]
        start, stop, length = i[1]
        currentGene=i[0]
        if currentGene==lastGene:
            id=currentGene+'g'+str(idNR)
            idNR+=1
        else:
            idNR=0
            id = currentGene + 'g' + str(idNR)
            idNR+=1
            lastGene=currentGene
        entry = {}
        entry["id"] = id
        entry['start'] = start
        entry['stop'] = stop
        entry['length'] = length
        entry['gene'] = str.upper(gene)
        entriesList+=[entry]

    jsonOutput = json.dumps(entriesList, indent=4, separators=("", " =,"))
    with open('AugustusOutputPrelucrat' + str(id) + '.json', 'w') as outputHandler:
        json.dump(jsonOutput, outputHandler)



def viewJsonOutput(file):
    with open(file, 'r') as jsonFile:
        d = json.load(jsonFile)
        print(d)
        fh1 = open("AugustusOutput1Prelucrat", "w")
        fh1.write(d)

def prelucrare(id):
    listaGene=[]
    lista = []
    printat = 0
    fh = open("AugustusOutput.txt", "r")
    # fh = open("test.txt", "r")
    #fh1 = open("AugustusOutput1Prelucrat", "w")
    line = fh.readline()
    while line != '':

        if '# start gene' in line:
            position = fh.readline()
            idGene = getGeneID(position)
            lista += [idGene]
            #fh1.write(idGene)

            tupla = getStartStopGeneAndLen(position)
            lista += [tupla]

            #fh1.write(str(tupla))
            printat = 1
        if '# coding sequence = [' in line and printat == 1:
            gene = getCodingSequence(line, fh)
            lista += [gene]

            #fh1.write(gene)
            #fh1.write("\n------\n")

            printat = 0
        if printat == 0 and lista != []:
            listaGene+=[lista]
            lista = []
        line = fh.readline()
    generareJSON(listaGene, id)
    #viewJsonOutput('AugustusOutput.json')

#prelucrare()
