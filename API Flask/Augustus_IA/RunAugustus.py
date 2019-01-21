import os
import sys


def runaugustus(genesPath, species='arabidopsis'):
    runCommand = "./Augustus/bin/augustus --species=" + species + "  --strand=both --singlestrand=false --genemodel=partial --codingseq=on --sample=100 --keep_viterbi=true --alternatives-from-sampling=true --minexonintronprob=0.2 --minmeanexonintronprob=0.5 --maxtracks=2 " + genesPath + " --exonnames=on > AugustusOutput.txt"
    os.system(runCommand)


#print((runCommand))