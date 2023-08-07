print("TIPOS DE LISTAS\n :Las listas pueden contener valores de distintos tipos de datos:")
print([1, 2, 3, 4, 5])
print(["a", "b", "i", "o", "u"])
print([1.1, 2.1, 3.1, 4.1, 5.1])
print([1, 2.1, "Emily", 4.5])
print("Asignando mis listas a una variable")
numbers=[1, 2, 3, 4, 5]
vowels=["a", "b", "i", "o", "u"]
type_float=[1.1, 2.1, 3.1, 4.1, 5.1]
type_mixer=[1, 2.1, "Emily", 4.5]
print(f"El contenido de mi variable 'numbers':{numbers}")
print(f"El contenido de mi variable 'vowels':{vowels}")
print(f"El contenido de mi variable 'type_float': {type_float}")
print(f"El contenido de mi variable 'type_mixer'{type_mixer}")
print("LISTAS EN LISTAS: LISTAS ANIDADAS:")
list_nested=[[1, 2, 3 ], [ 4, 5]]
list_simple=[1, 2, 3, 4, 5]
print(list_nested)
print("ACCEDIENDO A LOS ELEMENTOS DE MI LISTA ANIDADA")
print(f"El elemento de mi lista 'list_nested[0]' posicion 0: {list_nested[0]}")
print(f"El elemento de mi lista 'list_nested[1]' posicion 1: {list_nested[1]}")
print(f"El elemento de mi lista 'list_nested[0][1]' posicion 0 posicion 1: {list_nested[0][1]}")
print(f"El elemento de mi lista 'list_nested[1][0]' posicion 1 posicion: {list_nested[1][0]}")
print("FUNCION LEN() = TAMAÑO DE UNA LISTA")
print(f"La longitud de mi list_nested:{len(list_nested)}")
print(f"La longitud de mi list_nested[0] posicion 0 : {len(list_nested[0])}")
print(f"La longitud de mi list_nested[1] posicion 1 : {len(list_nested[1])}")
print("MODIFICANDO LOS ELEMENTOS DE MI LISTA")
print(f"Mi lista original {list_simple}")
list_simple[0]=0 
#ordeno que en mi lista simple se modifique el elemento en la posicion 0 por el numero '0'
print(f"Mi lista modificada {list_simple}")
print("AGREGANDO NUEVOS ELEMENTOS A MI LISTA .append() ")
list_simple.append(6)
list_simple.append(7)
list_simple.append(8)
#ordeno que en mi lista simple se agregen los elementos 
print(f"Mi lista con los nuevos elementos {list_simple}")
print("REMOVIENDO ELEMENTOS A MI LISTA .remove() ")
list_simple.remove(4)
list_simple.remove(0)
list_simple.remove(7)
#ordeno que en mi lista simple se remuevan los elementos 
print(f"Mi lista con los nuevos elementos {list_simple}")
print(f"IDEXACION DE LISTAS\n El contenido de mi lista: {list_simple}")
print(f"sintaxis basica para ingresar a una lista [inicio:fin:salto ]")
print(f"sintaxis basica para el indice en una lista ['1, 2, 3, 4, 5' ]")
print(f"sintaxis basica para el indice en una lista ['0  1  2  3  4' ]")
print(f"el elemento de mi lista posicion 3:  {list_simple[3]}")
print(f"los elementos de mi lista de inicio a fin de dos en dos:  {list_simple[: :2]}")
print(f"los elemento de mi lista en posicion 0 al 3:  {list_simple[0:3]}")
print(f"los elemento de mi lista en posicion 3 al 5 :  {list_simple[3:5]}")
#recordar que el corte se realiza una posicion antes de la señalada
me_list=[1, 15, 3, 3, 4, 5, 6, 7, 8, 2, 2]
print(f"APLICANDO METODOS A MI LISTA: \nEl contenido inicial de mi lista: {me_list}")
print(f"El contenido de mi lista con metodo .extend(): {me_list.extend([6, 7, 8])}")
print(f"El contenido de mi lista con metodo .pop():{me_list.pop()}")
print(f"El contenido de mi lista con metodo .index(6):{me_list.index(6)}")
print(f"El contenido de mi lista con metodo .count(2): {me_list.count(2)}")
print(f"El contenido de mi lista con metodo .sort(): {me_list.sort()}")
print(f"El contenido de mi lista con metodo .reverse(): {me_list.reverse()}")
print(f"El contenido de mi lista con metodo .clear(): {me_list.clear()}")
me_tupla=[1, 15, 3, 3, 4, 5, 6, 7, 8, 2, 2]
me_tupla_nested=[ [1, 15, 3, 3, 4 ], [5, 6, 7, 8, 2, 2 ] ]
print("TUPLAS\n :Las tupla pueden contener valores de distintos tipos de datos:")
print(f"IDEXACION DE tuplas\n El contenido de mi tupla: {me_tupla}")
print(f"sintaxis basica para ingresar a una tupla [inicio:fin:salto ]")
print(f"sintaxis basica para el indice en una tupla [1, 15, 3, 3, 4, 5, 6, 7, 8, 2, 2 ]")
print(f"sintaxis basica para el indice en una tupla ['0  1  2  3  4  5  6  7  8  9  10' ]")
print(f"el elemento de mi tupla posicion 3:  {me_tupla[3]}")
print(f"los elementos de mi tupla de inicio a fin de dos en dos:  {me_tupla[: :2]}")
print(f"los elemento de mi tupla en posicion 0 al 3:  {me_tupla[0:3]}")
print(f"los elemento de mi tupla en posicion 3 al 5 :  {me_tupla[3:5]}")
#recordar que el indice va siempre de izquierda a derecha, de caso contrario debemos comenzar con -1
print("ACCEDIENDO A LOS ELEMENTOS DE MI TUPLA ANIDADA")
print(f"El elemento de mi lista 'me_tupla_nested[0]' posicion 0: {me_tupla_nested[0]}")
print(f"El elemento de mi lista 'me_tupla_nested[1]' posicion 1: {me_tupla_nested[1]}")
print(f"El elemento de mi lista 'me_tupla_nested[0][1]' posicion 0 posicion 1: {me_tupla_nested[0][1]}")
print(f"El elemento de mi lista 'me_tupla_nested[1][0]' posicion 1 posicion: {me_tupla_nested[1][0]}")
print("FUNCION LEN() = TAMAÑO DE UNA TUPLA")
print(f"Mi tupla anidada original {me_tupla_nested}")
print(f"La longitud de mi tupla anidada:{len(me_tupla_nested)}")
print(f"La longitud de mi tupla[0] posicion 0 :{len(me_tupla_nested[0])}")
print(f"La longitud de mi tupla[1] posicion 1 :{len(me_tupla_nested[1])}")
print(f"Mi tupla original {me_tupla}")
print(f"La longitud de mi tupla :{len(me_tupla)}")
print(f"La longitud de mi tupla[0][6] posicion 0 hasta 6 :{len(me_tupla[1])}")
print(f"La longitud de mi tupla[-1][-10] posicion -1 hasta -10 :{len(me_tupla)[-1][-10]}")
print(f"APLICANDO METODOS A MI TUPLA: \nEl contenido inicial de mi tupla: {me_tupla}")
print(f"Mi tupla con metodo .count(6): {me_tupla.count(6)} ")
print(f"Mi tupla con metodo .index(7): {me_tupla.index(7)} ")
#recordad a diferencia de las listas las tuplas son inmutables es decir que
#no se puede modificar , actualizar, remover ni añadir
#en caso de requerir se puede hacer copia nueva de la tupla
print("ASIGNACION DE UNA TUPLA")
print(f"Mi tupla original {me_tupla}")
me_tupla=("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",)
print(f"Mi tupla con valores asignados {me_tupla}")

