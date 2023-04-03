from matplotlib import pyplot
import json

ruta = './data.json'

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
            
    print(bonos,canasta,fiesta)


    

    

# if __name__ == '__main__':
#     slices = (100, 15, 3)
#     preferencias = ('Bonos', 'Canasta', 'Fiesta')
#     colores = ('red', 'blue', 'yellow')
#     pyplot.pie(slices, colors= colores)
#     pyplot.show()