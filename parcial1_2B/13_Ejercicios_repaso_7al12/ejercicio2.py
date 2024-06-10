# 2.-Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120, y luego mostrar la lista: Usar un while y for
list=[]
i=0
while len(list)<120:
    list.append(i)
    i+=1
#for
for i in range(120):
    list.append(i)

print(list)