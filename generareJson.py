import json


def generateJson(file):
    with open(file, 'r') as handler:
        entriesList = []
        line = handler.readline()
        id = 1
        while line:
            line = line.rstrip('\n')
            if line != '------':
                words = line.split(' ')
                gene = words[1]

                start, stop, length = words[0].split('\t')
                entry = dict()
                entry['id'] = id
                entry['start'] = start
                entry['stop'] = stop
                entry['length'] = length
                entry['gene'] = gene
                entriesList.append(entry)
                id += 1
            line = handler.readline()


        jsonOutput = json.dumps(entriesList, indent=4, separators=("", " = "))
        with open('AugustusOutput1Prelucrat.json', 'w') as outputHandler:
            json.dump(jsonOutput, outputHandler)


def viewJsonOutput(file):
    with open(file, 'r') as jsonFile:
        d = json.load(jsonFile)
        print(d)



if __name__ == '__main__':
    generateJson('AugustusOutput1Prelucrat.txt')
    viewJsonOutput('AugustusOutput1Prelucrat.json')

