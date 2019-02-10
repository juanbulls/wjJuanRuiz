import csv
import sys
url = r'blogtext.csv'
csv.field_size_limit(sys.maxsize)
ancho = 40
def barra(titulo):
    x=titulo
    y = int((ancho-len(x))/2)
    print ('[%s%s%s]' % ('-' * y, x, '-' * y))
    print('[', end='', flush=True)
    
print('\nAplicacion para Whale & Jaguar por Juan Ruiz.')
print('Segmentando por tema y por edad')
print('------------------------------------------------')
print('calculando largo...', end='')
largo = sum(1 for line in open(url, encoding='utf-8'))
print(str(largo)+' lineas\n')
adatos = open(url, 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)
tema = []
edad = []
t=0
anchoavo=1
barra('indexando temas-')
for i,f in enumerate(datos):
    if i == int((largo/ancho)*anchoavo): #actualizando barra
        anchoavo +=1
        print('-', end='', flush=True)
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
print('-]')
print()
adatos.close()
adatos = open(url, 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)
e=0
anchoavo=1
barra('indexando edades')
for p,g in enumerate(datos):
    if p == int((largo/ancho)*anchoavo): #actualizando barra
        anchoavo +=1
        print('-', end='', flush=True)
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
print('-]')
print ()
adatos.close()
print('temas segmentados de mas nombrado a menos:')
temas = sorted(tema,key=lambda x: x[1], reverse=True)
for i in range(t-1):
    print(temas[i][0]+' '+str(temas[i][1]))
print()
print('edades segmentadas en orden por edad:')
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
print()
print('Programa finalizado')
input()
