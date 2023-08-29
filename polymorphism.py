class Coche():

    def desplazamiento(self):

        print("Me desplao utilizando 4 ruedas")

class Moto():

    def desplazamiento(self):

        print("Me desplazo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):

        print("Me desplazo utilizando 6 ruedas")

def desplazamiento_vehiculo(vehiculo):

    vehiculo.desplazamiento()


miVehiculo=Camion()

desplazamiento_vehiculo(miVehiculo)

