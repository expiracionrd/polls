def startAuth(login):
    login = login.casefold()
    people = reader()

    # print(people) // Sólo usar en DEBUG
    while login not in people:
        login = input("Error. Ingresa el nombre a continuación: ").casefold()
    else:
        print("Tú pasas.")

def reader():
    people = []
    with open(r"gestion\helper\empleados.txt", encoding="utf-8") as nombres:
        for linea in nombres:
            people.append(linea.split('\n')[0].casefold())
    return people

