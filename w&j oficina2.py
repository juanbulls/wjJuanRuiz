import csv
import sys
csv.field_size_limit(sys.maxsize)
adatos = open(r'../blogtext.csv', 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)

tema = []
lim = 20000#16841
print ("indexando temas...")
for f in datos:
    #if c == lim:
    #    break
    unico = True
    for c,t in enumerate(tema):
        if t == f[3]:
            unico = False
            tcant[c] +=1
    if unico == True:
        tema.append([])
        tema.append(f[3])
        tcant.append(1)
print ("temas indexados.")

for c,t in enumerate(tema):
    print(t+' '+str(tcant[c]))
