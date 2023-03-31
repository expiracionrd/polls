def startAuth():
    login = input("Ingresa el nombre a continuación: ").casefold()
    people = reader()

    # print(people) // Sólo usar en DEBUG
    while login not in people:
        login = print("Error. Intenta de nuevo. ")
        return startAuth()
    else:
        print("Tú pasas.")


def reader():
    people = []
    with open(r"C:\Users\yordy\OneDrive\Escritorio\proyecto\encuesta\gestion\private\empleados.txt", encoding="utf-8") as nombres:
        for linea in nombres:
            people.append(linea.split('\n')[0].casefold())
    return people
    
startAuth()
