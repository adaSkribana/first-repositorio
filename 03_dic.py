print(f"DICCIONARIOS EN PYTHON:\n ")
#Las claves del diccionario deben ser de un tipo de dato inmutable. Por ejemplo, pueden ser cadenas de caracteres, números, 
# o tuplas pero no pueden ser listas ya que las listas son mutables (pueden ser cambiadas)
print("Sintaxis basica para declarar un diccionario")
print("{   'a': 1,        'b': 2,          'c': 3}")
print("{'keys':'value', 'keys':'value', 'keys':'value'}")
print("DICCIONARIOS CON DISTINTOS TIPOS DE CLAVES")
me_keys_character={"mover arriba": 1,
                  "mover abajo": 2,
                  "mover a la derecha": 3,
                  "mover a la izquierda": 4
                  }
me_keys_numbers={1: "ciudad zeta",
                2: "ciudad alpha",
                3: "ciudad kromo",
                4: "ciudad titanium"
                }
me_keys_tuplas={(0, 0): "Comienzo",
                (-1, -12): "Meta"}
print(f"Diccionario con clave cadena de caracteres: {me_keys_character}\nDiccionario con clave numerica: {me_keys_numbers}\nDiccionario con clave tuplas: {me_keys_tuplas}\n ")
#Los diccionarios pueden contener valores de cualquier tipo de dato, así que podemos asignar cadenas de caracteres, números, 
# listas, tuplas, conjuntos, e incluso otros diccionarios como valores.
print("DICCIONARIOS CON DISTINTOS TIPOS DE VALORES")
me_value_character={1: "mover arriba",
                  2: "mover abajo",
                  3: "mover a la derecha",
                  4: "mover a la izquierda"
                  }
me_value_numbers={"ciudad zeta": 1,
                "ciudad alpha": 2,
                "ciudad kromo": 3,
                "ciudad titanium": 4
                }
me_value_tuplas={"Comienzo": (-1, -12) ,
               "Meta": (0, 0)
               }
me_value_list={"ingredientes":["tomate", "queso", "salame", "aceitunas", "choclo" ],
               "costo de compras":[1.169, 3.753, 2.455, 1.498, 999 ] }
me_value_dic={"diccionario de vocales":{"a": 1,
                                        "e": 2, 
                                         "i": 3, 
                                        "o": 4},
               "diccionario de frutas": {"manzana": 1.000,
                                        "banana": 1.800,
                                         "naranja": 900,
                                        "melon": 900,
                                         "guinda": 1.500,}
                                        }
