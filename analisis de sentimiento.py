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
print('Sentimiento: positivo y negativo')
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
        tema[t].append(0)
        tema[t].append(0)
        t+=1
print('-]')
print()
adatos.close()
positivas = []
po = open(r'positive-words.txt', 'r')
posi=csv.reader(x.replace('\0','') for x in po)
for p in posi:
    positivas.append(p[0])
negativas = []
ne = open(r'negative-words.txt', 'r')
nega=csv.reader(x.replace('\0','') for x in ne)
for n in nega:
    negativas.append(n[0])
adatos = open(url, 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)
anchoavo=1
barra('analisando sentimiento')
for a,b in enumerate(datos):
    if a == int((largo/ancho)*anchoavo): #actualizando barra
        anchoavo +=1
        print('-', end='', flush=True)
    pos=0
    neg=0
    for np in range(len(positivas)):
        if positivas[np] in b[6]:
            pos+=1
    for nn in range(len(negativas)):
        if negativas[nn] in b[6]:
            neg+=1
    if pos!=0 or neg!=0:
        for k in range(len(tema)):
            if tema[k][0]==b[3]:
                tema[k][2] = pos
                tema[k][3] = neg
                break
print('-]')
print ()
adatos.close()
print('temas, nombramientos, positivos, negativos:')
temas = sorted(tema,key=lambda x: x[1], reverse=True)
for i in range(t-1):
    print(temas[i][0]+' '+str(temas[i][1])+' '+str(temas[i][2])+' '+str(temas[i][3]))
print('escribiendo sentimiento a csv')
sentf = open('sentimiento.csv','w')
sentf.write('Edad,Menciones')
for i in range(t-1):
    edadesf.write('\n')
    edadesf.write(str(edades[i][0])+','+str(edades[i][1])+','+str(edades[i][2])+','+str(edades[i][3]))
edadesf.close()
print('escrito en edades.csv')
print()
print('Programa finalizado')
