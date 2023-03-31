def startAuth(login):
    login = login.casefold()
    people = reader()

    # print(people) // Sólo usar en DEBUG
    while login not in people:
        login = input("Error. Ingresa el nombre a continuación: ").casefold()
    else:
        print("Tú pasas.")

def saveForm(voted):
    voted = voted
    option = writter() 

    print(option)
    while voted not in option:
        voted = print("No hay datos a guardar.").append()
    else:
        print("¡Completado!")

# Busca los archivos en la database para ser enviardos a 'startAuth()'

def reader():
    people = []
    with open(r"gestion\helper\empleados.txt", encoding="utf-8") as nombres:
        for linea in nombres:
            people.append(linea.split('\n')[0].casefold())
    return people

# Guarda las respuestas seleccionadas en 'saveForm()'

def writter():
    vote = []
    with open("gestion\helper\votos.txt", mode='a', encoding="utf-8") as selectos:
     for palabras in selectos:
        vote.append(palabras.append())
    return vote