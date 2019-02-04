import csv
paralineas = open(r'blogtext.csv', 'r', encoding='utf-8')
lineas = len(paralineas.readlines())
paralineas.close()
adatos = open(r'blogtext.csv', 'r', encoding='utf-8')
datos = csv.reader(adatos)

tema = []
c=0
l=6
print('Muestra de las '+str(l-1)+' primeras lineas de las ' + str(lineas) + ' del blog:')
try:
    for f in datos:
        #if c==l:
        #    break
        unico = True
        for t in tema:
            if t == f[3]:
                unico = False
        if unico == True:
            tema.append(f[3])
            print(str(c) + ' incluido: ' + f[3])
        c+=1
except:
    print("Error en la fila " + str(c))
print('termine')
