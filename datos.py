#Declarar una lista
lista0=[0,1,2,3,4]
print(type(lista0))
print("lista0: ", lista0)
print("lista0[0]: ", lista0[0]) #Mostramos la posicion 0 de la lista

lista1= [23, 3.4, True, 'a', "hola"]
print("lista1: ", lista1)
print("lista1[4]: ", lista1[4]) #Mostramos la posicion 4 de la lista

lista2= [23, [1, 2, [50, 60]], "hola"]

lista21= ['A', 'B', [0, 1, 2], 'D', True]

lista21A= lista21[0:2] #rango de posicion 0 a 2 sin incluir
print("lista21A: ", lista21A)

lista21B=lista21[2]

lista22=[lista21A, lista21B]
print("lista22: ", lista22)

lista3= [i for i in range(10)]
print("lista3: ", lista3)

lista31=lista3[0:10:2]
print("lista31: ", lista31)

lista32=lista3[1:10:2]
print("lista32: ", lista32)


lista33=lista3[:5:]
print("lista33: ", lista33)

lista34=lista3[-1:-11:-1]
print("lista 34: ", lista34)

lista4=[i for i in range(100) if i % 3 == 0]
print("lista4: ", lista4)

lista51= [0,1,2,3]
lista52=['A','B','C','D']

lista5=[lista51]
lista5.append(lista52)
print(lista5)

lista6=[lista51]
lista6.extend(lista52)
print(lista6)