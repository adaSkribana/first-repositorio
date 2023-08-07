""""numeros=[1, 2, 3, 4, 5]
print(f"El contenido original de mi lista {numeros}")
numeros_pop=[ ]
numeros_pop.append(numeros.pop(0))
numeros_pop.append(numeros.pop(-1))
print(f"El contenido actual de mi lista {numeros} \n Lista numeros eliminados {numeros_pop} ")
print("***************************************************************")
print("***La ejemplificacion ha finalizado, reinicie para continuar***")
print("***************************************************************")
"""

lista= [ 1, 2, 3, 4, 5]
variable_help=[1, 5, 2, 4, 3 ]
lista_pop= [ ]
var_help2= [ ]
print(f"El contenido inicial es el siguiente:\n lista original: {lista}\n lista de numeros eliminados por sentencia: {lista_pop} \n La ejucucion ha comenzado. ")
while variable_help != lista_pop:
    if lista == var_help2:
        break
lista_pop.append(lista.pop(0))
lista_pop.append(lista.pop())
   
print(f"El contenido resultante es el siguiente:\n lista original modificada: {lista_pop}\n lista de numeros eliminados por el bucle: {lista_pop} \n La ejucucion ha finalizado ")





