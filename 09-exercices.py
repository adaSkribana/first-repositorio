user_option=float(input("Ingrese la nota minimo de aprobacion"))
avereges={"Helen": 4.0,
          "Osman": 5.5,
          "Tamara": 5.8,
          "Elizabeth": 6.0,
          "Idriams": 4.0,
          "Aaron": 6.6
          }

grades_values= avereges.values() 
list(grades_values)
print (grades_values)
names_keys= avereges.keys()
list(names_keys)
print (names_keys)
list_items= avereges.items()
list(list_items)
print(list_items)
for k, v in list_items:
    print(f"Nombre estudiante: {k}, su promedio: {v}")
students=[ ]

for grade in grades_values:
 for name in names_keys:
   students.append(name)
   if grade >= user_option:
       print(f"el estudiante {name}")
       print(f"Ha aprobado con promedio: {grade}")
   elif grade < user_option:
        print(f"el estudiante {name }")
        print (f"Ha reprobado con promedio{grade}") 

                                