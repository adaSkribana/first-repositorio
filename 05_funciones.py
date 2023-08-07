print("*********************************************")
print("**sintaxis basica para declarar una funcion**")
print("*********************************************")
print("*********************************************")
print("**def name_fuction(quere, cibe)**************")
print("**      'instruccion'************************")
print("*********************************************")
print("*********************************************")
print("Llamo print(name_fuction)********************")
print("*********************************************") 

#tabla de multiplicar
def table_multiplex(n):
    for i in range(1, 11 ,1):
       result= n*i
       print(f"la tabla del {n} * {i} = {result}")

print(table_multiplex(6))

#funcio con return
def fuction(n):
    return(n)
print(fuction(7))

#example
def val_input(e):
    return(f"El numero ingresado: {e}")
print(val_input(23.987)) 

#example cadena
def cadena():
    return("curso de python")
print(cadena())

#example 

def sum(a,b):
    return(a+b)

respuesta= (sum(33, 2))
print(respuesta)    
print(sum(12, 3))

#separar lista en pares e impares

def separate_list(lista):
    lista.sort()
    even=[]
    odd=[]
    for element in lista:
        if element %2 ==0:
            even.append(element)
        else:
            odd.append(element)
    return(even, odd)

ejemplo=[1, 2, 3, 4, 5]    
even,odd= separate_list(ejemplo)
print(f"Numeros pares:{even},Numeros impares:{odd}" )

def resta_num( a):
    result= (a-a)
    if a < a:
     return (result)

resta_num(32-10)
resta_num(10-32)



