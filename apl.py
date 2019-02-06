import csv
lineas=681285
#lineas = len(paralineas.readlines())
#paralineas.close()
adatos = open(r'blogtext.csv', 'r', encoding='utf-8')
datos = csv.reader(adatos)

tema = []
c=0
l=16844
print('Muestra de las '+str(l-1)+' primeras lineas de las ' + str(lineas) + ' del blog:')
try:
    for f in datos:
        if c==l:
            c+=1
            continue
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
print('termine en c=' + str(c))
