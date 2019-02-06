import csv
import sys
csv.field_size_limit(sys.maxsize)
adatos = open(r'blogtext.csv', 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)

tema = []
t=0
print ("indexando temas...")
for i,f in enumerate(datos):
    unico = True
    for j in range(len(tema)):
        if tema[j][0] == f[3]:
            unico = False
            tema[j][1] += 1
    if unico == True:
        tema.append([])
        tema[t].append(f[3])
        tema[t].append(1)
        t+=1
print ("temas indexados.")

for i in range(t):
    print(tema[i][0]+' '+str(tema[i][1]))
print()
print('organizados:')
temas = sorted(tema,key=lambda x: x[1], reverse=True)
for i in range(t):
    print(temas[i][0]+' '+str(temas[i][1]))