print(f"Diccionario con valor de cadena de caracteres: {me_value_character}\nDiccionario con valor numerico: {me_value_numbers}\nDiccionario con valor tuplas: {me_value_tuplas}\nDiccionario con valor de listas: {me_value_list}\nDiccionario con valor diccionario: {me_value_dic}  ")
print("TAMAÑO DE UN DICCIONARIO FUNCION LEN()")
print(f"Longitud de mi 'diccionario claves numericas': {len(me_keys_numbers)}\nLongitud de mi 'diccionario valores numericos': {len(me_value_numbers)}\n")
print("OBTENER EL VALOR DE UN DICCIONARIO CON SU CLAVE")
#print(me_dictionary)['keys']")
#imprimira en pantalla el valor asociado a la clave
#que yo facilite
print((me_keys_numbers)[1])
print((me_keys_numbers)[2] )
print((me_keys_numbers)[3] )
print((me_keys_numbers)[4] ) 
print("MODIFICAR EL VALOR DE UN DICCIONARIO CON SU CLAVE")
print(f" El contenido original de mi diccionario: {me_keys_numbers}")
(me_keys_numbers)[2]= "Ciudad ciruela" 
(me_keys_numbers)[3]= "Ciudad helado"
(me_keys_numbers)[4]= "Ciudad cerebro"
#se añade el operador es igual '=' para indicar el
#nuevo valor asosiado a nuestra clave
print(f" El nuevo contenido de mi diccionario: {me_keys_numbers}")
print("AÑADIR UN NUEVO PAR CLAVE-VALOR A UN DICCIONARIO ")
print(f" El contenido original de mi diccionario: {me_keys_numbers}")
(me_keys_numbers)[5]= "Ciudad verde" 
(me_keys_numbers)[6]= "Ciudad roja"
(me_keys_numbers)[7]= "Ciudad blanca"
#se añade una nueva clave
# se añade el operador es igual '=' para indicar el
#valor asosiado a nuestra clave
print(f" El nuevo contenido de mi diccionario: {me_keys_numbers}")
print("ELIMINAR UN PAR CLAVE-VALOR DE UN DICCIONARIO ")
print("Sintaxis basica para la funcion 'del' name_dic[keys] ")
print(f" El contenido original de mi diccionario: {me_value_character}")
del me_value_character[4]
print(f" El contenido actual de mi diccionario: {me_value_character}")
#Es correcto decir que un par clave-valor es llamado items
#por tanto los diccionarios estan compuestos por items
print("METODOS EN DICCIONARIOS:")
print(f"El diccionario que ejemplificaremos {(me_value_numbers)}")
print(f"Los items de mi diccionario: {(me_value_numbers.items())}\n**metodo .items()**")
print(f"Las claves de mi diccionario: {(me_value_numbers.keys())}\n**metodo .keys()**")
print(f"Los valores de mi diccionario: {(me_value_numbers.values())}\n**metodo .values()**")
print(f"Contenido de mi diccionario: {(me_value_numbers.pop('ciudad zeta'))}\n**metodo .pop()**")
print(f"Contenido de mi diccionario: {(me_value_numbers.popitem())}\n**metodo .popitem()**")
print("METODOS QUE NECESITAN UNA VARIABLE PARA ALMACENAR ELEMENTO")
help= me_value_numbers.setdefault("ciudad kromo")
help_1= me_value_numbers.get("ciudad kromo")
print(f"Metodo .setdefaul() {help}")
print(f"Metodo .get(): {help_1}")
#La siguiente instruccion la deje aca porque es de limpieza
#al aplicarlo mi diccionario queda vacio y por tanto innutilizable para mis siguientes instrucciones
#pero al dejarlo al final ejemplifica muy bien su funcion
print(f"Contenido de mi diccionario: {(me_value_numbers.clear())}\n**metodo .clear()**")
#El método update()es especialmente útil cuando se amplía 
# un diccionario que tiene pares clave-valor diferentes de otro diccionario
#si tienen las mismas claves se terminara reemplazando el valor asignado
print("Ejemplificando el uso del metodo update({ })")
dic_update={"name": "Jose",
            "age": 28,
            "job": "Asistente educacional"
            }
dic_update_two={"last name": "Hernan",
                "birth year": 1994}
print(f"Mi primer diccionario inicial: {(dic_update)}")
print(f"Mi segundo diccionario inicial: {(dic_update_two)}")
#nombro una tercera variable que guardara la exponenciacion de mis 2 diccionarios(?)
#dic_exponenciacion=(dic_update**dic_update_two)#Instruccion con operadores logicos
#print(f"Comprobando metodos de concatenacion operador'**' :{dic_exponenciacion}")
dic_update.update(dic_update_two)#Instruccion
print(f"La concatenacion de ambos diccionarios iniciales: {dic_update}")
print(f"'Correcta concatenacion' != (no existen) keys repetidas")
dic_update.update({'salary': 399.458, 
                 'workin day': 'full time'
                 })
print(f"Contenido Resultante: {dic_update}") #Instruccion
(dic_update.update({'salary': 101.212,
                    'workin day': 'part time'
                     }))#Instruccion
print(f"'Icorrecta concatenacion' = (existen) keys repetidas\nContenido Resultante: {dic_update}")


