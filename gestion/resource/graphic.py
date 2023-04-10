from matplotlib import pyplot
import json, io, base64, urllib

ruta = './data.json'

def resultados():

    bonos = 0
    canasta = 0
    fiesta = 0


    with open(ruta, 'r') as archivo:
        datos = json.load(archivo)


        for i in datos:
            if i['eleccion'] == 'Bonos':
                bonos = bonos+1

            elif i['eleccion'] == 'canasta':
                canasta = canasta+1

            elif i['eleccion'] == 'fiesta':
                fiesta = fiesta+1


            totalB = bonos+1
            totalC = canasta+1
            totalF = fiesta+1
        print( "Bonos:",bonos, "Canastas:",canasta, "Fiesta:",fiesta)

    ejeX = (totalB, totalC, totalF)
    ejeY = ('Bonos', 'Canasta', 'Fiesta')
    pyplot.bar(ejeY, ejeX)
    pyplot.savefig('gestion/static/graficos.png',  bbox_inches='tight')