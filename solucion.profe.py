cant_matrix=int(input("¿Cuantas matrices vamos a sumar?: "))
cant_rows=int(input("¿Cuantas filas tendrán las matrices?: "))
cant_column=int(input("¿Cuantas columnas tendran nuestras matrices?: "))

#
# PARTE 1. INGRESO DE LAS MATRICES
#

if cant_matrix > 0 and cant_rows > 0 and cant_column > 0:
  sum_matrix = []

  for matrixIndex in range(cant_matrix):
    print(""
      f"++++  INGRESO DE LA MATRIZ {matrixIndex + 1}"
    "")
    matrix_creator = []

    for actualRowIndex in range(cant_rows):
      for actualColumnIndex in range(cant_column):
        user_value = int(input(f"Introduce el valor para la matriz fila {actualRowIndex + 1} columna {actualColumnIndex + 1}: "))

        # MANEJO DE LA INSERCIÓN DE VALORES EN LA MATRIZ ACTUAL
        if actualColumnIndex == 0:
          matrix_creator.append([user_value])
        else:
          matrix_creator[actualRowIndex].append(user_value)

        #ACTUALIZACIÓN DE LA SUMA
        if matrixIndex > 0: # <-- si ya existe una matriz previa
          sum_matrix[actualRowIndex][actualColumnIndex] += matrix_creator[actualRowIndex][actualColumnIndex]

    if len(sum_matrix) == 0: # <-- la primera vez la suma es igual a la primera matriz, luego se actualiza la suma
      sum_matrix = matrix_creator

    print(f"Matriz{matrixIndex + 1} = {matrix_creator} \n:")
    print(f"Matriz suma actual \n {sum_matrix} \n")

else:
    print("Debe ingresar valores enteros positivos, re-intente por favor.")
    
