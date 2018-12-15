import os
import re

def segment(path):
    if os.path.isfile(path):
        nr=0
        try:
            handle = open(path, mode='r')
            g=open('output.txt','w')
        except Exception as e1:
            print("Eroare la deschiderea fisierului", e1)
        g.write('>Just the usual bogus header\n')
        content = ""
        minGeneLength = 200 * 3
        next(handle)

        c=handle.readline()
        while c!='':
            k=0
            con=''
            con+=c
            c2=''
            while '>chr' not in c and c!=None:
                c=handle.readline()
                print(len(c))
                if not '>chr'in c:
                    con += c
                k+=1
                if c=='':
                    print(nr)
                    break
            print(k)
            con=con.replace('\n','')
            con=con.replace(' ','')
            print(con)
            print('pas1')
            lastSTOP = 0
            start = 0
            stop = 0
            while start!=-1:
                print(start,lastSTOP)
                l=con.find('ATG',lastSTOP)
                if l==start:
                    break
                start= con.find('ATG', lastSTOP)
                for i in range(start, len(con), 3):
                    # Define the codon
                    codon = con[i:i + 3]
                    # Check to see if it is a STOP codon
                    if codon in ["TAA", "TGA", "TAG",'NNN']:
                        stop = i + 3
                        break
                gena = con[start:stop]
                if stop - start >= minGeneLength and 'N' not in gena:
                    line="{0}\t{1}\t{2}\t{3}\n------\n".format(start + 1, stop + 1, stop - start,gena)
                    g.write(line)
                    nr+=1
                    lastSTOP = stop
                    print(nr)
                else:
                    lastSTOP=stop
                if start==-1:
                    break
            print('peste')
            c = handle.readline()
            if c == None:
                break

        handle.close()
        g.close()



segment('1.1.D41_genom_secventa_nucleotide.txt')

