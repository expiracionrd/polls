# import os, sys

# login = input("Ingresa el nombre a continuación: ").capitalize()
# if login == "hola":
#     return("Tú pasas")
# else:
#     print("Intenta de nuevo." + "\n" + login) * 2


def startAuth():
    login = input("Ingresa el nombre a continuación: ").casefold()

    people = reader()

    print(people)
    while login not in people:
        login = input("Error. Ingresa el nombre a continuación: ")
    else:
        print("Tú pasas.")


def reader():
    people = []
    with open(r"C:\Users\yordy\OneDrive\Escritorio\proyecto\encuesta\gestion\private\empleados.txt", encoding="utf-8") as nombres:
        for linea in nombres:
            people.append(linea.split('\n')[0].casefold())
    return people
    
startAuth()
