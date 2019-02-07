import csv
import sys
csv.field_size_limit(sys.maxsize)
adatos = open(r'blogtext.csv', 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)

tema = []
edad = []
t=0
e=0
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
print ("indexando edades...")
adatos.close()
adatos = open(r'blogtext.csv', 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)
for p,g in enumerate(datos):
    unico = True
    for q in range(len(edad)):
        if edad[q][0] == g[2]:
            unico = False
            edad[q][1] += 1
    if unico == True:
        edad.append([])
        edad[e].append(g[2])
        edad[e].append(1)
        e+=1
print ()
print('temas de mayor a menor:')
temas = sorted(tema,key=lambda x: x[1], reverse=True)
for i in range(t):
    print(temas[i][0]+' '+str(temas[i][1]))
print()
print('edades en orden:')
edades = sorted(edad,key=lambda x: x[0], reverse=False)
for i in range(e):
    print(edades[i][0]+' '+str(edades[i][1]))
