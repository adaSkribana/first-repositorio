fruits={"manzana": 2.599,
        "platano": 3.299,
        "guinda": 1.989
        }
print (f"Ejemplificando el metodo pop()\n +Mi contenido inial+ \n {fruits}")

dejo=fruits.pop("platano")
print(f"Aplicando metodo pop\n +Contenido resultante+\n {fruits} \n +Contenido eliminado+ \n {dejo}")

print("Ejemplo de error, correct")
dejo=fruits.pop("", 3.299)
print(f"Aplicando metodo pop\n {dejo}\n +Contenido resultante+\n {fruits}")

print("Ejemplo de error")
dejo=fruits.pop("cafe")
print(f"Aplicando metodo pop\n {dejo}\n +Contenido resultante+\n {fruits}")
