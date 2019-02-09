import csv
import sys
url = r'blogtext.csv'
csv.field_size_limit(sys.maxsize)
adatos = open(url, 'r', encoding='utf-8')
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
adatos = open(url, 'r', encoding='utf-8')
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
adatos.close()
print ()
print('temas de mayor a menor:')
temas = sorted(tema,key=lambda x: x[1], reverse=True)
for i in range(t-1):
    print(temas[i][0]+' '+str(temas[i][1]))
print()
print('edades en orden:')
edades = sorted(edad,key=lambda x: x[0], reverse=False)
for i in range(e-1):
    print(edades[i][0]+' '+str(edades[i][1]))
print()
print('escribiendo temas a csv')
temasf = open('temas.csv', 'w')
temasf.write('Tema, Menciones')
for i in range(t-1):
    temasf.write('\n')
    temasf.write(temas[i][0]+','+str(temas[i][1]))
temasf.close()
print('escrito en temas.csv')
print()
print('escribiendo edades a csv')
edadesf = open('edades.csv','w')
edadesf.write('Edad,Menciones')
for i in range(e-1):
    edadesf.write('\n')
    edadesf.write(str(edades[i][0])+','+str(edades[i][1]))
edadesf.close()
print('escrito en edades.csv')
