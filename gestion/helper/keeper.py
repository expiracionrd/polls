import os, sys

urna = 'votos.txt'

def saveForm(voted):
    voted = voted
    chosen = writter()


    if voted not in chosen:
        writter()
        voted = print("No hay datos a guardar.")
    else:
        print("¡Completado!")
        writter()


# Guarda las respuestas seleccionadas en 'saveForm()'

def writter():
    chosen = []

    with open(urna, 'w', encoding='utf-8') as opciones:
        for lineas in opciones:
            chosen.append(chosen)
        print(chosen)

    # f = open(urna, 'w')
    # f.write('elección'.join(chosen))
    # f.close()
    print(urna)

    return chosen