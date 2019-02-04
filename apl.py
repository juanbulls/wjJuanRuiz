import csv
adatos = open(r'blogtext.csv', 'r', encoding='utf-8')
datos = csv.reader(adatos)
print('Muestra del csv en datos, contador = c:')
c=0
for f in datos:
    if c==3:
        break
    print(f[5])
    c+=1
print('termine')
