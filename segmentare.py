import re
import os

r = re.compile(b"ATG{[TCAG][TCAG][TCAG]}*{TAA}|{TGA}|{TAG}")

def segmentare(fille_name):
	try:
		f = open(fille_name,"rb")
		g = open(output.txt,"wb")
	except:
		print("Eroare la deschiderea fisierului")

	while f :
		text = f.readlines()
		result = r.search(text)
		g.writelines(result)
	try:
		f.close()
		g.close()
	except:
		print("Eroare la inchiderea fisierului")