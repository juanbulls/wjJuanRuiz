import csv
paralineas = open(r'blogtext.csv', 'r', encoding='utf-8')
lineas = len(paralineas.readlines())
paralineas.close()
adatos = open(r'blogtext.csv', 'r', encoding='utf-8')
datos = csv.reader(adatos)

c=0
l=6
print('Muestra de las '+str(l-1)+' primeras lineas de las ' + str(lineas) + ' del blog:')
for f in datos:
    if c==l:
        break
    print(f[5])
    c+=1
print('termine')
