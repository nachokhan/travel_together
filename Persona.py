class Persona:
    def __init__(self, nombre, latitud, longitud, vehiculo=None):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.vehiculo = vehiculo
        self.ubicacion = (latitud, longitud)
