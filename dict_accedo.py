print("**********************************")
print("****ACCEDIENDO A LOS ELEMENTOS****")
print("**********************************\n")

dictionary={"a": 1,
            "e": 2, 
            "i": 3, 
            "o": 4
            }

print(f"Diccionario: {dictionary}")
print()
print (f"Clave e: {dictionary['e']}")
print()
print (f"Clave a: {dictionary['a']}")
print()
dictionary={"group": {"a": 1, "e": 2, "i": 3, "o": 4},
            "numbers": [1, 2, 3, 4 ]}

print (f"Diccionario: {dictionary}")
print()
print (f"Clave numbers: {dictionary['numbers']}")
print()
print (f"Clave group: {dictionary['group']}")