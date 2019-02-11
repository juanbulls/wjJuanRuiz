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
print('Correlacion Tema a la edad de quien escribe en el blog')
print('------------------------------------------------')
print('calculando largo...', end='')
largo = sum(1 for line in open(url, encoding='utf-8'))
print(str(largo)+' lineas\n')
adatos = open(url, 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)
corrtae = []
c=0
anchoavo=1
barra('indexando temas-')
for i,f in enumerate(datos):
    if i == 0: continue #sacar encabezado
    if i == int((largo/ancho)*anchoavo): #actualizando barra
        anchoavo +=1
        print('-', end='', flush=True)
    unico = True
    for j in range(len(corrtae)):
        if corrtae[j][0] == f[3]:
            unico = False
    if unico == True:
        corrtae.append([])
        corrtae[c].append(f[3])#0 tema
        corrtae[c].append(c)#1 xi correspondiente numerico al tema
        corrtae[c].append(0)#2 yi edad promedio (inconcluso)
        corrtae[c].append(0)#3 (xi-x)^2 x=tema (inconcluso)
        #xi-x = tema menos promedio de temas
        corrtae[c].append(0)#4 (yi-y)^2 x=edad avg (inconcluso)
        #yi-y = avg de edad del tema menos avg del avg de temas
        corrtae[c].append(0)#5 (xi-x)(yi-y) (inconcluso)
        c+=1
print('-]\n')
adatos.close()
adatos = open(url, 'r', encoding='utf-8')
datos=csv.reader(x.replace('\0','') for x in adatos)
avguno = 0
avgdos = 0
anchoavo=0
barra('promediando y calculando')
for i in range(c):
    edad = []
    if i == int((c/ancho)*anchoavo): #actualizando barra
        anchoavo +=1
        print('-', end='', flush=True)
    adatos = open(url, 'r', encoding='utf-8')
    datos=csv.reader(x.replace('\0','') for x in adatos)
    for p,g in enumerate(datos):
        if g[3] == corrtae[i][0]:#si corresponde al mismo tema
            edad.append(int(g[2]))#indexa edad
    adatos.close()
    avguno += corrtae[i][1]#sumatoria numeros de temas
    avgdos += sum(edad)/len(edad)#sumatoria promedios de edades
    corrtae[i][2] = sum(edad)/len(edad) #2 yi edad promedio (concluido)
print('-]\n')
avguno = avguno/c #promediando sumatoria
avgdos = avgdos/c #promediando sumatoria de promedios
Suno = 0
Sdos = 0
avgunodos = 0
for i in range(c):
    corrtae[i][3] = (corrtae[i][1]-avguno)*(corrtae[i][1]-avguno)#(concluido)
    aa = corrtae[i][3]
    corrtae[i][4] = (corrtae[i][2]-avgdos)*(corrtae[i][2]-avgdos)#(concluido)
    bb = corrtae[i][4]
    corrtae[i][5] = (corrtae[i][1]-avguno)*(corrtae[i][2]-avgdos)#(concluido)
    cc = corrtae[i][5]
    Suno += corrtae[i][3]
    Sdos += corrtae[i][4]
    avgunodos += corrtae[i][5]
Suno = Suno/(c-1)
Sdos = Sdos/(c-1)
avgunodos = avgunodos/c
print('Correlacion entre la edad de quien escribe en el blog y el tema:')
print(avgunodos/((c-1)*Suno*Sdos))
corr = sorted(corrtae,key=lambda x: x[0])
sentf = open('correlacion.csv','w')
sentf.write('Tema, n Tema, yi, (xi-x)^2, (yi-y)^2, (xi-x)(yi-y)')
for i in range(c):
    sentf.write('\n')
    linea = str(corr[i][0])+','+str(corr[i][1])+','+str(corr[i][2])+','+str(corr[i][3])+','+str(corr[i][4])+','+str(corr[i][5])
    sentf.write(linea)
sentf.close()
print('escrito en sentimiento.csv')
print()
print('Programa finalizado')
