import random
menu_option = ""
wins = 0
loose = 0

while menu_option != "3":
    print(f"----- Cachipun -----\n"
          f"1. Quiero jugar\n"
          f"2. Quiero saber los resultados\n"
          f"3. Salir")

    menu_option = input()

    if(menu_option == "1"):
        user_option = input("Escoge entre piedra, papel o tijeras:\npara terminar escribe salir.\n").lower().strip()
        computer_choice = random.choice(["piedra", "papel", "tijeras"])

        if (user_option != "tijeras" and user_option != "papel" and user_option != "piedra" and user_option != "salir"):
            print("escribe una opción válida")

        print(f"elegiste {user_option}")
        print(f"la computadora eligió {computer_choice}")

        if((user_option == "tijeras" and computer_choice == "papel") or (user_option == "piedra" and computer_choice == "tijeras") or (user_option == "papel" and computer_choice == "piedra")):
            wins += 1
            print("¡Ganaste!")
        elif((user_option == "piedra" and computer_choice == "papel") or (user_option == "tijeras" and computer_choice == "piedra") or (user_option == "papel" and computer_choice == "tijeras")):
            loose += 1
            print("¡Perdiste!")
        elif(user_option == computer_choice):
            print("Empate")
    elif(menu_option == "2"):
        print(f"Cantidad ganadas usuario: { wins }")
        print(f"Cantidad ganadas computadora: { loose }")
    elif(menu_option == "3"):
        print(f"Gracias por jugar")